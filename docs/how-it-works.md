# How It Works

Framesmith wraps [HyperFrames](https://hyperframes.heygen.com) with a production system: a gate that asks before building, a three-level workflow that covers every video type, and a loop that takes you from idea to delivered MP4 without skipping steps.

---

## The gate system

Every session starts with three gates. The agent asks these questions before writing a single line of HTML or running any command.

### Gate 1 — Workflow level

Which of the three levels fits the request?

| Level | Use when | What happens |
| --- | --- | --- |
| **1 — Website-to-Video** | You have a URL and want a short video from it | Agent captures the page, adapts it as a HyperFrames composition |
| **2 — Motion graphic** | You want an original promo, explainer, or social video | Agent scripts, storyboards, and builds from scratch |
| **3 — Guided video** | You have raw footage, a recording, or screen capture | Full pipeline: silence-cut → transcribe → retake-cut → composition |

If unclear, the agent asks: *"Do you have existing footage, or are we building a motion graphic from scratch?"*

### Gate 2 — Brand

Before writing any HTML, the agent reads DESIGN.md and confirms that the brand is loaded. If you are using a custom brand and `DESIGN.md` has not been updated yet, the agent will stop and prompt you to update it — it will not fall back to generic colors or fonts.

This gate exists because a brand error discovered after rendering costs far more to fix than one caught before the first line of HTML.

### Gate 3 — Project details

- Project name (becomes the folder: `video-projects/<name>/`)
- Target duration and aspect ratio
- Delivery platform
- Assets on hand

When all three gates are closed, the agent summarises the plan and waits for confirmation before taking any action.

---

## Three workflow levels

### Level 1 — Website-to-Video

Converts an existing animated webpage into a short MP4 (typically 6–15 seconds). Useful for capturing a product demo, brand animation, or interactive component as a social asset.

**Skill:** `website-to-hyperframes` / `/website-to-hyperframes`

**Flow:**

```
URL provided
  → agent captures page (Playwright screenshot + DOM analysis)
  → extracts design tokens (colors, fonts, layout)
  → adapts as HyperFrames composition with timing and animation
  → lint → Studio preview → draft render → final render
```

The composition matches the source page's visual style. If you want Hihnala brand applied instead, tell the agent before it builds.

---

### Level 2 — Motion Graphic

Building an original video from a concept, script, or brief. Covers both 16:9 (YouTube, LinkedIn) and 9:16 (Reels, Shorts, TikTok). This is the most common level.

**Recommended skill flow:**

```
/script        → SCRIPT.md with scene breakdown
/hyperframes   → composition authoring
/hyperframes-cli → lint, preview, render
/multi-format  → YouTube + LinkedIn renders
/thumbnail     → brand-consistent thumbnails
/delivery      → pre-publish checklist
/journal       → production record
```

**The two mandatory preview gates:**

No final render without both of these:

1. **Live Studio preview** (`npx hyperframes preview`, localhost:3002) — review the composition live before any render. Catches layout, timing, and visual issues cheaply.
2. **Draft render review** — render at draft quality, scrub the full video, verify captions and beats. Only then run the final standard or high quality render.

Skipping a preview gate turns render cycles into guesswork.

---

### Level 3 — Guided Video

Full production pipeline for camera recordings, screen recordings, or talking-head footage. The raw video is edited first, then overlaid with HyperFrames motion graphics and captions.

**Skill:** `video-pipeline` / `/video-pipeline`

**Full pipeline:**

```
raw.mp4
  ├── Step 1: Silence cut
  │     bash tools/silence-cut.sh
  │     → raw-silence-cut.mp4
  │
  ├── Step 2: Transcription (choose one)
  │     python tools/transcribe-whisper.py raw-silence-cut.mp4  (local, English)
  │     npx hyperframes transcribe raw-silence-cut.mp4 --json   (ElevenLabs Scribe)
  │     → .transcript.json + .transcript.txt
  │
  ├── Step 3: Retake cut
  │     python tools/cut-retakes.py  (edit KEEPS list from transcript first)
  │     → edit.mp4  ← source of truth for composition timing
  │
  ├── Step 4: Storyboard motion overlays
  │     Plan scenes against edited-video timestamps
  │     Read DESIGN.md + MOTION_PHILOSOPHY.md before designing
  │
  ├── Step 5: HyperFrames composition
  │     Build index.html + sub-compositions
  │     All timestamps in edited-video time — never original recording time
  │
  └── Step 6: Lint → Studio preview → Draft render → Final render
              bash ../../tools/render-all.sh
```

**Critical rule:** all composition timestamps use edited-video time. If `edit.mp4` is 47 seconds long, every `data-start` and `data-duration` value in your composition references that 47-second timeline. Never mix original-recording time with edited-video time in the same composition.

---

## The production loop

A complete video moves through these stages in order:

```
Idea
  ↓
Gate (level → brand → project)
  ↓
Script (SCRIPT.md — approved before build)
  ↓
Build (compositions, lint, Studio preview)
  ↓
Draft render + review
  ↓
Thumbnails (thumbnail.html → YouTube + LinkedIn PNGs)
  ↓
Final render (render-all.sh → YouTube + LinkedIn MP4s)
  ↓
Delivery check (DELIVERY.md signed off)
  ↓
Upload
  ↓
Journal (JOURNAL.md + PRODUCTION_LOG.md updated)
```

No stage is optional. A skipped script means the composition has no timing anchor. A skipped delivery check means the upload might have a brand error, wrong font, or missing thumbnail. A skipped journal entry means the next session starts cold.

---

## Series vs standalone videos

**Standalone** — a one-off video with no recurring format. The agent applies `DESIGN.md` brand and the production loop above.

**Series** — a recurring format (weekly educational, LinkedIn thought leadership, product demos) defined in `video-projects/series.json`. Series specs define:

- Shared intro and outro compositions (stored in `video-projects/shared/`)
- Lower-third position, name, and title
- Caption style
- CTA line (verbatim, applied to every episode)
- Title format (`EP01: Title`, etc.)
- Episode registry (every episode tracked with date and published URLs)

When starting a new series episode, the agent loads the series spec, applies it to the new project, and runs a series consistency check before the delivery gate.

See [Skills — Series](skills.md#series) for the full guide.

---

## How compositions are structured

This is documented fully in the [HyperFrames docs](https://hyperframes.heygen.com/introduction). The short version relevant to Framesmith:

Every composition is a plain HTML file with `data-*` timing attributes. Clips are `<div>` elements with `class="clip"`, `data-start`, `data-duration`, and `data-track-index`. Animation is GSAP, registered on `window.__timelines`. Everything is deterministic — no `Math.random()`, no `Date.now()`, no network fetches at render time.

The root composition (`index.html`) holds sub-compositions via `data-composition-src`. For a typical talking-head video this might be:

```
index.html
├── ambient-bg.html      track 3  — brand background, grain, vignette
├── face-video.html      track 0  — edit.mp4 talking head
├── scene1-hook.html     track 1  — motion overlay, scene 1
├── scene2-problem.html  track 1  — motion overlay, scene 2
└── captions.html        track 2  — word-synced captions
```

For a pure motion graphic (no footage), the face layer is replaced by additional content scenes.
