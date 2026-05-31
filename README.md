# Framesmith

**HTML-native video production studio powered by [HyperFrames](https://hyperframes.heygen.com). Works with any AI coding agent.**

Write HTML. Render video. No proprietary editors.

---

## What it is

Framesmith is an AI agent workspace for producing professional videos using HyperFrames — a framework that converts HTML compositions into deterministic MP4s. It ships with:

- **Three-level workflow** — Website-to-Video, Storyboard-first Motion Graphics, and Guided Video with raw footage editing
- **Full video pipeline** — silence cutting, word-level transcription, retake removal, audio enhancement, ElevenLabs Scribe support
- **Gate system** — the agent asks the right questions before doing anything
- **Hihnala brand system** by default, with a clear guide to swap it for your own
- **21st.dev integration** — pull UI components from the registry into your compositions
- **Sixteen agent skills** covering every stage of production

---

## Requirements

- Node.js ≥ 22
- FFmpeg (`brew install ffmpeg`)
- Python ≥ 3.10 (for video pipeline tools)
- Any AI coding agent (Claude Code, Cursor, Gemini CLI, GitHub Copilot, etc.)

---

## Quick start

```bash
git clone https://github.com/Hihnala/framesmith
cd framesmith
cp .env.example video-projects/.env
# Add your API keys to video-projects/.env:
#   ELEVENLABS_API_KEY  — transcription and TTS

npx skills add heygen-com/hyperframes   # install HyperFrames skills for your agent
```

Then open the project in your agent and describe what you want to make. The gate system will ask three questions — workflow level, brand, and project name — before doing anything.

**Claude Code users:** type `/framesmith` to run the gate system directly.

---

## Three workflow levels

### Level 1 — Website-to-Video

Convert any animated webpage into a short MP4 (6–15s).

```bash
npx hyperframes preview   # after the agent builds the composition
npx hyperframes render --quality standard --output renders/final.mp4
```

### Level 2 — Storyboard-first Motion Graphics

Build motion graphics from scratch with brand discipline. The agent reads `DESIGN.md` and `MOTION_PHILOSOPHY.md` before writing a single line of HTML, storyboards the scenes, then builds and renders.

Supports both 16:9 (promo, explainer) and 9:16 (TikTok, Reels, Shorts).

### Level 3 — Guided Video (raw footage → finished MP4)

Full pipeline for talking-head and screen recordings:

1. Silence cut — `tools/silence-cut.sh`
2. Word-level transcription — `tools/transcribe-whisper.py` (local) or ElevenLabs Scribe (multilingual)
3. Retake removal — `tools/cut-retakes.py`
4. Audio enhancement — `tools/process-audio.py`
5. HyperFrames composition with motion overlay and captions
6. Lint → Studio preview → draft render → final render

---

## Brand system

Framesmith ships with the **Hihnala** brand: near-black canvas (`#06060A`), ember-orange accents (`#FF6A1A`), Source Serif 4 headings (weight 400), Plus Jakarta Sans body.

To use your own brand:

1. Read `BRAND_SETUP.md`
2. Replace `DESIGN.md` with your brand spec
3. Update `assets/brand-tokens.css`
4. Add your logos to `assets/`

---

## Agent skills

Skills encode HyperFrames-specific patterns that are not in generic web docs. Install them once:

```bash
npx skills add heygen-com/hyperframes
```

| Skill | What it covers |
| --- | --- |
| `framesmith` | Gate system — establish level, brand, and project before any work |
| `script` | Write video scripts in brand voice, scene-timed for HyperFrames |
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
| `journal` | Update project journal and workspace production log |
| `delivery` | Pre-publish gate — structured checklist, signed-off DELIVERY.md |
| `series` | Manage series specs, episodes, and consistency checks |
| `21st-dev` | Import and adapt components from 21st.dev |

**Claude Code users:** skills load as slash commands automatically from `.claude/skills/`.

---

## 21st.dev integration

Framesmith includes a skill for pulling design components from [21st.dev](https://21st.dev) into your compositions. Components are adapted from React to plain HTML, colors replaced with brand tokens, and animations converted to GSAP for deterministic rendering.

---

## File structure

```
framesmith/
├── AGENTS.md              ← agent-agnostic guide (start here for non-Claude agents)
├── CLAUDE.md              ← Claude Code-specific guide (slash commands, skills)
├── DESIGN.md              ← brand spec (Hihnala default)
├── MOTION_PHILOSOPHY.md   ← motion discipline (read before brainstorming)
├── BRAND_SETUP.md         ← how to swap the brand
├── assets/                ← shared brand assets
├── tools/                 ← Python video pipeline tools
└── video-projects/        ← one folder per project
```

---

## Documentation

**Framesmith docs** (in this repo):

- [getting-started.md](./docs/getting-started.md) — installation, first project, project structure
- [how-it-works.md](./docs/how-it-works.md) — gate system, three workflow levels, production loop
- [skills.md](./docs/skills.md) — all sixteen skills with usage guide
- [brand-system.md](./docs/brand-system.md) — Hihnala brand and how to swap it for your own
- [tools.md](./docs/tools.md) — Python and shell tools reference

**HyperFrames docs** (external):

- HyperFrames docs: https://hyperframes.heygen.com/introduction
- Agent sitemap: https://hyperframes.heygen.com/llms.txt
- Catalog (50+ blocks): https://hyperframes.heygen.com/catalog/blocks/data-chart

---

## License

MIT — see `LICENSE`. Built by [Markku Hihnala / Hihnala](https://hihnala.com).

[HyperFrames](https://github.com/heygen-com/hyperframes) is built by HeyGen, licensed under Apache 2.0.

Additional inspiration from Nate Herk's [fork](https://github.com/nateherkai/hyperframes-student-kit), and Robonuggets [fork](https://github.com/robonuggets/hyperframes-helper) of HeyGen's repo.
