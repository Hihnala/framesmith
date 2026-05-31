# Framesmith — Video Production Studio

HTML-native video workspace built on [HyperFrames](https://hyperframes.heygen.com). Hihnala brand by default — see `BRAND_SETUP.md` to swap to your own brand.

**Using a different agent?** See `AGENTS.md` for the agent-agnostic guide (Cursor, Gemini CLI, GitHub Copilot, etc.).

**This workspace hosts multiple video projects, one folder each, all under `video-projects/`.** The workspace root holds shared tooling and brand files — never put `index.html`, `assets/`, `compositions/`, or `renders/` directly at the root. Always work from inside a project subfolder.

---

## GATE SYSTEM — Invoke before doing anything

**Every workflow begins by invoking a gate. Ask before building.**

When the user says they want to make a video, ask these questions first — in one conversational pass. Do not start writing HTML or running commands until gates are closed.

### Gate 1: Identify the level

Which workflow level fits the request?

| Level | Trigger | What happens |
|---|---|---|
| **1 — Website-to-Video** | "Convert this page/URL", "turn my website into a video" | Run `/website-to-hyperframes` |
| **2 — Storyboard** | "Motion graphic", "promo", "social ad", "new video concept" | Plan scenes, storyboard, then build compositions |
| **3 — Guided Video** | "I have a recording", "talking head", "screen recording", "raw footage" | Full video pipeline: silence-cut → transcribe → retake-cut → composition |

If unclear, ask: *"Do you have existing footage, or are we building a motion graphic from scratch?"*

### Gate 2: Brand check

Before writing any composition HTML:

1. **Does `DESIGN.md` exist at the workspace root?** → Read it. Apply its exact colors, fonts, and motion rules.
2. **Has the user named a different brand?** → Check `BRAND_SETUP.md`, then read the new `DESIGN.md` they provide.
3. **No DESIGN.md?** → Ask three questions before writing any HTML:
   - What's the mood? (calm / cinematic / energetic / technical / editorial)
   - Light or dark canvas?
   - Any specific brand colors, fonts, or references?
   Then generate a minimal `DESIGN.md` from the answers.

**Hard rule: No default colors (#333, #3b82f6, Roboto). Every composition must trace back to DESIGN.md.**

### Gate 3: Project details

For any new project, ask before scaffolding:

1. Project name (used as folder: `video-projects/<name>/`)
2. Target duration and aspect ratio (16:9 1920×1080 / 9:16 1080×1920 / 1:1)
3. Delivery platform (YouTube / LinkedIn / Instagram / internal)
4. Assets on hand (footage, audio, logo, script, storyboard)

**Gate closed when:** level identified, brand confirmed, project name known.

---

## DESIGN.md + MOTION_PHILOSOPHY.md — READ BEFORE BRAINSTORMING

**You MUST read both before:**
- Brainstorming a composition, scene, or storyboard
- Proposing a visual direction, palette, or pacing
- Picking transitions, animations, or registry blocks
- Designing any kinetic typography, logo reveal, or product showcase

**How to use them:**
1. `DESIGN.md` overrides `MOTION_PHILOSOPHY.md` wherever brand rules conflict.
2. Read `MOTION_PHILOSOPHY.md` sections 0 and 4 every session — the 11 Laws and pre-flight checklist apply universally.
3. Apply Hihnala defaults: ~1.5s avg scene length, Deep Void `#06060A` canvas, ember glow behind focal elements, Source Serif 4 headlines with Plus Jakarta Sans labels, push-slide transitions with ember flash opener, hold outro 4–6s.

---

## THREE-LEVEL WORKFLOW

### Level 1: Website-to-Video

Convert an existing animated webpage into a short MP4 (6–15 seconds).

```
→ Invoke /website-to-hyperframes
→ Provide the URL
→ Lint → preview → draft render → final render
```

### Level 2: Storyboard-first Motion Graphics

Build original motion-graphic videos by planning before coding.

```
→ Read DESIGN.md + MOTION_PHILOSOPHY.md
→ Storyboard: scene count, timing, key visual beats
→ Scaffold: npx hyperframes init <name>
→ Build compositions one scene at a time
→ Lint → Studio preview (localhost:3002)
→ Draft render review
→ Final render
```

**Two mandatory preview gates before any final render:**
1. **Live Studio preview** (localhost:3002) — review live before any render
2. **Draft MP4 preview** — frame-verify draft before final quality render

### Level 3: Guided Video (full pipeline)

For camera recordings, screen recordings, or raw talking-head footage.

```
Step 01 · Raw footage → edited video
   silence-cut.sh       → removes silences
   transcribe-whisper.py → word-level transcript
   cut-retakes.py        → removes duplicate takes (last-take rule)
   process-audio.py      → audio enhancement (loudnorm, compression, optional pad)

Step 02 · Storyboard title card overlays
   Plan motion graphics that overlay on the edited video

Step 03 · HyperFrames composition
   Build the composition with video + motion overlay + captions
   Lint → Studio preview → draft render → final render

Step 04 · Optional: ElevenLabs Scribe (alternative transcription)
   Use for multilingual content or speaker diarization
   (requires ELEVENLABS_API_KEY in video-projects/.env)
```

**Python tools are in `tools/`. Always run them from the project folder.**

---

## SKILLS — USE THESE FIRST

Always invoke the matching skill before writing or modifying compositions.

| Skill | Command | When to use |
|---|---|---|
| `framesmith` | `/framesmith` | Gate system — start here when unsure |
| `script` | `/script` | Write video script in Hihnala brand voice before building |
| `journal` | `/journal` | Update project journal and workspace production log |
| `delivery` | `/delivery` | Pre-publish gate — produces signed-off DELIVERY.md |
| `series` | `/series` | Manage series specs, start episodes, check consistency |
| `hyperframes` | `/hyperframes` | Authoring compositions, captions, TTS, audio-reactive animation, transitions |
| `hyperframes-cli` | `/hyperframes-cli` | CLI: `init`, `lint`, `preview`, `render`, `transcribe`, `tts`, `doctor` |
| `gsap` | `/gsap` | GSAP timelines, easing, stagger, plugins, performance |
| `hyperframes-registry` | `/hyperframes-registry` | Installing catalog blocks/components via `npx hyperframes add <name>` |
| `website-to-hyperframes` | `/website-to-hyperframes` | URL → composition (7-step pipeline) |
| `make-a-video` | `/make-a-video` | Beginner end-to-end flow |
| `short-form-video` | `/short-form-video` | 9:16 talking-head + motion graphics playbook |
| `video-pipeline` | `/video-pipeline` | Level 3: silence-cut → transcribe → retake-cut → compose |
| `process-audio` | `/process-audio` | Two-pass loudnorm + light compression for talking-head audio |
| `multi-format` | `/multi-format` | Render to YouTube + LinkedIn (+ TikTok if vertical composition exists) |
| `thumbnail` | `/thumbnail` | Generate brand-consistent YouTube + LinkedIn thumbnails |
| `21st-dev` | `/21st-dev` | Search and import UI components from 21st.dev |

---

## COMMANDS

```bash
# Authoring loop (run from inside video-projects/<name>/)
npx hyperframes preview                          # Studio at localhost:3002 with hot reload
npx hyperframes lint                             # static HTML check — always before rendering
npx hyperframes compositions                     # list comp IDs + resolved durations
npx hyperframes render --quality draft --output renders/draft.mp4
npx hyperframes render --quality standard --output renders/final.mp4

# Catalog
npx hyperframes catalog --type block
npx hyperframes add <name>

# Media pipeline
npx hyperframes transcribe <file> --model small.en --json
npx hyperframes tts "text" --voice af_nova --output narration.wav

# Diagnostics
npx hyperframes doctor
npx hyperframes info --json
```

```bash
# Python tools (run from workspace root)
python tools/transcribe-whisper.py video-projects/<name>/raw.mp4
python tools/cut-retakes.py        # edit KEEPS list inside the script first
bash tools/silence-cut.sh          # edit IN/OUT paths inside the script first
python tools/process-audio.py --input video-projects/<name>/retakes-removed.mp4 --output video-projects/<name>/audio-processed.mp4

# Shell tools (run from inside the project folder)
bash ../../tools/render-all.sh                                    # render YouTube + LinkedIn (+ TikTok if index-vertical.html exists)
bash ../../tools/extract-frame.sh renders/<project>.mp4 12.5     # extract a single frame at timestamp
bash ../../tools/thumbnail-render.sh                              # render thumbnail.html → YouTube + LinkedIn PNGs
```

---

## FILE STRUCTURE

```
framesmith/
├── CLAUDE.md              ← this file
├── AGENTS.md              ← agent-agnostic guide
├── DESIGN.md              ← brand spec (Hihnala default)
├── MOTION_PHILOSOPHY.md   ← motion discipline (read before brainstorming)
├── BRAND_SETUP.md         ← swap-your-brand guide
├── PRODUCTION_LOG.md      ← one-line-per-session log across all projects
├── README.md              ← public docs
├── LICENSE                ← MIT
├── package.json
├── .env.example           ← API key template
├── assets/                ← shared brand assets
│   ├── brand-tokens.css
│   ├── hihnala-logo.jpg
│   └── ...
├── tools/                 ← video pipeline tools
│   ├── transcribe-whisper.py
│   ├── cut-retakes.py
│   ├── silence-cut.sh
│   ├── render-all.sh
│   ├── extract-frame.sh
│   ├── thumbnail-render.sh
│   ├── requirements.txt
│   └── nim-clients/       ← auto-cloned on first run (gitignored)
├── .claude/skills/        ← slash commands
└── video-projects/
    ├── .env               ← API keys (gitignored)
    ├── series.json        ← series definitions and episode registry
    ├── shared/            ← shared intro/outro/lower-third compositions
    └── <project-name>/
        ├── index.html
        ├── thumbnail.html ← thumbnail composition (when built)
        ├── compositions/
        ├── assets/
        ├── renders/
        ├── SCRIPT.md      ← video script (when written)
        ├── JOURNAL.md     ← project production journal
        └── DELIVERY.md    ← delivery sign-off (when cleared)
```

---

## CRITICAL RULES (non-negotiable)

1. **Never modify HyperFrames core code.** Work only in `video-projects/` and `assets/`.
2. **Always lint before rendering.** Zero errors required before any render command.
3. **Always run CLI from inside the project folder** (`video-projects/<name>/`), not the workspace root.
4. **Never put files at the workspace root.** Every project lives in its own subfolder.
5. **Quote costs before any paid generation** (TTS, ElevenLabs Scribe).
6. **Two preview gates before final render** — Studio live preview then draft MP4, both required.
7. **`.env` is always gitignored.** Never commit API keys.
