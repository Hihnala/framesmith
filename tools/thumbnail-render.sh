#!/usr/bin/env bash
#
# thumbnail-render.sh — Render thumbnail.html to PNG for YouTube and LinkedIn.
#
# USAGE (run from inside the project folder):
#   bash ../../tools/thumbnail-render.sh
#
# Expects: thumbnail.html in the current directory (video-projects/<name>/)
#
# OUTPUTS (in renders/):
#   thumbnail-youtube-1280x720.png   — YouTube native thumbnail size
#   thumbnail-linkedin-1200x627.png  — LinkedIn native thumbnail size

set -euo pipefail

if [ ! -f "thumbnail.html" ]; then
  echo "Error: thumbnail.html not found in current directory."
  echo "Build thumbnail.html first using the /thumbnail skill, then run this script."
  exit 1
fi

mkdir -p renders

echo "Rendering thumbnail.html..."

# Render as a 1-second MP4 (HyperFrames requires video output)
npx hyperframes render \
  --entry thumbnail.html \
  --quality high \
  --fps 30 \
  --output renders/thumbnail-raw.mp4

# Extract frame at t=0.5s (fully animated, safe from any entrance transitions)
echo "Extracting frame at t=0.5s..."
ffmpeg -y -ss 0.5 -i renders/thumbnail-raw.mp4 \
  -frames:v 1 -q:v 1 \
  renders/thumbnail-youtube-1280x720.png

# Scale to LinkedIn dimensions (1200×627)
echo "Scaling for LinkedIn..."
ffmpeg -y -i renders/thumbnail-youtube-1280x720.png \
  -vf "scale=1200:627:flags=lanczos" \
  renders/thumbnail-linkedin-1200x627.png

# Clean up raw render
rm -f renders/thumbnail-raw.mp4

echo ""
echo "Thumbnails ready:"
ls -lh renders/thumbnail-*.png | awk '{print "  " $5 "  " $9}'
echo ""
echo "Review before uploading:"
echo "  YouTube : renders/thumbnail-youtube-1280x720.png"
echo "  LinkedIn: renders/thumbnail-linkedin-1200x627.png"
