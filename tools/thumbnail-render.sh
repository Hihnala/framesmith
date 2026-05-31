#!/usr/bin/env bash
#
# thumbnail-render.sh — Render thumbnail.html to PNG for the specified platform(s).
#
# USAGE (run from inside the project folder):
#   bash ../../tools/thumbnail-render.sh --platform youtube
#   bash ../../tools/thumbnail-render.sh --platform linkedin
#   bash ../../tools/thumbnail-render.sh --platform youtube --platform linkedin
#   bash ../../tools/thumbnail-render.sh   (renders both — fallback)
#
# Expects: thumbnail.html in the current directory (video-projects/<name>/)
#
# Outputs (in renders/):
#   thumbnail-youtube-1280x720.png   — YouTube native thumbnail size
#   thumbnail-linkedin-1200x627.png  — LinkedIn native thumbnail size

set -euo pipefail

PLATFORMS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    --platform)
      PLATFORMS+=("$2")
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

# No platform specified — render both (backward-compatible fallback)
if [ ${#PLATFORMS[@]} -eq 0 ]; then
  PLATFORMS=("youtube" "linkedin")
fi

if [ ! -f "thumbnail.html" ]; then
  echo "Error: thumbnail.html not found in current directory."
  echo "Build thumbnail.html first using the /thumbnail skill, then run this script."
  exit 1
fi

mkdir -p renders

echo "Rendering thumbnail.html..."

# Render as a 1-second MP4 at 1280×720 (thumbnail.html native size)
npx hyperframes render \
  --entry thumbnail.html \
  --quality high \
  --fps 30 \
  --output renders/thumbnail-raw.mp4

# Extract frame at t=0.5s as full-resolution source
echo "Extracting frame at t=0.5s..."
ffmpeg -y -ss 0.5 -i renders/thumbnail-raw.mp4 \
  -frames:v 1 -q:v 1 \
  renders/thumbnail-source.png

rm -f renders/thumbnail-raw.mp4

# Produce output for each requested platform
OUTPUTS=()

for PLATFORM in "${PLATFORMS[@]}"; do
  case "$PLATFORM" in
    youtube)
      cp renders/thumbnail-source.png renders/thumbnail-youtube-1280x720.png
      OUTPUTS+=("renders/thumbnail-youtube-1280x720.png")
      ;;
    linkedin)
      ffmpeg -y -i renders/thumbnail-source.png \
        -vf "scale=1200:627:flags=lanczos" \
        renders/thumbnail-linkedin-1200x627.png
      OUTPUTS+=("renders/thumbnail-linkedin-1200x627.png")
      ;;
    *)
      echo "Unknown platform: $PLATFORM (valid: youtube, linkedin)" >&2
      exit 1
      ;;
  esac
done

rm -f renders/thumbnail-source.png

echo ""
echo "Thumbnails ready:"
for OUTPUT in "${OUTPUTS[@]}"; do
  SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
  echo "  $SIZE  $OUTPUT"
done

echo ""
echo "Review before uploading:"
for OUTPUT in "${OUTPUTS[@]}"; do
  echo "  $OUTPUT"
done
