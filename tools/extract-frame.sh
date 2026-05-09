#!/usr/bin/env bash
#
# extract-frame.sh — Extract a single frame from a rendered video at a given timestamp.
#
# USAGE (run from inside the project folder):
#   bash ../../tools/extract-frame.sh renders/<project>-youtube.mp4 12.5
#
# OUTPUT:
#   renders/<project>-youtube-frame-12.5s.png

set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: bash ../../tools/extract-frame.sh <video.mp4> <timestamp_seconds>"
  echo "Example: bash ../../tools/extract-frame.sh renders/myproject-youtube.mp4 12.5"
  exit 1
fi

VIDEO="$1"
TIME="$2"
OUT="${VIDEO%.mp4}-frame-${TIME}s.png"

ffmpeg -y -ss "$TIME" -i "$VIDEO" -frames:v 1 -q:v 1 "$OUT"
echo "Frame saved: $OUT"
