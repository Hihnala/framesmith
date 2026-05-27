#!/usr/bin/env python3
"""
tools/eye-contact.py — Eye contact correction for Framesmith talking-head videos.

Wraps the NVIDIA Maxine Eye Contact NIM preview API (grpc.nvcf.nvidia.com).
Sends cleaned footage through the API and returns a video where gaze is
redirected toward the camera.

Run this AFTER retake removal (step 3), BEFORE audio enhancement and
HyperFrames composition (steps 4–5).

Usage:
    python tools/eye-contact.py --input edited.mp4 --output eye-contact.mp4

Requirements:
    ffmpeg (already required by Framesmith)
    NVIDIA_API_KEY and NVIDIA_EYE_CONTACT_FUNCTION_ID in video-projects/.env
    Internet access (calls grpc.nvcf.nvidia.com:443)

First run: clones NVIDIA-Maxine/nim-clients into tools/nim-clients/ automatically.
"""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path

# ── nim-clients setup ──────────────────────────────────────────────────────────
NIM_CLIENTS_DIR  = Path(__file__).parent / "nim-clients"
NIM_CLIENTS_REPO = "https://github.com/NVIDIA-Maxine/nim-clients.git"
EYE_CONTACT_DIR  = NIM_CLIENTS_DIR / "eye-contact"
EYE_CONTACT_SCRIPT = EYE_CONTACT_DIR / "scripts" / "eye-contact.py"

# ── API endpoint ───────────────────────────────────────────────────────────────
NVCF_TARGET = "grpc.nvcf.nvidia.com:443"

# ── Video encoding defaults ────────────────────────────────────────────────────
TARGET_FPS  = 30      # Eye Contact NIM does not support VFR — convert to CFR
VIDEO_CODEC = "libx264"
OUTPUT_BITRATE = 20_000_000  # 20 Mbps — NIM default, good for 1080p


def run(cmd, check=True, capture=False):
    flat = [str(c) for c in cmd]
    print("  $", " ".join(flat))
    return subprocess.run(
        flat,
        capture_output=capture,
        text=True,
        check=check
    )


def load_env():
    """Load .env from video-projects/.env (Framesmith convention)."""
    env_path = Path(__file__).parent.parent / "video-projects" / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def get_required_env(key):
    value = os.environ.get(key)
    if not value:
        print(f"\nERROR: {key} is not set.")
        print(f"  Add it to video-projects/.env:")
        print(f"  {key}=your_value_here")
        if key == "NVIDIA_EYE_CONTACT_FUNCTION_ID":
            print("  Find the function ID at: https://build.nvidia.com/nvidia/eyecontact/api")
        sys.exit(1)
    return value


def ensure_nim_clients():
    """Clone NVIDIA-Maxine/nim-clients on first run if not already present."""
    if EYE_CONTACT_SCRIPT.exists():
        return

    print("\n[setup] nim-clients not found — cloning NVIDIA-Maxine/nim-clients...")
    if not NIM_CLIENTS_DIR.exists():
        run(["git", "clone", "--depth", "1", NIM_CLIENTS_REPO, str(NIM_CLIENTS_DIR)])
    else:
        print(f"  nim-clients directory exists but eye-contact script is missing.")
        print(f"  Expected: {EYE_CONTACT_SCRIPT}")
        sys.exit(1)

    if not EYE_CONTACT_SCRIPT.exists():
        print(f"ERROR: Expected script not found after clone: {EYE_CONTACT_SCRIPT}")
        sys.exit(1)
    print("  Clone complete.")


def install_nim_requirements():
    """Install nim-clients requirements if not already installed."""
    req_file = EYE_CONTACT_DIR / "requirements.txt"
    if not req_file.exists():
        return
    print("\n[setup] Installing nim-clients requirements...")
    run([sys.executable, "-m", "pip", "install", "-q", "-r", str(req_file)])


def is_vfr(input_path: Path) -> bool:
    """Return True if the video uses Variable Frame Rate."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=r_frame_rate,avg_frame_rate",
            "-of", "default=noprint_wrappers=1",
            str(input_path)
        ],
        capture_output=True, text=True, check=False
    )
    lines = {
        k: v for line in result.stdout.splitlines()
        if "=" in line for k, v in [line.split("=", 1)]
    }
    r_fps   = lines.get("r_frame_rate", "0/1")
    avg_fps = lines.get("avg_frame_rate", "0/1")
    # VFR: r_frame_rate (container-reported max) differs from avg_frame_rate
    return r_fps != avg_fps


def prepare_input(input_path: Path, tmp_dir: str) -> Path:
    """
    Convert to CFR H.264 with faststart (required by Eye Contact NIM).
    Returns path to the prepared file (may be the original if already valid).
    """
    prepared = Path(tmp_dir) / "ec_prepared.mp4"
    print(f"\n[1/?] Preparing input for Eye Contact NIM...")
    print(f"  Converting to CFR {TARGET_FPS}fps + H.264 + faststart...")

    # Single ffmpeg pass: CFR + H.264 + faststart + copy audio
    run([
        "ffmpeg", "-hide_banner", "-y",
        "-i",         str(input_path),
        "-vf",        f"fps={TARGET_FPS}",
        "-c:v",       VIDEO_CODEC,
        "-preset",    "fast",
        "-movflags",  "+faststart",
        "-c:a",       "copy",
        str(prepared)
    ])
    print(f"  Prepared: {prepared}")
    return prepared


def run_eye_contact(prepared: Path, output_path: Path, api_key: str, function_id: str):
    """Send the prepared video to the NVIDIA Eye Contact NIM preview API."""
    print(f"\n[2/?] Sending to NVIDIA Eye Contact NIM...")
    print(f"  Endpoint  : {NVCF_TARGET}")
    print(f"  Mode      : streaming (preferred for streamable MP4)")
    print(f"  Input     : {prepared}")
    print(f"  Output    : {output_path}")

    run([
        sys.executable, str(EYE_CONTACT_SCRIPT),
        "--preview-mode",
        "--target",      NVCF_TARGET,
        "--api-key",     api_key,
        "--function-id", function_id,
        "--input",       str(prepared),
        "--output",      str(output_path),
        "--streaming",                        # preferred for faststart MP4
        "--bitrate",     str(OUTPUT_BITRATE),
        "--detect-closure", "1",              # handle blinks naturally
        "--enable-lookaway", "0",             # keep gaze fixed on camera
    ])


def verify_output(output_path: Path):
    if not output_path.exists() or output_path.stat().st_size == 0:
        print(f"\nERROR: Output file missing or empty: {output_path}")
        print("  Check the API response above for error details.")
        sys.exit(1)
    size_mb = output_path.stat().st_size / 1_048_576
    print(f"\n[done] Eye contact correction complete.")
    print(f"  Output : {output_path}")
    print(f"  Size   : {size_mb:.1f} MB")


def process(input_path: str, output_path: str, skip_prepare: bool = False):
    inp = Path(input_path)
    out = Path(output_path)

    if not inp.exists():
        print(f"ERROR: Input file not found: {inp}")
        sys.exit(1)

    load_env()
    api_key     = get_required_env("NVIDIA_API_KEY")
    function_id = get_required_env("NVIDIA_EYE_CONTACT_FUNCTION_ID")

    ensure_nim_clients()
    install_nim_requirements()

    with tempfile.TemporaryDirectory(prefix="framesmith-ec-") as tmp_dir:
        if skip_prepare:
            prepared = inp
            print(f"\n[1/?] Skipping preparation (--skip-prepare set).")
        else:
            prepared = prepare_input(inp, tmp_dir)

        run_eye_contact(prepared, out, api_key, function_id)

    verify_output(out)


def main():
    parser = argparse.ArgumentParser(
        description="Eye contact correction for Framesmith talking-head videos.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Pipeline position:
  Step 3   tools/cut-retakes.py       → retakes-removed.mp4
  Step 3.5 tools/eye-contact.py       → eye-contact.mp4       ← this tool
  Step 4   tools/process-audio.py     → audio-processed.mp4
  Step 5   HyperFrames composition

What the tool does:
  1. Converts input to CFR 30fps H.264 + faststart (required by the NIM)
  2. Sends the prepared video to the NVIDIA Eye Contact NIM preview API
  3. Returns a video with gaze redirected toward the camera

Required .env entries (in video-projects/.env):
  NVIDIA_API_KEY=nvapi-...
  NVIDIA_EYE_CONTACT_FUNCTION_ID=...   (find at build.nvidia.com/nvidia/eyecontact/api)

First run:
  Clones NVIDIA-Maxine/nim-clients into tools/nim-clients/ automatically.
  Installs its Python requirements.

Examples:
  python tools/eye-contact.py --input retakes-removed.mp4 --output eye-contact.mp4
  python tools/eye-contact.py --input retakes-removed.mp4 --output eye-contact.mp4 --skip-prepare
        """
    )
    parser.add_argument("--input",        required=True,
                        help="Input video file (post-retake-removal)")
    parser.add_argument("--output",       required=True,
                        help="Output video file with corrected eye contact")
    parser.add_argument("--skip-prepare", action="store_true",
                        help="Skip CFR/H.264/faststart conversion (use if already prepared)")
    args = parser.parse_args()

    print("eye-contact — Framesmith eye contact correction")
    print(f"  Input  : {args.input}")
    print(f"  Output : {args.output}")

    process(args.input, args.output, args.skip_prepare)


if __name__ == "__main__":
    main()
