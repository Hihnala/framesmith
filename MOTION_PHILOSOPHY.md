# MOTION PHILOSOPHY — Hihnala

*Quiet Power in Motion. Every frame earns its place.*

Read this before starting any composition. Re-read the Laws and the overlay system before brainstorming any new scene.

---

## For Other Brands

This file ships pre-filled with the **Hihnala** brand. The structure — Laws, overlay system, pacing rules, technical recipes, pre-flight checklist — applies to any brand. The brand layer (colors, fonts, move names, act assignments) is what you replace.

| Universal (keep as-is) | Brand-specific (replace) |
| --- | --- |
| The 10 Laws (concepts) | Color references in the Laws |
| Overlay system types and pacing | Overlay card colors, fonts, accent hex values |
| Pacing discipline (timing values) | Canvas color and accent families |
| All technical recipes (§4.x) | Accent rgba values in recipes |
| GSAP easing reference | Move names ("Ember pulse," "Amber whip," etc.) |
| Sub-comp gotchas (§5) | None — these are framework rules |
| Pre-flight checklist structure | Brand-specific checklist items |

**Substitution map:**

| Hihnala element | Generic role | Your value |
| --- | --- | --- |
| Deep Void `#06060A` | Canvas / darkest background | ***\_***___ |
| Soft White `#F5F5F7` | Primary text | ***\_***___ |
| Silver `#CDCDD4` | Secondary text / italic anchor | ***\_***___ |
| Ember `#FF6A1A` | Primary accent — action, CTA, decisive moments | ***\_***___ |
| Steel `#4F6D8A` | Secondary accent — context, infrastructure | ***\_***___ |
| Copper `#D4892F` | Tertiary accent — structure, labels | ***\_***___ |
| Source Serif 4 (weight 400) | Heading / authority font | ***\_***___ |
| Plus Jakarta Sans | Body / UI / caption font | ***\_***___ |

Also update `BRAND_SETUP.md` when adapting this file.

---

## 0 · The 10 Laws

1. **One idea per overlay or beat. Cut fast.** Each card or kinetic text element carries ONE concept. Each full-screen scene lands ONE word or claim and moves on. If a scene or card says two things, split it.

2. **The canvas depends on the beat type.** For full-screen composition beats (intro, CTA, chapter transition): Deep Void (`#06060A`) fills 80–90% of the frame and negative space is the design. For overlay beats on white-background footage: the speaker and the footage are the canvas; the dark glass card carries the brand.

3. **Light and contrast signal brand.** On full-screen beats: Ember glow means decision, Steel trace means infrastructure, Copper marks mean structure. On overlay beats: the dark card is the signal — it brings the Hihnala palette into a bright-background context. Nothing appears without a reason.

4. **The frame must live.** Full-screen still frames have ambient motion: particle drift, vignette pulse, ember radial shift. Overlay beats keep the speaker as the live element — cards slide in cleanly and hold without restlessness.

5. **Overlay cards enter with intent, exit during silence.** Entry: crisp, fast (0.4–0.7s), directional. Exit: during a natural spoken pause, never competing with what is being said. A card that exits while the speaker is mid-sentence loses the viewer.

6. **Serif authority at readable scale.** Source Serif 4 at weight 400 is the compositional voice. In video: minimum 48px for headings, minimum 52px for lower third names, minimum 64px for pull quotes. Authority comes from scale and contrast, not thickness. Never bold.

7. **One dominant accent per beat.** Follow the psychological order: Steel (infrastructure) → Copper (structure) → Ember (decision). Never invert it within a piece. On overlay cards: one accent color per card. The Ember underline on a stat callout and a Steel label on the same card is mixing equals — pick one.

8. **Hold the moments that matter.** Lower thirds: 4–5 seconds. Stat callouts: match spoken duration, minimum 2.5s. Pull quotes: spoken duration + 1s. Final CTA: 5+ seconds of stillness. Speed earns the right to hold.

9. **Captions always.** Word-by-word captions are the highest single retention lever in talking-head video. They run continuously and are never turned off for a cleaner look. Viewers read before they listen.

10. **Timelines must fill their slots.** HyperFrames hides a sub-composition the moment `timeline.duration()` falls short of `data-duration` — producing a black frame flash. Every GSAP timeline ends with `tl.to({}, { duration: SLOT_DURATION }, 0)` as a no-op anchor. Non-negotiable.

---

## 1 · The Hihnala Video Model

Hihnala videos are talking-head shots on a white background. The speaker carries the authority. The overlay system carries the brand. The structure below applies to a 4–8 minute YouTube video; scale down for shorter formats.

### Act structure

| Act | Duration | What happens | Overlay types active |
| --- | --- | --- | --- |
| **Cold open / hook** | 0–30s | Speaker opens with a provocation or claim. No overlays yet — let the face land first. Captions always active. | Captions only |
| **Lower third** | 0:30–1:00 | Speaker ID card appears after the hook lands. Slides in, holds 4–5s, exits before first main point. | Lower third |
| **Body — point 1** | 1:00–3:00 | Captions + stat callouts when numbers are spoken. Pull quote for the key claim. | Captions, Stat, Pull quote |
| **Body — point 2** | 3:00–5:00 | Chapter marker at the transition. Same overlay rotation. | Chapter marker, then Captions, Stat |
| **Body — point 3** | 5:00–7:00 | Chapter marker. One pull quote for the most shareable insight. | Chapter marker, Pull quote |
| **CTA / close** | 7:00–end | Full-screen composition beat (dark void). Ember CTA card. Speaker close VO underneath or before. | Full-screen composition |

### The overlay rotation rule

Within any body section:
1. Captions run continuously
2. Stat callout fires on a spoken number (1 per major point)
3. Pull quote fires on the key claim (1 per section)
4. Never two non-caption overlays simultaneously

### Shorter formats

| Format | Hook | Body | CTA |
| --- | --- | --- | --- |
| 60s YouTube Short | 0–8s (no lower third) | 8–50s (captions + 1 stat max) | 50–60s (1 pull quote as CTA) |
| 3-min explainer | 0–20s | 20s–2:40 (2 points, 1 stat each) | 2:40–3:00 (full-screen or pull quote) |

### Color assignment by act

- Hook: no overlays, captions only
- Body/infrastructure points: Steel accents in stats, Copper labels
- Body / resolution moments: Ember underlines stats, Ember emphasizes words in captions
- CTA: Ember dominant

---

## 2 · The Overlay Vocabulary

### 2.1 Overlay types at a glance

| Type | When it fires | Key constraint |
| --- | --- | --- |
| **Lower third** | 0:30–1:00, once per video | Must exit before first main argument |
| **Stat callout** | When a number/metric is spoken | One per major point, right or center, never on speaker's face |
| **Pull quote** | On the most shareable claim in a section | One per section, left-anchored or centered |
| **Chapter marker** | Between major topics | Brief (2.5–3s), horizontally centered, pill-shaped — always `top: 48px` (top of frame), never vertically centered |

> **Talking-head spatial rule:** The speaker's face occupies the vertical center of the frame. Do not place any overlay card at `top: 50%` or equivalent mid-frame vertical position. Safe zones: top edge (chapter markers), top-left corner (pull quotes), top-right (stat callouts), bottom-left (lower thirds). Horizontal centering is always fine; vertical centering is never safe in talking-head compositions.
| **Kinetic captions** | Always | Never off. Word-by-word. Bottom-centered. |

### 2.2 Motion vocabulary for overlays

| Move | What it does | GSAP recipe |
| --- | --- | --- |
| **Card slide-up** | Lower third enters from below | `tl.to(card, { y: 0, autoAlpha: 1, duration: 0.6, ease: 'power3.out' })` from `{ y: 40, autoAlpha: 0 }` |
| **Stat pop** | Stat callout appears with slight scale settle | `tl.to(card, { scale: 1, autoAlpha: 1, duration: 0.4, ease: 'back.out(1.2)' })` from `{ scale: 0.92, autoAlpha: 0 }` |
| **Ember underline draw** | Line draws under the stat number | `tl.from('.ember-line', { scaleX: 0, duration: 0.3, ease: 'power2.out', transformOrigin: 'left' }, '+=0.15')` |
| **Pull quote slide** | Pull quote enters from left | `tl.to(card, { x: 0, autoAlpha: 1, duration: 0.7, ease: 'power3.out' })` from `{ x: -40, autoAlpha: 0 }` |
| **Chapter pill** | Chapter marker scales in | `tl.to(pill, { scale: 1, autoAlpha: 1, duration: 0.5, ease: 'expo.out' })` from `{ scale: 0.94, autoAlpha: 0 }` |
| **Word reveal** | Captions reveal word by word | `gsap.from('.word', { y: 14, autoAlpha: 0, duration: 0.22, ease: 'power3.out', stagger: 0.16 })` |
| **Ember word flash** | Emphasis word renders in Ember | Render in `color: #FF6A1A` — appears on the same word reveal tween as normal words |
| **Card exit fade** | Any card exits cleanly | `tl.to(card, { autoAlpha: 0, duration: 0.35, ease: 'power2.in' })` |
| **Stat exit lift** | Stat callout exits with slight upward drift | `tl.to(card, { y: -10, autoAlpha: 0, duration: 0.35, ease: 'power2.in' })` |
| **Ember pulse** | Full-screen beat: radial glow fires at decision moment | `tl.to(ember, { opacity: 0.12, duration: 0.4, ease: 'power2.out' }).to(ember, { opacity: 0.07, duration: 1.2, ease: 'sine.inOut' })` |
| **Amber whip** | Full-screen beat: tinted streak masks the cut | `gsap.fromTo(streak, { xPercent: -150 }, { xPercent: 250, duration: 0.4, ease: 'power3.in' })` |

### 2.3 Color rules for overlays

White-footage context inverts the standard color usage. This is the source of most first-attempt failures.

| Context | Allowed colors | Forbidden |
| --- | --- | --- |
| **Directly on white footage** | Ember `#FF6A1A` at 48px+, Deep Void `#06060A` at 40px+ | Everything else |
| **Inside dark overlay card** | Soft White, Silver, Copper (32px+), Steel (32px+), Ember | Ash (too subtle) |
| **Caption pill** | Soft White text on `rgba(6,6,10,0.80)` pill | Steel, Silver, Pewter on pill |
| **Full-screen void beat** | Full palette applies | — |

### 2.4 Typography at video scale

These are minimums for a 1920×1080 composition. Going below them means the element serves no communication purpose.

| Element | Minimum | Why |
| --- | --- | --- |
| Captions | 36px | Read at normal viewing distance on phone |
| Card body text | 40px | Readable within a 2-second overlay hold |
| Card labels | 32px | Labels must register instantly |
| Stat numbers | 72px | The number is the message — it must dominate |
| Pull quotes | 52px | Must be readable before the card exits |
| Chapter headings | 48px | Read in under 1 second |
| Lower third name | 52px | Viewer connects name to face in the first hold |

Source Serif 4 weight 400 throughout. The italic variant carries pull quotes and Ember emphasis words. Plus Jakarta Sans for all labels, captions, and body.

### 2.5 Pacing discipline

**Overlay timing:**
- Lower third entry: within the first 30 seconds, after the hook
- Stat callout: fire within 0.5s of the spoken number landing
- Pull quote: fire within 1s of the claim being fully stated
- Chapter marker: fire on the spoken transition phrase, not before
- Caption reveal stagger: 0.16s per word — faster feels rushed, slower feels sluggish

**Hold durations:**
- Lower third: 4–5 seconds
- Stat callout: spoken duration, minimum 2.5 seconds
- Pull quote: spoken duration + 1 second
- Chapter marker: 2.5–3 seconds
- Final CTA full-screen beat: 5+ seconds of stillness

**The silence rule:** Never animate an overlay exit while the speaker is mid-sentence. Cards must exit during natural spoken pauses — breath, comma, or end of point. If the speaker never pauses, the card holds until the section ends.

### 2.6 Full-screen composition beats

These are separate from overlay beats. They use the deep void canvas and apply to intro sequences, CTA outros, and major act transitions.

For the full vocabulary of full-screen beats (ember pulse, steel trace, copper marks, kinetic serif, void breathe, amber whip), see the motion vocabulary in the original full-screen section. The pacing rules for full-screen beats (1–2s per beat, no dead air over 1s) still apply.

The key difference: full-screen beats are fully controlled compositions. Overlay beats are time-locked to the video clip underneath.

### 2.7 Audio

| Layer | Volume | Role |
| --- | --- | --- |
| Speaker (talking head) | `1.0` | Primary — drives all timing |
| Underscore (warm ambient pad) | `0.10–0.12` | Nearly invisible. Warmth only. |
| Overlay SFX (soft settle click) | `0.15` | Optional. Short tail. |

Music-free is a valid and often better choice. The speaker's voice is the soundtrack.

---

## 3 · Building Overlays in HyperFrames — Concrete Recipes

### 3.1 Project structure for talking-head video

```
hihnala-video/
├── index.html                    ← root: video clip + overlay sub-comps chained
├── compositions/
│   ├── 00-intro-beat.html        ← full-screen void beat (optional cold open)
│   ├── 01-lower-third.html       ← lower third sub-comp
│   ├── 02-captions-act1.html     ← captions for act 1 (or use body-level siblings)
│   ├── 03-stat-callout-a.html    ← stat callout, point 1
│   ├── 04-pull-quote-a.html      ← pull quote, point 1
│   ├── 05-chapter-2.html         ← chapter marker
│   ├── 06-stat-callout-b.html    ← stat callout, point 2
│   ├── 07-pull-quote-b.html      ← pull quote, point 2
│   └── 08-cta-outro.html         ← full-screen ember CTA
└── assets/
    ├── brand-tokens.css
    ├── talking-head.mp4           ← the raw footage
    ├── hihnala-logo.jpg
    └── ambient-pad.mp3
```

The talking-head video clip goes in `index.html` as the base layer (track-index 0). All overlay sub-comps layer above it (track-index 2+).

### 3.2 Lower third recipe

```html
<!-- compositions/01-lower-third.html -->
<template id="lower-third-template">
  <div data-composition-id="lower-third"
       data-start="0"
       data-duration="8"
       data-width="1920" data-height="1080">

    <div class="lt-card">
      <div class="lt-copper-rule"></div>
      <div class="lt-name">Markku Hihnala</div>
      <div class="lt-role">AI Strategy & Implementation</div>
    </div>

  </div>
</template>

<style>
[data-composition-id="lower-third"] .lt-card {
  position: absolute;
  left: 72px; bottom: 80px;
  width: 560px;
  background: rgba(6, 6, 10, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 12px;
  padding: 28px 36px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  opacity: 0; visibility: hidden;
}

[data-composition-id="lower-third"] .lt-copper-rule {
  width: 40px; height: 2px;
  background: #D4892F;
  margin-bottom: 14px;
}

[data-composition-id="lower-third"] .lt-name {
  font-family: 'Source Serif 4', serif;
  font-size: 52px; font-weight: 400;
  color: #F5F5F7;
  line-height: 1.1;
  margin-bottom: 8px;
}

[data-composition-id="lower-third"] .lt-role {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 34px; font-weight: 400;
  color: #CDCDD4;
}
</style>

<script>
const SLOT = 8;
const tl = gsap.timeline({ paused: true });

// Entry at t=0.5 (give the footage half a second to establish)
tl.to('.lt-card', { autoAlpha: 1, y: 0, duration: 0.6, ease: 'power3.out' }, 0.5);

// Exit at t=5.5 (after ~5 second hold)
tl.to('.lt-card', { autoAlpha: 0, duration: 0.4, ease: 'power2.in' }, 5.5);

// Law #10
tl.to({}, { duration: SLOT }, 0);
window.__timelines['lower-third'] = tl;
</script>
```

### 3.3 Stat callout recipe

```html
<!-- compositions/03-stat-callout-a.html -->
<template id="stat-callout-a-template">
  <div data-composition-id="stat-callout-a"
       data-start="0"
       data-duration="7"
       data-width="1920" data-height="1080">

    <div class="stat-card">
      <div class="stat-label">AVERAGE AI PROJECT</div>
      <div class="stat-number">18<span class="stat-unit">mo</span></div>
      <div class="stat-ember-line"></div>
      <div class="stat-context">before first business result</div>
    </div>

  </div>
</template>

<style>
[data-composition-id="stat-callout-a"] .stat-card {
  position: absolute;
  right: 96px; top: 50%;
  transform: translateY(-50%);
  width: 420px;
  background: rgba(6, 6, 10, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 12px;
  padding: 32px 40px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  opacity: 0; visibility: hidden;
}

[data-composition-id="stat-callout-a"] .stat-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 22px; font-weight: 500;
  letter-spacing: 0.08em;
  color: #D4892F;
  text-transform: uppercase;
  margin-bottom: 12px;
}

[data-composition-id="stat-callout-a"] .stat-number {
  font-family: 'Source Serif 4', serif;
  font-size: 88px; font-weight: 400;
  color: #F5F5F7;
  line-height: 1;
}

[data-composition-id="stat-callout-a"] .stat-unit {
  font-size: 48px;
  color: #CDCDD4;
}

[data-composition-id="stat-callout-a"] .stat-ember-line {
  width: 0%; height: 3px;
  background: #FF6A1A;
  margin: 16px 0;
  transform-origin: left;
}

[data-composition-id="stat-callout-a"] .stat-context {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 28px; font-weight: 400;
  color: #8E8E99;
  line-height: 1.3;
}
</style>

<script>
const SLOT = 7;
const tl = gsap.timeline({ paused: true });

// Entry at t=0.3
tl.to('.stat-card', { scale: 1, autoAlpha: 1, duration: 0.4, ease: 'back.out(1.2)' }, 0.3);

// Ember line draws in after number lands
tl.to('.stat-ember-line', { width: '60%', duration: 0.3, ease: 'power2.out' }, 0.7);

// Exit at t=5.8
tl.to('.stat-card', { y: -10, autoAlpha: 0, duration: 0.35, ease: 'power2.in' }, 5.8);

// Law #10
tl.to({}, { duration: SLOT }, 0);
window.__timelines['stat-callout-a'] = tl;
</script>
```

### 3.4 Pull quote recipe

```html
<!-- compositions/04-pull-quote-a.html -->
<template id="pull-quote-a-template">
  <div data-composition-id="pull-quote-a"
       data-start="0"
       data-duration="9"
       data-width="1920" data-height="1080">

    <div class="pq-card">
      <div class="pq-accent-bar"></div>
      <div class="pq-text">
        Most AI implementations fail before they start — not from bad tools, but from skipped strategy.
      </div>
    </div>

  </div>
</template>

<style>
[data-composition-id="pull-quote-a"] .pq-card {
  position: absolute;
  left: 72px; bottom: 120px;
  width: 760px;
  background: rgba(6, 6, 10, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 12px;
  padding: 32px 40px 32px 52px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  display: flex; align-items: flex-start; gap: 20px;
  opacity: 0; visibility: hidden;
}

[data-composition-id="pull-quote-a"] .pq-accent-bar {
  width: 4px; min-height: 100%;
  background: #FF6A1A;
  border-radius: 2px;
  flex-shrink: 0;
  align-self: stretch;
}

[data-composition-id="pull-quote-a"] .pq-text {
  font-family: 'Source Serif 4', serif;
  font-size: 52px; font-weight: 400; font-style: italic;
  color: #CDCDD4;
  line-height: 1.35;
}
</style>

<script>
const SLOT = 9;
const tl = gsap.timeline({ paused: true });

// Entry
tl.to('.pq-card', { x: 0, autoAlpha: 1, duration: 0.7, ease: 'power3.out' }, 0.4);

// Exit at t=7.5
tl.to('.pq-card', { autoAlpha: 0, duration: 0.4, ease: 'sine.in' }, 7.5);

// Law #10
tl.to({}, { duration: SLOT }, 0);
window.__timelines['pull-quote-a'] = tl;
</script>
```

### 3.5 Chapter marker recipe

```html
<!-- compositions/05-chapter-2.html -->
<template id="chapter-2-template">
  <div data-composition-id="chapter-2"
       data-start="0"
       data-duration="5"
       data-width="1920" data-height="1080">

    <div class="ch-pill">
      <div class="ch-label">PART 2</div>
      <div class="ch-heading">The Implementation Gap</div>
    </div>

  </div>
</template>

<style>
[data-composition-id="chapter-2"] .ch-pill {
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  background: rgba(6, 6, 10, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 50px;
  padding: 24px 48px;
  text-align: center;
  white-space: nowrap;
  opacity: 0; visibility: hidden;
}

[data-composition-id="chapter-2"] .ch-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 22px; font-weight: 500;
  letter-spacing: 0.10em;
  color: #D4892F;
  text-transform: uppercase;
  margin-bottom: 8px;
}

[data-composition-id="chapter-2"] .ch-heading {
  font-family: 'Source Serif 4', serif;
  font-size: 48px; font-weight: 400;
  color: #F5F5F7;
}
</style>

<script>
const SLOT = 5;
const tl = gsap.timeline({ paused: true });

// Entry
tl.to('.ch-pill', { scale: 1, autoAlpha: 1, duration: 0.5, ease: 'expo.out' }, 0.3);

// Exit at t=3.8
tl.to('.ch-pill', { scale: 0.96, autoAlpha: 0, duration: 0.4, ease: 'power2.in' }, 3.8);

// Law #10
tl.to({}, { duration: SLOT }, 0);
window.__timelines['chapter-2'] = tl;
</script>
```

### 3.6 Kinetic captions (body-level siblings)

Keep captions out of sub-composition timelines. Place in `index.html` as body-level siblings of the master composition div.

```html
<!-- In index.html, outside the main composition div -->
<div class="cap clip" data-start="3.2"  data-duration="2.1"  data-track-index="30">
  Most AI projects take <span class="cap-ember">too long</span>.
</div>
<div class="cap clip" data-start="5.6"  data-duration="2.8"  data-track-index="31">
  Not because the tools are wrong.
</div>
<div class="cap clip" data-start="8.5"  data-duration="3.2"  data-track-index="32">
  Because the <span class="cap-ember">strategy</span> was skipped.
</div>
```

```css
.cap {
  position: absolute;
  bottom: 64px; left: 50%;
  transform: translateX(-50%);
  padding: 10px 24px;
  border-radius: 50px;
  background: rgba(6, 6, 10, 0.80);
  border: 1px solid rgba(255, 255, 255, 0.06);
  font: 500 36px/1.3 'Plus Jakarta Sans', sans-serif;
  color: #F5F5F7;
  white-space: nowrap;
}

.cap-ember {
  color: #FF6A1A;
}
```

Word-by-word reveals require splitting caption text into individual word `<span>` elements and applying stagger GSAP reveals inside `index.html` script. Each caption element appears at its `data-start` via the clip system — the word-reveal animation runs within that window.

### 3.7 Full-screen CTA outro (dark void beat)

```html
<!-- compositions/08-cta-outro.html -->
<template id="cta-outro-template">
  <div data-composition-id="cta-outro"
       data-start="0"
       data-duration="12"
       data-width="1920" data-height="1080">

    <!-- Layer 0: void background (just body background) -->
    <!-- Layer 1: ember ambient -->
    <div class="ember-ambient"></div>
    <!-- Layer 2: vignette -->
    <div class="vignette"></div>

    <!-- Layer 3: CTA content -->
    <div class="cta-wrap">
      <div class="cta-eyebrow">READY TO START</div>
      <div class="cta-heading">Book a Discovery Call</div>
      <div class="cta-url">hihnala.com</div>
    </div>

    <!-- Layer 4: logo -->
    <img class="cta-logo" src="../assets/hihnala-logo.jpg" alt="Hihnala">

  </div>
</template>

<style>
body { background: #06060A; }

[data-composition-id="cta-outro"] .ember-ambient {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 55% 40% at 50% 60%,
    rgba(255,106,26,0.10) 0%, rgba(6,6,10,0) 70%);
}

[data-composition-id="cta-outro"] .vignette {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse at center, transparent 30%, #040408 95%);
}

[data-composition-id="cta-outro"] .cta-wrap {
  position: absolute; left: 50%; top: 45%;
  transform: translate(-50%, -50%);
  text-align: center;
  opacity: 0; visibility: hidden;
}

[data-composition-id="cta-outro"] .cta-eyebrow {
  font: 500 22px/1 'Plus Jakarta Sans', sans-serif;
  letter-spacing: 0.12em;
  color: #D4892F;
  text-transform: uppercase;
  margin-bottom: 20px;
}

[data-composition-id="cta-outro"] .cta-heading {
  font: 400 72px/1.1 'Source Serif 4', serif;
  color: #F5F5F7;
  margin-bottom: 24px;
}

[data-composition-id="cta-outro"] .cta-url {
  font: 400 40px/1 'Plus Jakarta Sans', sans-serif;
  color: #FF6A1A;
}

[data-composition-id="cta-outro"] .cta-logo {
  position: absolute; bottom: 60px; right: 72px;
  width: 80px; height: 80px; border-radius: 8px;
  filter: drop-shadow(0 0 20px rgba(255,106,26,0.35));
  opacity: 0; visibility: hidden;
}
</style>

<script>
const SLOT = 12;
const tl = gsap.timeline({ paused: true });

// Void breathe
gsap.to('.ember-ambient', { opacity: 0.7, duration: 4, repeat: -1, yoyo: true, ease: 'sine.inOut' });

// CTA content enters
tl.to('.cta-wrap', { autoAlpha: 1, y: 0, duration: 0.8, ease: 'power3.out' }, 1.0);
tl.to('.cta-logo', { autoAlpha: 1, duration: 0.6, ease: 'power2.out' }, 1.4);

// Ember pulse at t=2s
tl.to('.ember-ambient', { opacity: 0.14, duration: 0.4, ease: 'power2.out' }, 2.0);
tl.to('.ember-ambient', { opacity: 0.08, duration: 1.5, ease: 'sine.inOut' }, 2.4);

// Hold for 5+ seconds — the longest shot in the piece
// Law #10
tl.to({}, { duration: SLOT }, 0);
window.__timelines['cta-outro'] = tl;
</script>
```

---

## 4 · HyperFrames Technical Recipes

### 4.1 The timeline-padding rule (Law #10)

Every sub-composition ends with a no-op anchor:

```javascript
tl.to({}, { duration: SLOT_DURATION }, 0);
window.__timelines['<data-composition-id>'] = tl;
```

Diagnose missing timelines:
```javascript
const p = document.querySelector('hyperframes-player');
const iw = p.shadowRoot.querySelector('iframe').contentWindow;
Object.fromEntries(Object.entries(iw.__timelines).map(([k,v]) =>
  [k, +v.duration().toFixed(4)]));
```

Any `timeline.duration() < data-duration` value is a black-frame risk.

### 4.2 Velocity-matched easing at beat seams

When an entry tween hands off to a linear hold, match end-velocity to avoid a perceived stall. For entry going 0 → 1 over 0.9s with desired end-velocity `v = 0.194`:

```javascript
const entryEase = (t) => -0.806 * t * t + 1.806 * t;
tl.to(card, { z: -50, duration: 0.9, ease: entryEase }, 0);
tl.to(card, { z: -80, duration: 0.65, ease: 'none' }, 0.9);
```

### 4.3 GSAP proxy pattern for Canvas 2D

```javascript
const proxy = { time: 0 };
tl.to(proxy, { time: DURATION, duration: DURATION, ease: 'none',
  onUpdate: () => renderAtTime(proxy.time) }, 0);
```

No `Math.random()` / `Date.now()` inside. Use harmonic-sin hashes for determinism.

### 4.4 Tall-canvas camera pan

```css
.viewport { width: 1920px; height: 1080px; overflow: hidden; }
.canvas   { width: 1920px; height: 5400px; position: absolute; top: 0; left: 0; }
```

```javascript
tl.to(canvas, { y: -1080, duration: 1.2, ease: 'power2.inOut' }, 1.8);
```

### 4.5 Video poster + lastframe bracketing

```html
<img id="poster"    src="assets/poster.jpg">
<video id="clip"    src="assets/clip.mp4" data-start="7.1" data-duration="8.94" data-track-index="5" muted></video>
<img id="lastframe" src="assets/lastframe.jpg">
```

```javascript
tl.set('#poster',    { display: 'none' }, 7.1);
tl.set('#lastframe', { opacity: 1 }, 16.04);
```

```bash
ffmpeg -y -ss 0       -i clip.mp4 -frames:v 1 -q:v 2 poster.jpg
ffmpeg -y -sseof -0.04 -i clip.mp4 -frames:v 1 -q:v 2 lastframe.jpg
```

### 4.6 Tween-comment convention

Every entry/exit tween names its matching tween in the adjacent beat:

```javascript
// ENTRY — y and blur match the outgoing "hook" beat's exit values
gsap.set(wrap, { filter: 'blur(18px)', y: 40 });
tl.to(wrap, { filter: 'blur(0px)', y: 0, duration: 0.35, ease: 'power2.out' }, 0);

// EXIT at t=5.8 — matches the incoming "stat" beat's x: -40 entry
tl.to(wrap, { x: -40, autoAlpha: 0, duration: 0.35, ease: 'power2.in' }, 5.8);
```

If you can't name the matching tween, you haven't designed the seam.

---

## 5 · Sub-Composition Gotchas

Hard-won rules from production. Every one of these causes silent failures or broken output.

### 5.1 Container sizing: `data-width`/`data-height`, not CSS `inset: 0`

The container div in `index.html` that loads a sub-composition must carry explicit dimension attributes. CSS `inset: 0` handles visual stacking but does not substitute for the data attributes.

```html
<!-- CORRECT -->
<div id="act1-comp"
     data-composition-id="act1"
     data-composition-src="compositions/01-act1.html"
     data-start="30" data-duration="29" data-track-index="2"
     data-width="1920" data-height="1080"></div>

<!-- WRONG — missing data-width/data-height -->
<div style="inset: 0; position: absolute;" ...></div>
```

### 5.2 CSS selectors: `[data-composition-id="..."]`, not `#id`

The template inner div has no `id` attribute — `data-composition-id` is the identifier. Ignore the linter suggestion to switch to `#id` selectors for sub-compositions.

```css
/* CORRECT */
[data-composition-id="act1"] .stat-card { ... }

/* WRONG — inner div has no id, matches nothing */
#act1 .stat-card { ... }
```

The linter warning is a style preference, not a bug. Leave as warnings.

### 5.3 Template inner div must have `data-start="0"` and `data-duration`

Without both attributes, the sub-composition silently fails to load — no error, just nothing visible.

```html
<template id="act1-template">
  <div data-composition-id="act1"
       data-start="0"        <!-- REQUIRED -->
       data-duration="29"    <!-- REQUIRED -->
       data-width="1920" data-height="1080">
    ...
  </div>
</template>
```

### 5.4 `class="clip"` does nothing inside sub-compositions

`class="clip"` with `data-start` / `data-duration` / `data-track-index` is a root-composition-only mechanism. Inside a sub-composition, every element with `class="clip"` is treated as a plain `div` — all elements appear simultaneously the moment the sub-composition renders.

**Fix: use GSAP ****`autoAlpha`**** for all show/hide inside sub-compositions.**

```css
/* Start all overlay elements hidden in CSS */
[data-composition-id="my-comp"] .overlay-element {
  opacity: 0;
  visibility: hidden;
}
```

```javascript
const tl = gsap.timeline({ paused: true });

// Show at t=2.0
tl.to('.overlay-element', { autoAlpha: 1, y: 0, duration: 0.5, ease: 'power3.out' }, 2.0);

// Hide at t=5.5
tl.set('.overlay-element', { autoAlpha: 0 }, 5.5);
```

### 5.5 Glow / ember elements: opacity-only, not gradient animation

GSAP gradient interpolation produces hard swaps, not smooth transitions. For glow elements, animate `opacity` only — never `backgroundImage` or gradient stops.

```css
.ember-pulse {
  background: radial-gradient(ellipse 55% 40% at 50% 58%,
    rgba(255,106,26,0.12) 0%, rgba(6,6,10,0) 70%);
  opacity: 0; visibility: hidden;
}
```

```javascript
tl.to('.ember-pulse', { autoAlpha: 1, duration: 0.4, ease: 'power2.out' }, 2.0);
tl.to('.ember-pulse', { opacity: 0.5, duration: 1.5, ease: 'sine.inOut' }, 2.4);
tl.set('.ember-pulse', { autoAlpha: 0 }, 4.5);
```

---

## 6 · Pre-flight Checklist

### Overlay beats
- [ ] Container in `index.html` has `data-width="1920" data-height="1080"`
- [ ] Template inner div has `data-start="0"` and `data-duration`
- [ ] CSS uses `[data-composition-id="..."]` selectors throughout
- [ ] No `class="clip"` on inner elements — removed entirely
- [ ] All overlay elements start with `opacity: 0; visibility: hidden` in CSS
- [ ] Visibility controlled entirely via GSAP `autoAlpha`
- [ ] No overlay covers the speaker's face
- [ ] No two non-caption overlays visible simultaneously
- [ ] No text below 32px anywhere in the composition
- [ ] No Steel, Silver, Pewter, or Ash text directly on white footage
- [ ] All overlay exits timed to spoken pauses, not mid-sentence
- [ ] Captions active throughout

### Full-screen beats
- [ ] Average scene length ≤ 2s in mid-section
- [ ] Every transition uses motion (amber whip, ember flash, slide — never a hard fade)
- [ ] One ember moment per section
- [ ] Void and vignette present in every scene
- [ ] Grain overlay on every scene
- [ ] CTA holds 5+ seconds

### Both types
- [ ] Every sub-composition timeline ends with `tl.to({}, { duration: SLOT }, 0)`
- [ ] All tween end-times snap to multiples of `1/fps` (at 30fps: 0.0333, 0.0667, 0.1...)
- [ ] Ran the timeline-duration diagnostic — no `timeline.duration() < data-duration` gaps
- [ ] Visual verification done — extracted frames, confirmed no text overflow, no broken transitions

---

## 7 · The "What Would Hihnala Do?" Test

1. **Could this overlay be removed without losing the argument?** If yes, remove it.
2. **Is the text large enough to read in 2 seconds?** If you have to squint, it fails.
3. **Is this color appearing on white footage without a dark card behind it?** Remove it.
4. **Does the card exit compete with what the speaker is saying?** Delay the exit.
5. **Are there two overlay cards visible at once?** Collapse to one.
6. **Are captions on?** They are always on.
7. **Is the Ember accent carrying a meaning here, or just filling space?** If the latter, remove it.
8. **Does the speaker's face remain visible?** If the card covers it, reposition.
9. **What does the viewer see in the first 8 seconds?** If the answer is "nothing but the speaker talking," the cold open is working — add a chapter marker or pull quote only after the hook lands.
10. **Does the CTA hold for at least 5 seconds?** If not, extend it.

---

## 8 · Anti-patterns

- No Steel, Silver, Pewter, or Ash text directly on white-background footage — ever.
- No text below 32px in any video composition at any point.
- No multiple overlay cards active simultaneously.
- No `class="clip"` inside sub-compositions — it has no effect and creates confusion.
- No CSS `#id` selectors inside sub-compositions — the inner div has no id.
- No missing `data-start="0"` on the template inner div — the comp silently fails.
- No missing `data-width`/`data-height` on the container div — use CSS inset for stacking, data attributes for sizing.
- No animating `backgroundImage` or gradient stops for ember/glow elements — animate `opacity` only.
- No `Math.random()` / `Date.now()` inside render loops — use harmonic hashes.
- No overlay exit mid-sentence — wait for a spoken pause.
- No CTA shorter than 5 seconds. The viewer needs time to register the information.
- No hype words in any overlay or caption: revolutionary, cutting edge, disruptive, seamless, unleash, leverage, next-gen, game-changer.

---

## 9 · GSAP Reference

**Easings by purpose:**

| Purpose | Ease | Typical duration |
| --- | --- | --- |
| Overlay card entry | `power3.out` | 0.5–0.7s |
| Stat callout pop | `back.out(1.2)` | 0.35–0.45s |
| Chapter marker entry | `expo.out` | 0.4–0.5s |
| Word reveal | `power3.out` | 0.20–0.25s per word |
| Card exit | `power2.in` | 0.35–0.4s |
| Stat exit lift | `power2.in` | 0.3–0.35s |
| Ember underline draw | `power2.out` | 0.25–0.35s |
| Ember settle | `sine.inOut` | 0.8–1.5s |
| Void breathe (repeat) | `sine.inOut` yoyo | 3–5s, `repeat: -1` |
| Full-screen entry | `power3.out` | 0.5–0.9s |
| Full-screen camera pan | `power2.inOut` | 1.2–2.3s |
| Amber whip | `power3.in` | 0.35–0.45s |

**Stagger values:**
- Word-by-word captions: `0.16–0.18s`
- Copper mark appear: `0.06–0.08s`
- Particle drift: `each: 0.5–0.8, from: 'random'`

Never use `gsap.defaults()` — every tween declares its ease and duration explicitly.

**Timeline skeleton (every sub-composition):**

```javascript
(() => {
  const SLOT = /* data-duration value */;
  const tl = gsap.timeline({ paused: true });

  // … tweens …

  tl.to({}, { duration: SLOT }, 0);  // Law #10
  window.__timelines['<data-composition-id>'] = tl;
})();
```

---

## 10 · TL;DR

> **One overlay at a time, dark cards on white footage, minimum 36px on everything, captions always on, one ember accent per card, hold every card through the spoken moment, exit in silence — and every timeline fills its slot.**
