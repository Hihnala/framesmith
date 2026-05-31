#!/usr/bin/env bash
#
# render-all.sh — Render a HyperFrames project to the specified platform(s).
#
# USAGE (run from inside the project folder):
#   bash ../../tools/render-all.sh --platform youtube
#   bash ../../tools/render-all.sh --platform linkedin
#   bash ../../tools/render-all.sh --platform youtube --platform linkedin
#   bash ../../tools/render-all.sh --platform youtube --platform tiktok
#   bash ../../tools/render-all.sh   (renders all available platforms — fallback)
#
# Outputs (in renders/):
#   <project>-youtube.mp4    — 1920×1080, high quality
#   <project>-linkedin.mp4   — 1920×1080, standard quality
#   <project>-tiktok.mp4     — 1080×1920, standard quality (requires index-vertical.html)

set -euo pipefail

PROJECT=$(basename "$PWD")
mkdir -p renders

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

# No platform specified — render all available (backward-compatible fallback)
if [ ${#PLATFORMS[@]} -eq 0 ]; then
  PLATFORMS=("youtube" "linkedin")
  [ -f "index-vertical.html" ] && PLATFORMS+=("tiktok")
fi

echo "Framesmith render-all — project: $PROJECT"
echo "Platforms: ${PLATFORMS[*]}"
echo "────────────────────────────────────────"

for PLATFORM in "${PLATFORMS[@]}"; do
  case "$PLATFORM" in
    youtube)
      echo ""
      echo "▶ YouTube (high quality)..."
      npx hyperframes render \
        --quality high \
        --output "renders/${PROJECT}-youtube.mp4"
      echo "✓ YouTube: renders/${PROJECT}-youtube.mp4"
      ;;
    linkedin)
      echo ""
      echo "▶ LinkedIn (standard quality)..."
      npx hyperframes render \
        --quality standard \
        --output "renders/${PROJECT}-linkedin.mp4"
      echo "✓ LinkedIn: renders/${PROJECT}-linkedin.mp4"
      ;;
    tiktok)
      if [ -f "index-vertical.html" ]; then
        echo ""
        echo "▶ TikTok/Reels (vertical, standard quality)..."
        npx hyperframes render \
          --entry index-vertical.html \
          --quality standard \
          --output "renders/${PROJECT}-tiktok.mp4"
        echo "✓ TikTok: renders/${PROJECT}-tiktok.mp4"
      else
        echo ""
        echo "— TikTok skipped (no index-vertical.html found)"
      fi
      ;;
    *)
      echo "Unknown platform: $PLATFORM (valid: youtube, linkedin, tiktok)" >&2
      exit 1
      ;;
  esac
done

# ── Summary ────────────────────────────────────────────────────────────────────
echo ""
echo "────────────────────────────────────────"
echo "Renders complete:"
ls -lh renders/*.mp4 2>/dev/null | awk '{print "  " $5 "  " $9}'

# Duration check — only relevant when both 16:9 renders exist
YT="renders/${PROJECT}-youtube.mp4"
LI="renders/${PROJECT}-linkedin.mp4"
if [ -f "$YT" ] && [ -f "$LI" ]; then
  YT_DUR=$(ffprobe -v error -show_entries format=duration \
    -of default=noprint_wrappers=1:nokey=1 "$YT" 2>/dev/null || echo "0")
  LI_DUR=$(ffprobe -v error -show_entries format=duration \
    -of default=noprint_wrappers=1:nokey=1 "$LI" 2>/dev/null || echo "0")
  DIFF=$(echo "$YT_DUR $LI_DUR" | awk '{d=$1-$2; if(d<0)d=-d; printf "%.2f", d}')
  if (( $(echo "$DIFF > 0.1" | bc -l) )); then
    echo ""
    echo "⚠ Duration mismatch: YouTube=${YT_DUR}s LinkedIn=${LI_DUR}s (diff=${DIFF}s)"
    echo "  Check that both renders used the same composition."
  else
    echo "✓ Durations match (within 0.1s)"
  fi
fi
