---
name: multi-format
description: Render a HyperFrames project to multiple platform-specific formats in one pass. Use when the user says "render for all platforms", "export for YouTube and LinkedIn", "render all formats", or after a final render is approved and needs to be distributed. Produces named output files per platform using tools/render-all.sh.
---

# Multi-Format Rendering

Renders one approved composition to all configured platforms in a single command. Outputs named files per platform so there is never ambiguity about which file goes where.

## Current platform profiles

| Platform | Dimensions | Quality | Output filename |
|---|---|---|---|
| YouTube | 1920×1080 (16:9) | high | `renders/<project>-youtube.mp4` |
| LinkedIn | 1920×1080 (16:9) | standard | `renders/<project>-linkedin.mp4` |
| TikTok | 1080×1920 (9:16) | standard | `renders/<project>-tiktok.mp4` (requires separate vertical composition) |

YouTube gets `--quality high` — upload the best source, let YouTube compress. LinkedIn gets `--quality standard` — LinkedIn recompresses regardless, no benefit to high quality.

## Usage

Run from inside the project folder, passing the platform(s) chosen in Gate 3:

```bash
# Single platform
bash ../../tools/render-all.sh --platform youtube
bash ../../tools/render-all.sh --platform linkedin

# Multiple platforms
bash ../../tools/render-all.sh --platform youtube --platform linkedin
bash ../../tools/render-all.sh --platform youtube --platform tiktok

# All platforms (no flag — fallback only, not for normal use)
bash ../../tools/render-all.sh
```

The script auto-detects the project name from the folder and renders only the requested platforms.

## Adding the vertical format (TikTok/Reels)

When a 9:16 composition exists alongside the 16:9 main composition, `render-all.sh` detects and renders it automatically. The convention:

- 16:9 root: `index.html` (always)
- 9:16 root: `index-vertical.html` (optional, author separately)

If `index-vertical.html` does not exist, the TikTok render is skipped with a note.

## Authoring a vertical composition

When vertical format is needed:

1. Copy the structure of the 16:9 composition — same sub-compositions, same timing
2. Create `index-vertical.html` with `data-width="1080"` `data-height="1920"`
3. Adjust layout: face-mode choreography, padding, font sizes for portrait
4. Lint separately: `npx hyperframes lint index-vertical.html`
5. `render-all.sh` will pick it up automatically

## After rendering

Verify all outputs before distributing:

```bash
# Check durations match
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1 \
  renders/<project>-youtube.mp4 \
  renders/<project>-linkedin.mp4
```

Durations must be within 0.1s of each other. If they differ, the compositions have diverged — fix the vertical composition before uploading.

## Platform upload specs (reference)

**YouTube**
- Container: MP4 (H.264 + AAC) ✓
- Resolution: 1920×1080 ✓
- Recommended bitrate: 8 Mbps (1080p30) — `--quality high` produces this

**LinkedIn**
- Container: MP4 (H.264 + AAC) ✓
- Resolution: up to 4096×2304 ✓
- Max file size: 5GB
- Max duration: 10 minutes
- `--quality standard` is sufficient — LinkedIn recompresses to ~2 Mbps regardless

**TikTok** (when added)
- Container: MP4 (H.264 + AAC) ✓
- Resolution: 1080×1920 ✓
- Max file size: 287.6 MB (under 1 min) / 1 GB (over 1 min)
- `--quality standard` is appropriate
