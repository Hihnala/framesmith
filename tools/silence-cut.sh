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

IN="video-projects/hihnala-channel-trailer/raw.mov"
OUT="video-projects/hihnala-channel-trailer/raw-silence-cut.mp4"
TMP="${OUT%.mp4}_tmp.mp4"

# Silences detected at -25dB:d=0.3 — 8 natural pauses, 9 keep ranges
# Original: 130.972s → output: ~126.5s (saves ~4.5s)

ffmpeg -hide_banner -y -i "$IN" -filter_complex "\
[0:v]trim=0:14.686,setpts=PTS-STARTPTS[v0];\
[0:a]atrim=0:14.686,asetpts=PTS-STARTPTS[a0];\
[0:v]trim=15.285:17.190,setpts=PTS-STARTPTS[v1];\
[0:a]atrim=15.285:17.190,asetpts=PTS-STARTPTS[a1];\
[0:v]trim=17.802:40.001,setpts=PTS-STARTPTS[v2];\
[0:a]atrim=17.802:40.001,asetpts=PTS-STARTPTS[a2];\
[0:v]trim=40.532:42.238,setpts=PTS-STARTPTS[v3];\
[0:a]atrim=40.532:42.238,asetpts=PTS-STARTPTS[a3];\
[0:v]trim=42.748:44.056,setpts=PTS-STARTPTS[v4];\
[0:a]atrim=42.748:44.056,asetpts=PTS-STARTPTS[a4];\
[0:v]trim=44.636:86.653,setpts=PTS-STARTPTS[v5];\
[0:a]atrim=44.636:86.653,asetpts=PTS-STARTPTS[a5];\
[0:v]trim=87.169:113.976,setpts=PTS-STARTPTS[v6];\
[0:a]atrim=87.169:113.976,asetpts=PTS-STARTPTS[a6];\
[0:v]trim=114.525:115.318,setpts=PTS-STARTPTS[v7];\
[0:a]atrim=114.525:115.318,asetpts=PTS-STARTPTS[a7];\
[0:v]trim=115.937:130.972,setpts=PTS-STARTPTS[v8];\
[0:a]atrim=115.937:130.972,asetpts=PTS-STARTPTS[a8];\
[v0][a0][v1][a1][v2][a2][v3][a3][v4][a4][v5][a5][v6][a6][v7][a7][v8][a8]concat=n=9:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -preset fast -crf 18 -r 30 -g 30 -keyint_min 30 \
  -force_key_frames "expr:gte(t,n_forced*1)" \
  -c:a aac -b:a 192k -movflags +faststart "$TMP"

mv "$TMP" "$OUT"
echo "Done. Output:"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "$OUT"
