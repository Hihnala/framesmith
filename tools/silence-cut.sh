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

IN="/Users/markku/Documents/Hihnala/YouTube/Raw videos/A001_05280944_C006.mov"
OUT="video-projects/week-1/raw-silence-cut.mp4"
TMP="${OUT%.mp4}_tmp.mp4"

# week-1 — A001_05280944_C006.mov
# Silences detected at -32dB:d=0.25
# 10 major gaps cut (6–8s each: pre-roll, section breaks, retake pauses, end tail)
# Original: 494.8s (8.25 min) → output: ~407.8s (6.8 min) — saves ~87s

ffmpeg -hide_banner -y -i "$IN" -filter_complex "\
[0:v]trim=4.298:24.628,setpts=PTS-STARTPTS[v0];\
[0:a]atrim=4.298:24.628,asetpts=PTS-STARTPTS[a0];\
[0:v]trim=31.710:95.587,setpts=PTS-STARTPTS[v1];\
[0:a]atrim=31.710:95.587,asetpts=PTS-STARTPTS[a1];\
[0:v]trim=103.831:164.166,setpts=PTS-STARTPTS[v2];\
[0:a]atrim=103.831:164.166,asetpts=PTS-STARTPTS[a2];\
[0:v]trim=172.486:190.565,setpts=PTS-STARTPTS[v3];\
[0:a]atrim=172.486:190.565,asetpts=PTS-STARTPTS[a3];\
[0:v]trim=197.751:288.559,setpts=PTS-STARTPTS[v4];\
[0:a]atrim=197.751:288.559,asetpts=PTS-STARTPTS[a4];\
[0:v]trim=296.563:359.669,setpts=PTS-STARTPTS[v5];\
[0:a]atrim=296.563:359.669,asetpts=PTS-STARTPTS[a5];\
[0:v]trim=366.253:387.433,setpts=PTS-STARTPTS[v6];\
[0:a]atrim=366.253:387.433,asetpts=PTS-STARTPTS[a6];\
[0:v]trim=395.348:414.828,setpts=PTS-STARTPTS[v7];\
[0:a]atrim=395.348:414.828,asetpts=PTS-STARTPTS[a7];\
[0:v]trim=420.531:448.056,setpts=PTS-STARTPTS[v8];\
[0:a]atrim=420.531:448.056,asetpts=PTS-STARTPTS[a8];\
[0:v]trim=456.908:471.828,setpts=PTS-STARTPTS[v9];\
[0:a]atrim=456.908:471.828,asetpts=PTS-STARTPTS[a9];\
[0:v]trim=476.809:481.778,setpts=PTS-STARTPTS[v10];\
[0:a]atrim=476.809:481.778,asetpts=PTS-STARTPTS[a10];\
[0:v]trim=486.848:490.028,setpts=PTS-STARTPTS[v11];\
[0:a]atrim=486.848:490.028,asetpts=PTS-STARTPTS[a11];\
[v0][a0][v1][a1][v2][a2][v3][a3][v4][a4][v5][a5][v6][a6][v7][a7][v8][a8][v9][a9][v10][a10][v11][a11]concat=n=12:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -preset fast -crf 18 -r 30 -g 30 -keyint_min 30 \
  -force_key_frames "expr:gte(t,n_forced*1)" \
  -c:a aac -b:a 192k -movflags +faststart "$TMP"

mv "$TMP" "$OUT"
echo "Done. Output:"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "$OUT"
