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

IN  = Path("video-projects/week-1/raw-silence-cut.mp4")
OUT = Path("video-projects/week-1/retakes-removed.mp4")

# Keep ranges (start, end) in seconds. Last-take rule — only the final good take.
# Source: raw-silence-cut.transcript.txt  |  ~5m 33s final edit
KEEPS = [
    # ── Opening + Core Problem ────────────────────────────────────────────────
    (0.00, 41.22),    # "Most AI projects don't fail..." → "...a consultant is brought in."
    (46.14, 68.86),   # retry: "Then something in the middle of that work." → "...moves on to something else."
                      #   cut: 41.84–45.78 (fumble: "Work begins then something in the middle of the work of that")
    # ── Transition + Mistake 1 ────────────────────────────────────────────────
    (78.50, 104.92),  # "This pattern almost always traces back..." → "Do they require account access?"
                      #   cut: 69.76–77.xx (explicit "cuts." then restarted)
    (109.44, 122.12), # clean take: "Are they complaints that require human response?..." → "...handles the work well."
                      #   cut: 105.50–108.96 ("that the require human? Cut.")
    (128.68, 142.60), # clean take: "And an AI system that handles customer inquiries badly..." → "Define the problem first"
                      #   cut: 122.68–127.86 ("customer inquiries bad cut.")
    (146.96, 162.62), # clean take: "Not we want to save time on customer service..." → "...not ready to build anything yet."
                      #   cut: 142.94–146.70 (fumble: "Not we want to find the problem first in specific terms.")
    # ── Mistake 2 ─────────────────────────────────────────────────────────────
    (162.62, 222.20), # "The AI doesn't fix program processes..." → "You can't automate that."
    (234.18, 253.42), # clean take: "The work before automation is to standardize..." → "...you're not right."
                      #   cut: 222.98–233.84 ("handle it, cut." + repeated "You can't automate that.")
    # ── Mistake 3 ─────────────────────────────────────────────────────────────
    (259.40, 290.08), # "A system gets built, it works..." → "Eventually someone notices the outputs are wrong."
                      #   cut: 253.44–258.94 (fumbled intro: "One kills more process than...")
    (296.54, 315.80), # clean take: "By that point, months of bad data or bad customer interactions..."
                      #             → "Every AI system needs an owner...someone who understands what it's doing."
                      #   cut: 290.76–295.46 ("months of bad data and cut.")
    (322.18, 325.16), # "and what needs to change when the business changes."
                      #   cut: 316.24–322.17 (repeated "not necessarily a technical person...what it's doing")
    (333.12, 351.60), # "If you can't name the person..." → "...were already failing before"
                      #   cut: 325.76–332.82 (fumble: "Someone who cuts someone who can tell..." — no clean retake, skipped)
    # ── Why This Matters + Close ──────────────────────────────────────────────
    (357.20, 362.62), # clean take: "...were already failing before implementation started."
                      #   cut: 351.60–356.94 (speech error: "before implemented")
    (363.04, 407.78), # "The money spent on the technology wasn't a loss." → "That's where you start."
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
