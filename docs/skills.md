# Skills

Framesmith ships with sixteen agent skills. Each skill is a knowledge file that tells the agent exactly how to perform a specific stage of production. In Claude Code they load as slash commands. In other agents they are available via `npx skills add heygen-com/hyperframes` and referenced by name.

Skills are not scripts — they are instructions. The agent reads the relevant skill before acting, which means it applies the right rules, asks the right questions, and produces consistent output every time.

---

## Install

```bash
npx skills add heygen-com/hyperframes
```

This installs the HyperFrames framework skills. The Framesmith-specific skills (`framesmith`, `script`, `multi-format`, `thumbnail`, `journal`, `delivery`, `series`) are already in `.claude/skills/` and do not require a separate install.

---

## Skill index

| Skill | Claude Code | Stage |
| --- | --- | --- |
| [framesmith](#framesmith) | `/framesmith` | Start |
| [script](#script) | `/script` | Pre-build |
| [hyperframes](#hyperframes) | `/hyperframes` | Build |
| [hyperframes-cli](#hyperframes-cli) | `/hyperframes-cli` | Build |
| [gsap](#gsap) | `/gsap` | Build |
| [hyperframes-registry](#hyperframes-registry) | `/hyperframes-registry` | Build |
| [website-to-hyperframes](#website-to-hyperframes) | `/website-to-hyperframes` | Level 1 |
| [make-a-video](#make-a-video) | `/make-a-video` | Level 2 |
| [short-form-video](#short-form-video) | `/short-form-video` | Level 2 |
| [video-pipeline](#video-pipeline) | `/video-pipeline` | Level 3 |
| [multi-format](#multi-format) | `/multi-format` | Post-build |
| [thumbnail](#thumbnail) | `/thumbnail` | Post-build |
| [journal](#journal) | `/journal` | Throughout |
| [delivery](#delivery) | `/delivery` | Pre-upload |
| [series](#series) | `/series` | Series episodes |
| [21st-dev](#21st-dev) | `/21st-dev` | Build (optional) |

---

## framesmith

**The gate system. Start every session here.**

Runs the three-gate intake before any work begins:
1. Identifies which workflow level fits the request
2. Loads and confirms the brand from `DESIGN.md`
3. Collects project name, duration, aspect ratio, platform, and assets

When all three gates close, the agent summarises the plan and waits for your confirmation before scaffolding anything.

**When to use:** at the start of any session, or when you are unsure which skill to invoke next.

**Output:** confirmed plan → hands off to the correct skill for the chosen level.

---

## script

**Write the video script before building anything.**

Runs a seven-question intake (platform, video type, topic, core insight, duration, CTA, assets on hand), then writes `SCRIPT.md` in the project folder.

The output maps directly to HyperFrames timing. Every scene in `SCRIPT.md` includes:

- Scene number and label
- Start and end timestamps
- Estimated word count
- VO lines (exact spoken words)
- Visual direction (what the composition should show)

This scene breakdown becomes the source of truth for `data-start` and `data-duration` values in the composition. The agent never needs to guess at timing — it reads the scene table.

**Hook structures supported:**

| Video type | Platform | Structure |
| --- | --- | --- |
| Educational | YouTube | Hook → Problem → Promise → Teaching → Proof → Takeaway → CTA |
| Thought leadership | YouTube | Bold claim → Evidence → Implication → So what → CTA |
| Personal | YouTube | Story hook → What happened → Lesson → Application → CTA |
| Any type | LinkedIn | Hook (≤10 words, works silent) → Body → Takeaway → Soft CTA |

**Brand voice rules applied automatically:**
- Short sentences — one idea per sentence
- No hype words (revolutionary, seamless, leverage, etc.)
- Operational language (reduces friction, improves consistency, clarifies the decision)
- Maximum ~15 words per VO sentence

**When to use:** always, before building any composition. The script is the foundation everything else is built on.

**Output:** `video-projects/<name>/SCRIPT.md`

---

## hyperframes

**The primary composition authoring skill.**

Covers everything involved in writing HyperFrames HTML: clip structure, timing attributes, GSAP timelines, captions, TTS, audio-reactive animation, transitions, and the render contract.

Before writing any HTML, this skill enforces the **visual identity gate**: it reads `DESIGN.md`, confirms the brand, and refuses to use generic colors or fonts. Every composition must trace its palette and typography back to `DESIGN.md`.

It also enforces the **layout-before-animation** principle: build the static end-state first (where every element is at its most visible moment), then add GSAP entrances. This prevents overlaps and misaligned layouts that only appear after a full render.

**Key rules it enforces:**

- `class="clip"` on every timed visible element (never on `<video>` or `<audio>`)
- `data-start`, `data-duration`, `data-track-index` on every clip
- GSAP timeline registered paused on `window.__timelines["<id>"]`
- `tl.to({}, { duration: SLOT_DURATION }, 0)` no-op anchor at the end of every timeline
- No `Math.random()`, `Date.now()`, or render-time network fetches
- Animate only `transform` and `opacity` — never `top`, `left`, `width`, `height`
- `<video>` must be `muted`; audio in a separate `<audio>` element

**When to use:** whenever building or editing compositions, adding captions, wiring TTS, or creating transitions. Invoke before writing any HTML.

**HyperFrames reference:** [hyperframes.heygen.com/introduction](https://hyperframes.heygen.com/introduction)

---

## hyperframes-cli

**All CLI commands.**

Covers every `npx hyperframes` command with the correct flags for each use case.

```bash
npx hyperframes preview                          # Studio at localhost:3002
npx hyperframes lint                             # validate — fix all errors before rendering
npx hyperframes render --quality draft           # fast iteration
npx hyperframes render --quality standard        # final delivery
npx hyperframes render --quality high            # archival / YouTube upload quality
npx hyperframes transcribe <file> --json         # word-level transcript (ElevenLabs Scribe)
npx hyperframes tts "text" --voice af_nova       # text-to-speech
npx hyperframes doctor                           # environment check
npx hyperframes compositions                     # list comp IDs and durations
npx hyperframes add <name>                       # install catalog block or component
```

**Quality guide:**
- `draft` — CRF 28, fast. Use for iteration.
- `standard` — CRF 18, visually lossless at 1080p. Use for LinkedIn and review.
- `high` — CRF 15. Use for YouTube (upload the best source, let them compress).

**When to use:** for any CLI operation — scaffolding, linting, previewing, rendering, transcribing.

---

## gsap

**GSAP animation — timelines, easing, stagger, performance.**

Covers `gsap.to()`, `gsap.from()`, `gsap.fromTo()`, timeline position parameter, labels, nesting, stagger, and performance rules.

**Hihnala easing defaults:**
- Entrances: `power3.out`
- Snappy reveals: `expo.out`
- Background transitions: `sine.inOut`
- Scene transitions: `power2.inOut` (push), `power4.inOut` (ember flash)
- Precise custom spring: `cubic-bezier(0.32, 0.72, 0, 1)` via GSAP CustomEase

**Duration bands:**
- Snap entrances: 0.3–0.5s
- Headline entrances: 0.6–0.9s
- Ambient / breathing: 3–5s

**When to use:** whenever adding or modifying GSAP animations in compositions. Invoke alongside `hyperframes` for complex animation work.

---

## hyperframes-registry

**Install catalog blocks and components.**

HyperFrames ships with 50+ pre-built registry blocks (data charts, social overlays, shader transitions, logo outros, app showcases) and 3 components (grain overlay, shimmer sweep, grid pixelate wipe).

```bash
npx hyperframes catalog --type block      # browse blocks
npx hyperframes catalog --type component  # browse components
npx hyperframes add <name>               # install into compositions/
```

**Notable blocks for Framesmith use:**
- `logo-outro` — branded outro card
- `yt-lower-third` — YouTube lower-third name tag
- `data-chart` — animated data visualisation
- `cinematic-zoom`, `glitch`, `whip-pan` — shader transitions
- `transitions-push`, `transitions-blur` — CSS transition packs
- `grain-overlay` — film grain (always-on for Hihnala brand)

**When to use:** before manually building any component that might already exist in the registry. Always check the catalog first.

**Registry reference:** [hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog/blocks/data-chart)

---

## website-to-hyperframes

**Convert a URL to a video — Level 1.**

Seven-step pipeline: capture the page → extract design tokens → write a script → storyboard → build composition → validate → render.

The agent uses Playwright to screenshot and analyse the source page, extracts colors and layout, then builds a HyperFrames composition that matches the page's visual style. The result is a short MP4 (typically 6–15 seconds) suitable for social or product demos.

**When to use:** whenever you have a URL and want a video from it. Even if the user just pastes a link, this is the right skill.

---

## make-a-video

**End-to-end guided flow for any new video — Level 2.**

Runs eight sequential gates: intent and format → script and voice → style intake → storyboard → scaffold → compositions → preview → render. Designed for cases where you want to be walked through the entire process rather than invoking individual skills.

**When to use:** starting a new Level 2 video from scratch, especially if you are less familiar with the workflow. For experienced use, invoking individual skills (`script`, `hyperframes`, `multi-format`) is faster.

---

## short-form-video

**9:16 vertical video for social — Level 2.**

Specifically designed for talking-head + motion graphic overlay + karaoke captions at 1080×1920. Encodes the face-mode choreography system:

- **BOTTOM mode** — face fills the bottom half of the frame (1080×607.5), motion graphic overlay in the top half
- **FULLSCREEN mode** — face crops to fill the full portrait frame (1920×1080 source scaled to cover 1080×1920)

The composition uses a four-layer structure: ambient background, face video, scene overlays, captions. Each layer runs on its own track index so they never interfere.

**When to use:** any 9:16 social video with a talking head, regardless of platform.

---

## video-pipeline

**Full production pipeline for raw footage — Level 3.**

Guides the complete journey from raw recording to finished MP4:

1. Silence cut (`tools/silence-cut.sh`)
2. Transcription — local faster-whisper or ElevenLabs Scribe
3. Retake cut (`tools/cut-retakes.py`)
4. Storyboard motion overlays
5. HyperFrames composition
6. Lint → preview → draft render → final render

**Transcription options:**

| Option | Tool | Best for |
| --- | --- | --- |
| Local | `python tools/transcribe-whisper.py` | English content, no API cost, runs offline |
| ElevenLabs Scribe | `npx hyperframes transcribe --json` | Multilingual, speaker diarisation, high accuracy |

Scribe requires `ELEVENLABS_API_KEY` in `video-projects/.env`.

**When to use:** any time you have a recording that needs to be edited before becoming a HyperFrames composition.

---

## multi-format

**Render to YouTube and LinkedIn in one command.**

```bash
# Run from inside video-projects/<name>/
bash ../../tools/render-all.sh
```

Produces:
- `renders/<name>-youtube.mp4` — high quality
- `renders/<name>-linkedin.mp4` — standard quality
- `renders/<name>-tiktok.mp4` — if `index-vertical.html` exists

After rendering, the script checks that YouTube and LinkedIn durations match within 0.1 seconds and warns if they diverge.

**TikTok/Reels:** create `index-vertical.html` (1080×1920) in the project folder. The script detects it automatically on the next run.

**When to use:** after a final render is approved, before running the delivery checklist.

---

## thumbnail

**Brand-consistent YouTube and LinkedIn thumbnails.**

Two modes:

**Dedicated composition (primary):**

The agent builds `thumbnail.html` (1280×720) using the Hihnala brand system — Deep Void canvas, Source Serif 4 hook phrase, optional portrait with gradient mask, single Ember accent. Then:

```bash
bash ../../tools/thumbnail-render.sh
```

Renders the composition, extracts a frame at t=0.5s, and scales to LinkedIn dimensions. Outputs:
- `renders/thumbnail-youtube-1280x720.png`
- `renders/thumbnail-linkedin-1200x627.png`

**Frame extract (quick reference):**

```bash
bash ../../tools/extract-frame.sh renders/<name>-youtube.mp4 12.5
```

Extracts the frame at 12.5 seconds. Useful for finding a candidate frame before building the dedicated composition.

**When to use:** after the script is approved, before or after the final render. The dedicated composition is always the deliverable — frame extraction is for reference only.

---

## journal

**Production record — update after every milestone.**

Creates and maintains two files:

- `video-projects/<name>/JOURNAL.md` — full session log for this project
- `PRODUCTION_LOG.md` at workspace root — one-line index across all projects

A journal entry includes: date, stage, duration (if render exists), decisions made, issues encountered, and what is needed next.

**Update after:**
- Script approved
- Draft render completed and reviewed
- Final render completed
- Thumbnails generated
- Delivery sign-off

**When resuming a session:** the agent reads `JOURNAL.md` before asking what to do next. The journal is the source of truth for what was decided and why — never rely on conversation memory.

**When to use:** after any significant milestone. Do not batch journal entries — write them as you go so the record is useful if the session ends unexpectedly.

---

## delivery

**Pre-publish gate. No video ships without a signed-off DELIVERY.md.**

Runs a four-category checklist by actually checking the files — not by asking you to confirm:

| Category | What it checks |
| --- | --- |
| **Content** | Hook in first 3s, single CTA, no banned words, script approved, captions accurate, duration within platform limits |
| **Brand** | Source Serif 4 headings, Plus Jakarta Sans body, brand colors only, no `transparent` in gradients, logo in outro, double-bezel on elevated containers |
| **Technical** | lint zero errors, both preview gates completed, YouTube + LinkedIn renders produced, durations match, no `Math.random()` or `Date.now()`, no render-time network fetches |
| **Platform** | YouTube thumbnail exists and is readable at small sizes, LinkedIn thumbnail exists, JOURNAL.md updated, series check passed (if series episode) |

Critical items (`*`) block delivery. Non-critical items produce a warning but do not block.

When everything passes, the agent creates `DELIVERY.md` in the project folder as a permanent sign-off record.

**When to use:** after the final render and thumbnails are ready, before uploading anywhere.

---

## series

**Manage recurring video formats.**

Series specs live in `video-projects/series.json`. Each series defines:

- Shared intro and outro compositions (in `video-projects/shared/`)
- Lower-third: name, title, position, timing
- Caption style: font, size, color, accent color, position
- CTA line (verbatim — applied to every episode)
- Title format (e.g. `EP01: Title`)
- Episode registry (number, title, project folder, date, status, published URLs)

**Starting a new series:** the agent asks ten questions (name, platform, type, cadence, intro/outro duration, lower-third, caption style, CTA, title format) and adds the spec to `series.json`.

**Starting a new episode:** the agent loads the series spec, applies it to the new project, wires the shared intro/outro compositions, and pre-fills the CTA and lower-third with spec values.

**Series consistency check:** run before the delivery gate on any series episode. Verifies intro/outro timing, lower-third position and copy, caption style, and CTA line against the spec. Any deviation is a blocking issue.

**Tracking episodes:**

```json
{
  "number": 3,
  "title": "The Clarity Framework",
  "project": "video-projects/clarity-framework",
  "date": "2026-05-18",
  "status": "delivered",
  "platforms": {
    "youtube": { "url": "https://youtu.be/...", "published": "2026-05-20" },
    "linkedin": { "url": "https://linkedin.com/...", "published": "2026-05-20" }
  }
}
```

**When to use:** whenever a video is part of a recurring format, at the start of the project (not at the end).

---

## 21st-dev

**Import UI components from **[**21st.dev**](https://21st.dev)**.**

21st.dev is a community registry of animated UI components — prompt boxes, cards, loaders, data visualisations, motion patterns. This skill adapts them for HyperFrames.

**Adaptation process:**

1. Fetch the component source from the 21st.dev URL
2. Convert React/JSX to plain HTML (HyperFrames is not React-based)
3. Replace CSS `@keyframes` with GSAP timelines for deterministic rendering
4. Add HyperFrames `data-*` attributes and `class="clip"` wrappers
5. Replace component colors with Hihnala brand tokens from `assets/brand-tokens.css`
6. Remove any `Math.random()` or `Date.now()` calls
7. Lint and preview before use

**Limitations:** Canvas/WebGL-heavy components may not render correctly in headless Chrome. Test at draft quality before committing to a final render.

**When to use:** before manually building a UI component that might already exist on 21st.dev. Check the registry first.
