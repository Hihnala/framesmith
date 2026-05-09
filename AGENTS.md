# Framesmith — AI Agent Guide

HTML-native video production studio built on [HyperFrames](https://hyperframes.heygen.com). Works with Claude Code, Cursor, Gemini CLI, GitHub Copilot, or any AI coding agent.

---

## Skills

Install the HyperFrames skills before writing any compositions. They encode framework-specific patterns (`window.__timelines` registration, `data-*` attribute semantics, shader-compatible CSS) that are not in generic web docs — skipping them produces broken compositions.

```bash
npx skills add heygen-com/hyperframes
```

Framesmith-specific skills are already in `.claude/skills/` and load automatically in Claude Code. For other agents, the key patterns are documented in this file.

| Skill | What it covers |
|---|---|
| `framesmith` | Gate system — establish level, brand, and project before any work |
| `script` | Write video scripts in Hihnala brand voice, mapped to HyperFrames scene timing |
| `journal` | Update project journal (JOURNAL.md) and workspace production log |
| `delivery` | Pre-publish gate — structured checklist producing signed-off DELIVERY.md |
| `series` | Manage series specs, start episodes, check consistency, track episode history |
| `hyperframes` | Composition authoring, captions, TTS, audio-reactive animation, transitions |
| `hyperframes-cli` | All CLI commands: lint, preview, render, transcribe, tts, doctor |
| `gsap` | Animation: timelines, easing, stagger, performance |
| `hyperframes-registry` | Install catalog blocks via `npx hyperframes add` |
| `make-a-video` | End-to-end guided flow for new videos |
| `short-form-video` | 9:16 vertical social video playbook |
| `website-to-hyperframes` | URL → composition (7-step pipeline) |
| `video-pipeline` | Level 3 raw footage pipeline with ElevenLabs Scribe |
| `multi-format` | Render to YouTube + LinkedIn + TikTok from one project |
| `thumbnail` | Generate brand-consistent YouTube + LinkedIn thumbnails |
| `21st-dev` | Import and adapt components from 21st.dev |

---

## Gate — Ask before building

Before writing any HTML or running any command, establish:

1. **Which workflow level?**
   - Level 1 — convert an existing webpage to video
   - Level 2 — build a motion graphic from scratch
   - Level 3 — edit raw footage and add motion overlays

2. **Brand confirmed?** Read `DESIGN.md` before writing any composition. Do not use default colors (#333, #3b82f6, Roboto).

3. **Project name?** Every project lives in `video-projects/<name>/`. Never put composition files at the workspace root.

---

## Commands

Run all CLI commands from inside the project folder (`video-projects/<name>/`), not the workspace root.

```bash
# Preview and render
npx hyperframes preview                                          # Studio at localhost:3002 (hot reload)
npx hyperframes lint                                             # validate compositions — fix all errors before rendering
npx hyperframes render --quality draft --output renders/draft.mp4
npx hyperframes render --quality standard --output renders/final.mp4

# Catalog
npx hyperframes catalog --type block
npx hyperframes add <name>

# Media
npx hyperframes transcribe <file> --model small.en --json       # word-level transcript
npx hyperframes tts "text" --voice af_nova --output narration.wav

# Diagnostics
npx hyperframes doctor
npx hyperframes docs <topic>    # topics: data-attributes, gsap, rendering, compositions, troubleshooting
```

```bash
# Python video pipeline tools (run from workspace root)
python tools/transcribe-whisper.py video-projects/<name>/raw.mp4
python tools/cut-retakes.py        # edit IN/OUT/KEEPS inside the script first
bash tools/silence-cut.sh          # edit IN/OUT paths inside the script first

# Shell tools (run from inside the project folder: video-projects/<name>/)
bash ../../tools/render-all.sh                                    # render YouTube + LinkedIn (+ TikTok if index-vertical.html exists)
bash ../../tools/extract-frame.sh renders/<project>.mp4 12.5     # extract a single frame at timestamp
bash ../../tools/thumbnail-render.sh                              # render thumbnail.html → YouTube + LinkedIn PNGs

# Install Python dependencies
pip install -r tools/requirements.txt
```

---

## Project structure

```
framesmith/                         ← workspace root
├── AGENTS.md                       ← this file
├── CLAUDE.md                       ← Claude Code-specific guide (slash commands, skills)
├── DESIGN.md                       ← brand spec (Hihnala default — read before brainstorming)
├── MOTION_PHILOSOPHY.md            ← motion discipline (read before brainstorming)
├── BRAND_SETUP.md                  ← how to swap the brand for your own
├── PRODUCTION_LOG.md               ← one-line-per-session log across all projects
├── assets/                         ← shared brand assets (logo, brand-tokens.css)
├── tools/                          ← video pipeline tools
│   ├── transcribe-whisper.py       ← word-level transcription via faster-whisper
│   ├── cut-retakes.py              ← last-take-rule retake removal
│   ├── silence-cut.sh              ← ffmpeg silence cutting
│   ├── render-all.sh               ← render YouTube + LinkedIn (+ TikTok if vertical exists)
│   ├── extract-frame.sh            ← extract a single frame at a timestamp
│   ├── thumbnail-render.sh         ← render thumbnail.html → YouTube + LinkedIn PNGs
│   └── requirements.txt
└── video-projects/                 ← one folder per project
    ├── .env                        ← API keys (gitignored — never commit)
    ├── series.json                 ← series definitions and episode registry
    ├── shared/                     ← shared intro/outro/lower-third compositions
    └── <project-name>/
        ├── index.html              ← root composition entry point
        ├── thumbnail.html          ← thumbnail composition (when built)
        ├── compositions/           ← sub-compositions (data-composition-src)
        ├── assets/                 ← media for this project (video, audio, images)
        ├── renders/                ← render outputs (gitignored)
        ├── meta.json               ← project metadata (id, name, dimensions, fps)
        ├── hyperframes.json        ← CLI config (all paths relative to project folder)
        ├── SCRIPT.md               ← video script (when written)
        ├── JOURNAL.md              ← project production journal
        └── DELIVERY.md             ← delivery sign-off (when cleared)
```

---

## Three workflow levels

### Level 1 — Website-to-Video

Convert an existing animated webpage into a short MP4 (6–15s).

```
Capture URL → design tokens → script → storyboard → build composition → lint → preview → render
```

### Level 2 — Storyboard-first Motion Graphics

Build original motion graphics from scratch.

```
Read DESIGN.md + MOTION_PHILOSOPHY.md
→ storyboard (scene count, timing, visual beats)
→ npx hyperframes init <name>
→ build compositions
→ lint → Studio preview → draft render → final render
```

**Two mandatory preview gates before any final render:**
1. Live Studio preview at localhost:3002 — iterate before paying render time
2. Draft MP4 scrub — verify pacing, captions, and beat alignment before final quality

### Level 3 — Guided Video (raw footage)

Full pipeline for talking-head or screen recordings.

```
Step 1: Silence cut     bash tools/silence-cut.sh
Step 2: Transcribe      python tools/transcribe-whisper.py raw-silence-cut.mp4
                        OR: npx hyperframes transcribe <file> --json  (ElevenLabs Scribe via .env)
Step 3: Retake cut      python tools/cut-retakes.py
Step 4: Storyboard motion overlay (plan scenes against edited-video timestamps)
Step 5: Build HyperFrames composition
Step 6: lint → Studio preview → draft render → final render
```

**All composition timestamps must use edited-video time — never original recording time.**

---

## Render contract (non-negotiable)

1. Root `<div>` requires `id`, `data-composition-id`, `data-start="0"`, `data-width`, `data-height`
2. Every timed visible element needs `class="clip"`, `data-start`, `data-duration`, `data-track-index` — **except** `<video>` and `<audio>` (adding `class="clip"` to `<video>` breaks playback)
3. GSAP timelines must be paused and registered on `window.__timelines`:
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
4. `<video>` must be `muted`. Audio belongs in a sibling `<audio>` element. One `<audio>` per source file.
5. Sub-compositions use `data-composition-src="compositions/file.html"` — never `masterTL.add(child)`
6. Never animate `width`/`height`/`top`/`left` on a `<video>` — wrap in a `<div>` and animate the wrapper
7. Every GSAP timeline ends with a no-op duration anchor to prevent black frame flash:
   ```js
   tl.to({}, { duration: SLOT_DURATION }, 0);
   ```
8. No `Date.now()`, no unseeded `Math.random()`, no render-time network fetches — compositions must be deterministic
9. Adjacent clips on the same `data-track-index` cannot overlap, even by milliseconds
10. Never call `.play()`, `.pause()`, or set `.currentTime` on media — the framework owns playback

---

## Brand system

`DESIGN.md` at the workspace root is the brand spec. Read it before writing any composition HTML.

Default brand: **Hihnala** — near-black canvas (`#06060A`), ember-orange accent (`#FF6A1A`), Source Serif 4 headings (weight 400), Plus Jakarta Sans body. Full token reference in `assets/brand-tokens.css`.

To use a different brand: follow `BRAND_SETUP.md`.

---

## Visual verification (required before delivery)

Lint passing does not mean the design is correct. Before reporting a render as done:

1. Render a draft: `npx hyperframes render --quality draft --output renders/draft.mp4`
2. Extract one frame per scene at its hero moment:
   ```bash
   ffmpeg -ss <time> -i renders/draft.mp4 -frames:v 1 -q:v 2 renders/frames/t<time>.png
   ```
3. Inspect every frame. Verify: no cropped faces, correct face mode per scene, captions on the right word, no text overflow, no blank frames, brand colors correct
4. Fix → re-render → re-verify. Never ship a broken render.

---

## API keys

`video-projects/.env` (gitignored). Copy `.env.example` for the template.

```
ELEVENLABS_API_KEY=your_key_here
```

ElevenLabs Scribe is used via `npx hyperframes transcribe` for multilingual content and speaker diarization. Local faster-whisper (English-only) via `python tools/transcribe-whisper.py` requires no API key.

---

## 21st.dev components

[21st.dev](https://21st.dev) is a UI component registry. Components must be adapted before use in HyperFrames:
- Convert React/JSX to plain HTML
- Replace CSS `@keyframes` with GSAP timelines (deterministic rendering)
- Add HyperFrames `data-*` attributes and `class="clip"`
- Replace component colors with brand tokens from `assets/brand-tokens.css`
- Remove any `Math.random()` or `Date.now()` calls

---

## Documentation

- Full docs: https://hyperframes.heygen.com/introduction
- Agent sitemap (fetch to resolve paths): https://hyperframes.heygen.com/llms.txt
- Catalog (50+ blocks): https://hyperframes.heygen.com/catalog/blocks/data-chart
- HTML schema reference: https://hyperframes.heygen.com/reference/html-schema
- Source repo: https://github.com/heygen-com/hyperframes
