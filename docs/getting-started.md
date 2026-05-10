# Getting Started

Framesmith is an AI agent workspace for producing professional videos with [HyperFrames](https://hyperframes.heygen.com). This guide walks you through installation, setup, and your first project.

---

## Requirements

Before cloning the repo, make sure you have these installed:

| Tool | Version | Install |
| --- | --- | --- |
| Node.js | ≥ 22 | [nodejs.org](https://nodejs.org) or `brew install node` |
| FFmpeg | Any recent | `brew install ffmpeg` |
| Python | ≥ 3.10 | System Python or `brew install python` |
| AI coding agent | Any | Claude Code, Cursor, Gemini CLI, GitHub Copilot |

Verify your environment after cloning:

```bash
npx hyperframes doctor
```

This checks Node.js, FFmpeg, Chrome (bundled by HyperFrames), and memory. Fix anything it flags before starting.

---

## Installation

```bash
git clone https://github.com/Hihnala/framesmith
cd framesmith

# Install Python dependencies (for video pipeline tools)
pip install -r tools/requirements.txt

# Install HyperFrames agent skills
npx skills add heygen-com/hyperframes
```

### Set up API keys

```bash
cp .env.example video-projects/.env
```

Open `video-projects/.env` and add your ElevenLabs API key. This is used for transcription (Scribe) and text-to-speech:

```
ELEVENLABS_API_KEY=your_key_here
```

The `.env` file is gitignored. Never commit it.

---

## Opening the workspace in your agent

### Claude Code

```bash
cd framesmith
claude
```

Type `/framesmith` to start the gate system. The agent will ask three questions — workflow level, brand confirmation, project name — before doing anything.

### Other agents (Cursor, Gemini CLI, Copilot, etc.)

Open the `framesmith/` folder in your agent. Point it to `AGENTS.md` as the entry point:

> "Read AGENTS.md and tell me how to get started."

The agent will load the gate system and guide you from there.

---

## Project structure

```
framesmith/
├── AGENTS.md              ← agent-agnostic guide (start here)
├── CLAUDE.md              ← Claude Code slash commands and skills
├── DESIGN.md              ← Hihnala brand spec — read before any composition
├── MOTION_PHILOSOPHY.md   ← motion discipline — read before brainstorming
├── BRAND_SETUP.md         ← how to swap the brand for your own
├── PRODUCTION_LOG.md      ← one-line session log across all projects
├── assets/                ← shared brand assets
├── tools/                 ← video pipeline tools
├── .claude/skills/        ← agent skills (slash commands in Claude Code)
└── video-projects/
    ├── .env               ← API keys (gitignored)
    ├── series.json        ← series definitions and episode tracking
    ├── shared/            ← shared intro/outro/lower-third compositions
    └── <project-name>/    ← one folder per video project
        ├── index.html          ← root composition
        ├── thumbnail.html      ← thumbnail composition
        ├── compositions/       ← sub-compositions
        ├── assets/             ← project media (video, audio, images)
        ├── renders/            ← output files (gitignored)
        ├── SCRIPT.md           ← video script
        ├── JOURNAL.md          ← project production journal
        └── DELIVERY.md         ← delivery sign-off
```

**Key rule:** every project lives in its own subfolder under `video-projects/`. Never put `index.html`, `assets/`, or `renders/` at the workspace root.

---

## Your first project

### Step 1 — Tell the agent what you want to make

Claude Code: `/framesmith`
Other agents: "I want to make a video about [topic]."

The gate system asks:
1. **Level** — webpage-to-video, motion graphic from scratch, or raw footage?
2. **Brand** — reads `DESIGN.md`, confirms the brand
3. **Project details** — name, duration, aspect ratio, platform, assets on hand

### Step 2 — Write the script

Before touching any HTML, run the script skill:

Claude Code: `/script`
Others: "Write a script for this video."

The agent asks about your hook, video type, and CTA, then produces `SCRIPT.md` with scene breakdown and timing mapped directly to HyperFrames slots.

### Step 3 — Build the composition

The agent scaffolds the project and builds the HTML compositions from your script. All timing, colors, and typography come from `DESIGN.md` automatically.

```bash
cd video-projects/<name>
npx hyperframes lint       # always before rendering
npx hyperframes preview    # Studio at localhost:3002
```

### Step 4 — Render

```bash
# From inside video-projects/<name>/
bash ../../tools/render-all.sh
```

Produces `renders/<name>-youtube.mp4` and `renders/<name>-linkedin.mp4`.

### Step 5 — Generate thumbnails

Claude Code: `/thumbnail`
Others: "Build a thumbnail for this video."

Then:

```bash
bash ../../tools/thumbnail-render.sh
```

Produces `renders/thumbnail-youtube-1280x720.png` and `renders/thumbnail-linkedin-1200x627.png`.

### Step 6 — Delivery check

Claude Code: `/delivery`
Others: "Run the delivery checklist."

The agent checks every critical item (content, brand, technical, platform) and produces `DELIVERY.md` when everything passes.

### Step 7 — Upload

Take the files from `renders/` and upload to your platforms. Update the episode record in `series.json` with the published URLs.

---

## Updating the brand

Framesmith ships with the Hihnala brand by default. To use your own:

1. Read [BRAND_SETUP.md](./../BRAND_SETUP.md)
2. Replace `DESIGN.md` with your brand spec
3. Update `assets/brand-tokens.css` with your tokens
4. Add your logo files to `assets/`

See [brand-system.md](./brand-system.md) for the full guide.

---

## Where to go next

- [how-it-works.md](./how-it-works.md) — gate system, three workflow levels, production loop
- [skills.md](./skills.md) — all sixteen skills explained
- [brand-system.md](./brand-system.md) — Hihnala brand and how to swap it
- [tools.md](./tools.md) — Python and shell tools reference
- [HyperFrames docs](https://hyperframes.heygen.com/introduction) — the rendering framework Framesmith is built on
