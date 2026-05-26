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

IN="video-projects/channel-trailer/raw.mov"
OUT="video-projects/channel-trailer/raw-silence-cut.mp4"
TMP="${OUT%.mp4}_tmp.mp4"

# Silences detected at -32dB:d=0.25 — 22 silences, 20 keep ranges
# Original: 60.1s → output: ~46.3s (saves ~13.8s — pre-roll, inter-sentence gaps, 3.4s tail)

ffmpeg -hide_banner -y -i "$IN" -filter_complex "\
[0:v]trim=2.707:6.812,setpts=PTS-STARTPTS[v0];\
[0:a]atrim=2.707:6.812,asetpts=PTS-STARTPTS[a0];\
[0:v]trim=7.155:10.768,setpts=PTS-STARTPTS[v1];\
[0:a]atrim=7.155:10.768,asetpts=PTS-STARTPTS[a1];\
[0:v]trim=11.034:13.616,setpts=PTS-STARTPTS[v2];\
[0:a]atrim=11.034:13.616,asetpts=PTS-STARTPTS[a2];\
[0:v]trim=14.042:15.185,setpts=PTS-STARTPTS[v3];\
[0:a]atrim=14.042:15.185,asetpts=PTS-STARTPTS[a3];\
[0:v]trim=15.568:19.572,setpts=PTS-STARTPTS[v4];\
[0:a]atrim=15.568:19.572,asetpts=PTS-STARTPTS[a4];\
[0:v]trim=19.902:20.809,setpts=PTS-STARTPTS[v5];\
[0:a]atrim=19.902:20.809,asetpts=PTS-STARTPTS[a5];\
[0:v]trim=21.199:22.837,setpts=PTS-STARTPTS[v6];\
[0:a]atrim=21.199:22.837,asetpts=PTS-STARTPTS[a6];\
[0:v]trim=23.091:24.136,setpts=PTS-STARTPTS[v7];\
[0:a]atrim=23.091:24.136,asetpts=PTS-STARTPTS[a7];\
[0:v]trim=24.870:27.267,setpts=PTS-STARTPTS[v8];\
[0:a]atrim=24.870:27.267,asetpts=PTS-STARTPTS[a8];\
[0:v]trim=27.659:28.994,setpts=PTS-STARTPTS[v9];\
[0:a]atrim=27.659:28.994,asetpts=PTS-STARTPTS[a9];\
[0:v]trim=29.120:32.486,setpts=PTS-STARTPTS[v10];\
[0:a]atrim=29.120:32.486,asetpts=PTS-STARTPTS[a10];\
[0:v]trim=33.088:36.342,setpts=PTS-STARTPTS[v11];\
[0:a]atrim=33.088:36.342,asetpts=PTS-STARTPTS[a11];\
[0:v]trim=36.647:37.988,setpts=PTS-STARTPTS[v12];\
[0:a]atrim=36.647:37.988,asetpts=PTS-STARTPTS[a12];\
[0:v]trim=38.455:40.450,setpts=PTS-STARTPTS[v13];\
[0:a]atrim=38.455:40.450,asetpts=PTS-STARTPTS[a13];\
[0:v]trim=40.750:42.948,setpts=PTS-STARTPTS[v14];\
[0:a]atrim=40.750:42.948,asetpts=PTS-STARTPTS[a14];\
[0:v]trim=43.254:46.281,setpts=PTS-STARTPTS[v15];\
[0:a]atrim=43.254:46.281,asetpts=PTS-STARTPTS[a15];\
[0:v]trim=46.390:47.844,setpts=PTS-STARTPTS[v16];\
[0:a]atrim=46.390:47.844,asetpts=PTS-STARTPTS[a16];\
[0:v]trim=48.367:49.929,setpts=PTS-STARTPTS[v17];\
[0:a]atrim=48.367:49.929,asetpts=PTS-STARTPTS[a17];\
[0:v]trim=50.468:53.682,setpts=PTS-STARTPTS[v18];\
[0:a]atrim=50.468:53.682,asetpts=PTS-STARTPTS[a18];\
[0:v]trim=53.871:55.976,setpts=PTS-STARTPTS[v19];\
[0:a]atrim=53.871:55.976,asetpts=PTS-STARTPTS[a19];\
[v0][a0][v1][a1][v2][a2][v3][a3][v4][a4][v5][a5][v6][a6][v7][a7][v8][a8][v9][a9][v10][a10][v11][a11][v12][a12][v13][a13][v14][a14][v15][a15][v16][a16][v17][a17][v18][a18][v19][a19]concat=n=20:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" \
  -c:v libx264 -preset fast -crf 18 -r 30 -g 30 -keyint_min 30 \
  -force_key_frames "expr:gte(t,n_forced*1)" \
  -c:a aac -b:a 192k -movflags +faststart "$TMP"

mv "$TMP" "$OUT"
echo "Done. Output:"
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "$OUT"
