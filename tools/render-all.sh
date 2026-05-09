#!/usr/bin/env bash
#
# render-all.sh — Render a HyperFrames project to all configured platform formats.
#
# USAGE: Run from inside the project folder:
#   bash ../../tools/render-all.sh
#
# Outputs (in renders/):
#   <project>-youtube.mp4    — 1920×1080, high quality
#   <project>-linkedin.mp4   — 1920×1080, standard quality
#   <project>-tiktok.mp4     — 1080×1920, standard quality (only if index-vertical.html exists)

set -euo pipefail

PROJECT=$(basename "$PWD")
mkdir -p renders

echo "Framesmith render-all — project: $PROJECT"
echo "────────────────────────────────────────"

# ── YouTube — high quality (upload best source, let YouTube compress) ──────────
echo ""
echo "▶ YouTube (high quality)..."
npx hyperframes render \
  --quality high \
  --output "renders/${PROJECT}-youtube.mp4"
echo "✓ YouTube: renders/${PROJECT}-youtube.mp4"

# ── LinkedIn — standard quality (platform recompresses regardless) ─────────────
echo ""
echo "▶ LinkedIn (standard quality)..."
npx hyperframes render \
  --quality standard \
  --output "renders/${PROJECT}-linkedin.mp4"
echo "✓ LinkedIn: renders/${PROJECT}-linkedin.mp4"

# ── TikTok/Reels — vertical composition (only if index-vertical.html exists) ───
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

# ── Summary ────────────────────────────────────────────────────────────────────
echo ""
echo "────────────────────────────────────────"
echo "Renders complete:"
ls -lh renders/*.mp4 2>/dev/null | awk '{print "  " $5 "  " $9}'

# Verify durations match (warn if they diverge by more than 0.1s)
YT_DUR=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "renders/${PROJECT}-youtube.mp4" 2>/dev/null || echo "0")
LI_DUR=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "renders/${PROJECT}-linkedin.mp4" 2>/dev/null || echo "0")

DIFF=$(echo "$YT_DUR $LI_DUR" | awk '{d=$1-$2; if(d<0)d=-d; printf "%.2f", d}')
if (( $(echo "$DIFF > 0.1" | bc -l) )); then
  echo ""
  echo "⚠ Duration mismatch: YouTube=${YT_DUR}s LinkedIn=${LI_DUR}s (diff=${DIFF}s)"
  echo "  Check that both renders used the same composition."
else
  echo "✓ Durations match (within 0.1s)"
fi
