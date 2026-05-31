---
name: thumbnail
description: Generate brand-consistent YouTube and LinkedIn thumbnails for a HyperFrames project. Two modes: (1) dedicated thumbnail.html composition rendered to PNG via HyperFrames, (2) frame extraction from an existing rendered video. Always build the dedicated composition first — use frame extraction only for quick reference grabs. Invoke after the script is approved and before or after the final render.
---

# Thumbnail Generator

Two modes — use both, in order:

1. **Dedicated composition** (`thumbnail.html`) — designed, brand-consistent, reusable. This is the deliverable.
2. **Frame extract** (`tools/extract-frame.sh`) — quick reference grab from a rendered video for comparison or placeholder.

---

## Mode 1: Dedicated composition

### Gate — Ask before building

1. **Hook phrase** — the main text on the thumbnail (usually the video's hook line, ≤6 words)
2. **Sub-text** (optional) — supporting line, ≤8 words
3. **Face/portrait** — is there a photo of Markku to include? (file path if yes)
4. **Accent element** — any specific visual (chart, icon, number callout)?
5. **Platform(s)** — Which platform(s) was this video made for? (Check Gate 3; only render thumbnails for those platforms.)

### Build process

Create `thumbnail.html` in the project root (`video-projects/<name>/thumbnail.html`).

**Composition spec:**
- `data-width="1280"` `data-height="720"` (YouTube native)
- `data-duration="1"` — one second is enough; we render a single frame
- Single composition, no sub-compositions needed

**Brand layout (Hihnala defaults):**

```
┌─────────────────────────────────────────────┐
│  SECTION LABEL (Copper, 11px, uppercase)    │
│                                             │
│  Hook phrase                                │
│  (Source Serif 4, 72–96px, Soft White)      │
│                                             │
│  Sub-text if present                        │
│  (Plus Jakarta Sans, 28px, Silver)          │
│                                             │
│  [Face photo top-right, gradient mask]      │
│  [Ember accent: single glow or line]        │
│                                             │
│  Logo bottom-left (small, with glow)        │
└─────────────────────────────────────────────┘
```

**Mandatory brand rules:**
- Canvas: Deep Void `#06060A`
- Heading: Source Serif 4, weight 400, Soft White `#F5F5F7`
- Sub-text: Plus Jakarta Sans, Silver `#CDCDD4`
- One Ember element only — glow behind focal text, or a single accent line
- Double-bezel card if any elevated container is present
- No gradients as backgrounds — solid `#06060A` + localized radial ember glow
- No `Math.random()` or `Date.now()`

**Portrait photo treatment (if provided):**
- Position top-right
- Left gradient mask: `linear-gradient(to right, #06060A 0%, transparent 40%)`
- Bottom gradient mask: `linear-gradient(to top, #06060A 0%, transparent 50%)`
- Do not crop the face — mask blends edges into the canvas

**GSAP timeline:**
- Keep it minimal — one short entrance animation (opacity fade, 0.3s)
- The frame we capture will be at t=0.5s so everything is fully visible

### Render to PNG

After `thumbnail.html` is built and linted:

```bash
bash ../../tools/thumbnail-render.sh --platform youtube
bash ../../tools/thumbnail-render.sh --platform linkedin
bash ../../tools/thumbnail-render.sh --platform youtube --platform linkedin
```

Pass `--platform` for each platform chosen in Gate 3. The script:
1. Renders `thumbnail.html` as a 1s MP4
2. Extracts frame at t=0.5s
3. Outputs only the PNG(s) for the requested platform(s)

Possible outputs:
- `renders/thumbnail-youtube-1280x720.png`
- `renders/thumbnail-linkedin-1200x627.png`

### Lint before rendering

```bash
npx hyperframes lint thumbnail.html
```

Fix all errors. The thumbnail is a composition — same rules apply.

---

## Mode 2: Frame extraction

For quick reference grabs from an existing render:

```bash
bash ../../tools/extract-frame.sh renders/<project>-youtube.mp4 <timestamp>
# Example: bash ../../tools/extract-frame.sh renders/myproject-youtube.mp4 12.5
```

Output: `renders/<project>-youtube-frame-12.5s.png`

Use this to:
- Find a good candidate frame before building the dedicated thumbnail
- Generate a placeholder while the dedicated composition is in progress
- Verify a specific moment in the video

**Frame extraction does not replace the dedicated composition.** The extracted frame will not have optimised text sizing, branding adjustments, or the correct thumbnail dimensions. Use it for reference only.

---

## After thumbnails are generated

Before uploading, open each thumbnail PNG that was generated (only for the chosen platform(s)) and verify:
- Text is readable at small sizes (YouTube shows thumbnails at ~168px wide in search)
- Face (if present) is not clipped by the gradient mask
- Ember accent reads clearly — not too subtle, not too dominant
- Logo is visible but not competing with the main text

If anything needs adjustment: edit `thumbnail.html`, re-run `thumbnail-render.sh --platform <platform>`

---

## Platform specs (reference)

| Platform | Native size | Min size | Notes |
|---|---|---|---|
| YouTube | 1280×720 | 640×360 | 16:9, under 2MB, JPG/PNG/GIF/BMP |
| LinkedIn | 1200×627 | 552×289 | ~1.91:1, under 5MB, JPG/PNG |
