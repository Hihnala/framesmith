#!/usr/bin/env bash
#
# silence-cut.sh — Remove silences from a recording using ffmpeg silencedetect.
#
# USAGE:
#   1. Set IN and OUT below
#   2. Detect silences first (run this, don't encode):
#      ffmpeg -i "$IN" -af "silencedetect=noise=-32dB:d=0.25" -f null - 2>&1 | grep silence
#   3. From the output, identify keep ranges (non-silent segments with 0.1s pad on each end)
#   4. Update the filter_complex section below with your keep ranges
#   5. Run: bash tools/silence-cut.sh
#
# Tunable knobs:
#   - silencedetect threshold: -32dB is a good default, -30dB more aggressive
#   - duration filter: 0.25s removes silences ≥ 0.25s; lower = stricter
#   - keep-pad: 0.1s of silence at each cut for natural pacing
#   - target fps: -r 30 (match your composition)
#   - CRF: 18 = high quality, 23 = good

set -euo pipefail

IN="video-projects/<your-project>/raw.mp4"
OUT="video-projects/<your-project>/raw-silence-cut.mp4"
TMP="${OUT%.mp4}_tmp.mp4"

# CUSTOMIZE: replace with keep ranges from silencedetect output.
# Example: if silencedetect reports silence from 14.36→14.65 and 17.64→17.82,
# your keep ranges are: (0, 14.36+0.1), (14.65-0.1, 17.64+0.1), (17.82-0.1, end)
# → use: trim=0:14.46  trim=14.55:17.74  trim=17.72:end

ffmpeg -hide_banner -y -i "$IN" -filter_complex "\
[0:v]trim=0:14.36,setpts=PTS-STARTPTS[v0];\
[0:a]atrim=0:14.36,asetpts=PTS-STARTPTS[a0];\
[0:v]trim=14.65:17.64,setpts=PTS-STARTPTS[v1];\
[0:a]atrim=14.65:17.64,asetpts=PTS-STARTPTS[a1];\
[0:v]trim=17.82:21.32,setpts=PTS-STARTPTS[v2];\
[0:a]atrim=17.82:21.32,asetpts=PTS-STARTPTS[a2];\
[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -preset fast -crf 18 -r 30 -g 30 -keyint_min 30 \
  -force_key_frames "expr:gte(t,n_forced*1)" \
  -c:a aac -b:a 192k -movflags +faststart "$TMP"

mv "$TMP" "$OUT"
echo "Done. Output:"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "$OUT"
