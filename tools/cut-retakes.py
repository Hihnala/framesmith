"""
cut-retakes.py — Apply last-take-rule to remove duplicate takes from raw recordings.

Usage:
    1. Set IN and OUT paths below
    2. Review the transcript (from transcribe-whisper.py) and identify keep ranges
    3. Fill in the KEEPS list with (start, end) tuples in seconds
    4. Run: python tools/cut-retakes.py

The last-take-rule: when a sentence was recorded multiple times,
keep only the last take. Fill KEEPS with the ranges of the takes you want to keep.

Requirements: ffmpeg must be on PATH
"""

import subprocess
import sys
from pathlib import Path

# ── CONFIGURE THESE ────────────────────────────────────────────────────────────

IN  = Path("video-projects/<your-project>/raw-silence-cut.mp4")
OUT = Path("video-projects/<your-project>/edit.mp4")

# Keep ranges (start, end) in seconds. Last-take rule — only the final good take
# per spoken section. Review transcript first, then fill in ranges.
KEEPS = [
    # (0.0, 14.36),   # Clip 1: "first sentence"
    # (14.65, 17.64), # Clip 2: "second sentence"
]

# ── DO NOT EDIT BELOW ──────────────────────────────────────────────────────────

def main():
    if not KEEPS:
        sys.exit("ERROR: KEEPS is empty. Fill in keep ranges from the transcript first.")

    parts = []
    for i, (s, e) in enumerate(KEEPS):
        s = max(0, s)
        parts.append(f"[0:v]trim={s}:{e},setpts=PTS-STARTPTS[v{i}]")
        parts.append(f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS[a{i}]")

    concat_inputs = "".join(f"[v{i}][a{i}]" for i in range(len(KEEPS)))
    concat = f"{concat_inputs}concat=n={len(KEEPS)}:v=1:a=1[v][a]"
    filter_complex = ";".join(parts) + ";" + concat

    cmd = [
        "ffmpeg", "-hide_banner", "-y", "-i", str(IN),
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-r", "30", "-g", "30", "-keyint_min", "30",
        "-force_key_frames", "expr:gte(t,n_forced*1)",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
        str(OUT),
    ]

    total = sum(e - s for s, e in KEEPS)
    print(f"Cutting {len(KEEPS)} clips. Estimated final duration: {total:.2f}s", flush=True)

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("FFMPEG STDERR:", result.stderr[-2000:], file=sys.stderr)
        sys.exit(result.returncode)

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(OUT)],
        capture_output=True, text=True,
    )
    print(f"OUT duration: {probe.stdout.strip()}s → {OUT}", flush=True)

if __name__ == "__main__":
    main()
