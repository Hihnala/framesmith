---
name: script
description: Write a video script in the Hihnala brand voice for YouTube or LinkedIn — educational, thought leadership, or personal video types. Produces a SCRIPT.md file with scene breakdown, VO lines, visual directions, and timestamps mapped to HyperFrames scene slots. Always invoke before building any composition. Ask before writing.
---

# Script — Video Script Writer

Writes production-ready scripts in the Hihnala brand voice. Output is a `SCRIPT.md` that maps directly to HyperFrames timing — scene numbers, timestamps, word counts, and visual directions are baked in so the composition can be built from the script without interpretation.

## Gate — Ask before writing

Run this intake in one pass before writing a single word:

1. **Platform** — YouTube or LinkedIn? (determines hook structure, pacing, caption requirements)
2. **Video type** — Educational / Thought leadership / Personal?
3. **Topic** — what is this video about? (one sentence)
4. **Core insight** — what's the single most important thing the viewer takes away?
5. **Target duration** — short (20–45s) / medium (45–90s) / long (90s–3min)?
6. **CTA** — what should the viewer do at the end? (default: "Clarity before commitment" / link to hihnala.com)
7. **Assets on hand** — any footage, screen recordings, or b-roll that should be noted in visual directions?

Do not write the script until all seven are answered.

---

## Hook structures

### YouTube — Educational

| Beat | Timing | Words | Purpose |
|---|---|---|---|
| Hook | 0–5s | 15–25 | Bold claim, provocative question, or surprising fact. Earns the next 5 seconds. No context, no setup. |
| Problem | 5–20s | 40–80 | What's broken or misunderstood. Make it felt — not just stated. |
| Promise (optional) | 15–25s | 20–30 | What they'll know or be able to do by the end. |
| Teaching body | bulk | varies | One idea per scene. ~1.5s average scene length. Short declarative sentences. |
| Proof | as needed | varies | Concrete example, case, or number. Never abstract. |
| Takeaway | last 10–15s | 20–40 | The one sentence to remember. Make it quotable. |
| CTA | last 5–10s | 10–20 | Single clear action. Never two CTAs. |

### YouTube — Thought Leadership

| Beat | Timing | Words | Purpose |
|---|---|---|---|
| Hook | 0–5s | 15–25 | Bold claim that will divide the room. State the contrarian position. |
| Evidence | 5–25s | 60–100 | Why this claim is true. Two or three sharp proof points. |
| Implication | bulk | varies | What this means in practice. Specific, operational. |
| So what | near end | 20–40 | The decision the viewer now has to make. |
| CTA | last 5–10s | 10–20 | Single clear action. |

### YouTube — Personal

| Beat | Timing | Words | Purpose |
|---|---|---|---|
| Story hook | 0–5s | 15–25 | Drop into the middle of the story. Skip the setup. |
| What happened | 5–30s | varies | The experience. First person, specific details, short sentences. |
| Lesson | bulk | varies | What it taught. One clear idea. |
| Application | near end | 20–40 | How the viewer can apply this. Practical, grounded. |
| CTA | last 5–10s | 10–20 | Softer than educational — an invitation, not a directive. |

### LinkedIn (all types)

LinkedIn is sound-off by default. Captions are mandatory.

| Beat | Timing | Words | Purpose |
|---|---|---|---|
| Hook | 0–3s | ≤10 | Must work without audio. Readable as a caption in 3 seconds. Provocative or specific. |
| Body | 3–45s | varies | Shorter than YouTube. Get to the insight faster. One idea per scene. |
| Takeaway | near end | 10–20 | The one sentence. Quotable. |
| CTA | last 5s | 5–15 | Conversational — a question to the audience or a soft invite, not a hard sell. |

---

## Brand voice rules (Hihnala)

Apply to every line of VO:

- Short sentences. One idea per sentence. No conjunctions to extend.
- Calm confidence — state without overselling.
- Affirmative positioning — say what is true, not what it avoids.
- No hype words: **never** use "revolutionary," "cutting edge," "disruptive," "seamless," "unleash," "leverage," "next-gen," "game-changer."
- No qualifiers that undercut authority: "kind of," "sort of," "basically," "I guess," "you know."
- Prefer operational language: "reduces friction," "improves consistency," "clarifies the decision," "removes the guesswork."
- Maximum sentence length for VO: ~15 words. If it runs longer, split it.

---

## Output format

Save as `SCRIPT.md` in the project folder (`video-projects/<name>/SCRIPT.md`).

```markdown
# [Video Title]

**Platform:** YouTube / LinkedIn
**Type:** Educational / Thought leadership / Personal
**Duration:** ~Xs (~N scenes)
**CTA:** [the exact CTA line]

---

## Scene breakdown

| # | Label | Start | End | Duration | Est. words |
|---|---|---|---|---|---|
| 01 | Hook | 0:00 | 0:05 | 5s | 20 |
| 02 | Problem | 0:05 | 0:18 | 13s | 55 |
| 03 | … | … | … | …s | … |

---

## Full script

### Scene 01 — Hook [0:00–0:05] ~20 words
**VO:** "Exact spoken words here."
**Visual:** Deep Void canvas. Single large serif line. Ember glow behind focal word.
**Captions note:** [anything specific about caption timing or emphasis]

### Scene 02 — Problem [0:05–0:18] ~55 words
**VO:** "First sentence. Second sentence. Third sentence."
**Visual:** Two-scene sequence. First: statement. Second: consequence or data point.

[continue for all scenes]

---

## CTA scene [X:XX–X:XX]
**VO:** "[exact CTA line]"
**Visual:** Hold on brand outro. Logo present. Ember accent. Still for 4–6s.

---

## Production notes
- Footage needed: [list any b-roll, screen recordings, or assets]
- Captions: [mandatory for LinkedIn / recommended for YouTube]
- Music: [tone suggestion — no specific track]
```

---

## After the script

Once `SCRIPT.md` is approved:

1. Pass scene breakdown directly to the HyperFrames composition builder
2. Each scene row maps to one sub-composition with `data-start` and `data-duration` from the timing column
3. VO lines map to caption data or TTS input
4. Visual directions map to GSAP animation choices — reference MOTION_PHILOSOPHY.md and DESIGN.md

The script is the source of truth for timing. Do not adjust scene timings in the composition without updating `SCRIPT.md` first.
