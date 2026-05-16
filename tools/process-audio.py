#!/usr/bin/env python3
"""
tools/process-audio.py — Audio enhancement for Framesmith talking-head videos.

Two-pass EBU R128 loudnorm with a high-pass filter, light compression, and
an optional ambient pad mix. No noise reduction, de-essing, or de-popping —
mics with built-in ENC (e.g. Hollyland Lark M2) handle that at capture.

Run this AFTER silence cutting and retake removal, not on raw footage.

Usage:
    python tools/process-audio.py --input edited.mp4 --output processed.mp4
    python tools/process-audio.py --input edited.mp4 --output processed.mp4 \\
        --pad assets/ambient-pad.mp3
    python tools/process-audio.py --input edited.mp4 --output processed.mp4 \\
        --pad assets/ambient-pad.mp3 --pad-volume -24

Requirements:
    ffmpeg (brew install ffmpeg) — already required by Framesmith.
    No additional pip installs.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


# ── Loudnorm targets ───────────────────────────────────────────────────────────
TARGET_LUFS = -16       # YouTube/LinkedIn standard integrated loudness
TARGET_TP   = -1.0      # True peak ceiling (dBTP)
TARGET_LRA  = 11.0      # Loudness range — preserves natural speech dynamics

# ── Compressor ─────────────────────────────────────────────────────────────────
# Threshold: 0.126 linear = -18 dBFS. Light — only catches the top 10-15% of peaks.
# Ratio 3:1 is the standard vocal ratio; keeps speech natural.
# Makeup: 1.413 linear = +3 dB. Recovers gain lost by compression.
COMP_THRESHOLD = 0.126
COMP_RATIO     = 3
COMP_ATTACK    = 5      # ms — fast enough to catch transients
COMP_RELEASE   = 50     # ms — natural, avoids pumping artefacts
COMP_MAKEUP    = 1.413

# ── High-pass filter ───────────────────────────────────────────────────────────
# 80 Hz: removes clothing rustle, HVAC hum, and surface vibration.
# Vocal fundamentals for male and female voices sit well above this.
HIGHPASS_HZ = 80

# ── Limiter ────────────────────────────────────────────────────────────────────
# 0.891 linear = -1 dBFS ≈ -1 dBTP. Hard safety ceiling after loudnorm.
LIMITER_LEVEL = 0.891

# ── Pad defaults ───────────────────────────────────────────────────────────────
PAD_DEFAULT_DB = -22    # Ambient pad level: audible but completely under voice


def run_ffmpeg(cmd):
    """Run an ffmpeg command and return the CompletedProcess."""
    flat = [str(c) for c in cmd]
    print("  $", " ".join(flat))
    return subprocess.run(flat, capture_output=True, text=True, check=False)


def analyze_loudness(input_path: Path) -> dict:
    """Pass 1: measure the input loudness so pass 2 can apply linear loudnorm."""
    print("\n[1/3] Analyzing audio...")
    result = subprocess.run(
        [
            "ffmpeg", "-hide_banner",
            "-i", str(input_path),
            "-af", (
                f"loudnorm="
                f"I={TARGET_LUFS}:"
                f"TP={TARGET_TP}:"
                f"LRA={TARGET_LRA}:"
                f"print_format=json"
            ),
            "-f", "null", "-"
        ],
        capture_output=True, text=True, check=False
    )
    # loudnorm writes its JSON to stderr
    match = re.search(r'\{[\s\S]*?\}', result.stderr)
    if not match:
        print("ERROR: Could not parse loudnorm analysis output.")
        print("ffmpeg stderr:", result.stderr[-2000:])
        sys.exit(1)

    m = json.loads(match.group())
    print(f"  Integrated loudness : {m['input_i']} LUFS  (target: {TARGET_LUFS} LUFS)")
    print(f"  True peak           : {m['input_tp']} dBTP  (ceiling: {TARGET_TP} dBTP)")
    print(f"  Loudness range      : {m['input_lra']} LU")
    return m


def build_filter(m: dict) -> str:
    """Build the ffmpeg audio filter chain using pass-1 measurements."""
    return (
        # 1. Cut low-frequency noise before compression (prevents compressor
        #    reacting to sub-vocal energy and over-attenuating the signal).
        f"highpass=f={HIGHPASS_HZ},"

        # 2. Light compression: evens out the natural peaks-and-valleys in
        #    conversational speech without killing the dynamic feel.
        f"acompressor="
        f"threshold={COMP_THRESHOLD}:"
        f"ratio={COMP_RATIO}:"
        f"attack={COMP_ATTACK}:"
        f"release={COMP_RELEASE}:"
        f"makeup={COMP_MAKEUP},"

        # 3. Linear loudnorm using pass-1 measurements.
        #    linear=true: single deterministic pass using measured values.
        f"loudnorm="
        f"I={TARGET_LUFS}:"
        f"TP={TARGET_TP}:"
        f"LRA={TARGET_LRA}:"
        f"linear=true:"
        f"measured_I={m['input_i']}:"
        f"measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:"
        f"measured_thresh={m['input_thresh']},"

        # 4. Hard limiter: safety ceiling for any inter-sample peaks that
        #    slip through. level=false: don't apply additional output gain.
        f"alimiter=limit={LIMITER_LEVEL}:level=false"
    )


def process(
    input_path: str,
    output_path: str,
    pad_path: str | None = None,
    pad_db: float = PAD_DEFAULT_DB
) -> None:
    inp = Path(input_path)
    out = Path(output_path)

    if not inp.exists():
        print(f"ERROR: Input file not found: {inp}")
        sys.exit(1)

    if pad_path and not Path(pad_path).exists():
        print(f"ERROR: Pad file not found: {pad_path}")
        sys.exit(1)

    measurements  = analyze_loudness(inp)
    voice_filter  = build_filter(measurements)

    print(f"\n[2/3] Applying filter chain...")
    print(f"  High-pass  : {HIGHPASS_HZ} Hz")
    print(f"  Compressor : threshold -18 dBFS, {COMP_RATIO}:1 ratio, +3 dB makeup")
    print(f"  Loudnorm   : {TARGET_LUFS} LUFS target, {TARGET_TP} dBTP ceiling (linear)")
    print(f"  Limiter    : {TARGET_TP} dBTP hard ceiling")
    if pad_path:
        print(f"  Ambient pad: {pad_path} at {pad_db} dB")

    if pad_path:
        # -stream_loop -1 on the pad input loops it indefinitely.
        # amix duration=first cuts the output at the voice track length.
        # -c:v copy never re-encodes the video stream.
        filter_complex = (
            f"[0:a]{voice_filter}[voice];"
            f"[1:a]volume={pad_db}dB[pad];"
            f"[voice][pad]amix=inputs=2:duration=first:dropout_transition=0[out]"
        )
        cmd = [
            "ffmpeg", "-hide_banner", "-y",
            "-i",            str(inp),
            "-stream_loop",  "-1",
            "-i",            str(pad_path),
            "-filter_complex", filter_complex,
            "-map",   "0:v",
            "-map",   "[out]",
            "-c:v",   "copy",
            "-c:a",   "aac",
            "-b:a",   "256k",
            "-shortest",
            str(out)
        ]
    else:
        cmd = [
            "ffmpeg", "-hide_banner", "-y",
            "-i",   str(inp),
            "-af",  voice_filter,
            "-map", "0:v",
            "-map", "0:a",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "256k",
            str(out)
        ]

    result = run_ffmpeg(cmd)
    if result.returncode != 0:
        print("\nERROR: ffmpeg failed.")
        print(result.stderr[-2000:])
        sys.exit(1)

    size_mb = out.stat().st_size / 1_048_576
    print(f"\n[3/3] Done.")
    print(f"  Output : {out}")
    print(f"  Size   : {size_mb:.1f} MB")


def main():
    parser = argparse.ArgumentParser(
        description="Audio enhancement for Framesmith talking-head videos.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Filter chain (applied in this order):
  1. High-pass at 80 Hz        Removes rumble, HVAC hum, clothing noise
  2. Compression 3:1           Evens out peaks-and-valleys in speech
  3. EBU R128 loudnorm -16 LUFS  YouTube-standard loudness, -1 dBTP ceiling
  4. Limiter at -1 dBTP        Hard safety ceiling

Notes:
  Video stream is copied without re-encoding.
  Designed for mics with built-in ENC (Hollyland Lark M2 etc.).
  No noise reduction, de-essing, or fine EQ is applied.
  Run after silence-cut.sh and cut-retakes.py, not on raw footage.

Examples:
  python tools/process-audio.py --input edited.mp4 --output processed.mp4
  python tools/process-audio.py --input edited.mp4 --output processed.mp4 \\
      --pad assets/ambient-pad.mp3
  python tools/process-audio.py --input edited.mp4 --output processed.mp4 \\
      --pad assets/ambient-pad.mp3 --pad-volume -24
        """
    )
    parser.add_argument("--input",      required=True,
                        help="Input video file (post-edit — after silence cut and retake removal)")
    parser.add_argument("--output",     required=True,
                        help="Output video file with processed audio")
    parser.add_argument("--pad",        default=None,
                        help="Ambient pad audio file to mix under the voice (optional)")
    parser.add_argument("--pad-volume", type=float, default=PAD_DEFAULT_DB,
                        help=f"Pad mix level in dB (default: {PAD_DEFAULT_DB})")
    args = parser.parse_args()

    print("process-audio — Framesmith audio enhancement")
    print(f"  Input  : {args.input}")
    print(f"  Output : {args.output}")

    process(args.input, args.output, args.pad, args.pad_volume)


if __name__ == "__main__":
    main()
