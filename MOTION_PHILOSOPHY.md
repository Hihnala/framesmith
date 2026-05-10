# MOTION PHILOSOPHY — Hihnala

*Quiet Power in Motion. Every frame earns its place.*

Read this before starting any composition. Re-read the Laws before brainstorming any new scene.

---

## 0 · The 10 Laws

1. **One idea per beat. Cut fast.** Each scene lands one concept and moves on. If a scene says two things, split it. Target 1.0-2.0 seconds per beat in the mid-section.

2. **The void is the canvas.** Deep Void (`#06060A`) or Abyss (`#040408`) fills 80-90% of every frame. Negative space is the design. Color earns its place by carrying meaning.

3. **Light signals brand.** Ember glow means decision. Steel trace means infrastructure activation. Copper marks mean structure. Nothing glows without a reason assigned to it.

4. **The frame breathes.** Even "still" frames have ambient motion: particle drift, vignette pulse, a slow ember radial shift. Static = death.

5. **Motion blur covers every cut.** Every transition uses directional blur or a streak element. Hard cuts feel cheap. Amber-tinted whip streaks on energy beats. Blur crossfades on brand reveals.

6. **Serif authority.** Source Serif 4 at weight 400 is the compositional voice. It can scale to screen-fill. It can reveal word by word. It never goes bold. Authority comes from scale and contrast, not thickness.

7. **One dominant color per scene.** Follow the psychological order: Steel (infrastructure) → Copper (structure) → Ember (decision). Never invert it within a piece. Mixing Ember and Steel equally in one scene dissolves both.

8. **Hold the hero.** Brand reveals get 1.5-2 seconds of stillness. Final CTA holds 4-6 seconds. Speed earns silence. The outro is the longest single shot in the piece.

9. **One unifying texture across everything.** The Hihnala texture: deep void background + ambient ember radial at the composition's center of gravity + slow particle drift. Present in every scene, even when nearly invisible.

10. **Timelines must fill their slots.** HyperFrames hides a sub-composition the moment `timeline.duration()` is shorter than `data-duration`, producing a black frame flash. Every GSAP timeline ends with `tl.to({}, { duration: SLOT_DURATION }, 0)` as a no-op anchor. Non-negotiable.

---

## 1 · The Hihnala Composition Model

Every Hihnala video follows a three-act structure regardless of length.

**60-second format:**

| Time | Act | What's on screen | Dominant accent |
|------|-----|-----------------|-----------------|
| 0-3s | Opening | Void. Ambient ember radial forms. Serif type reveals word by word. | None (void establishes) |
| 3-15s | Problem / Context | Infrastructure described. Steel traces activate nodes. | Steel |
| 15-45s | Solution (three beats) | Each beat: Copper marks appear first (structure). Ember pulse fires at resolution. | Copper → Ember |
| 45-55s | Outcome | Single serif statement at scale. Ember stage expands. | Ember |
| 55-60s | CTA hold | Brand mark. Contact or URL. Stillness. | Ember (held) |

**30-second format:**

| Time | Act | Dominant accent |
|------|-----|-----------------|
| 0-5s | Hook (one problem sentence, kinetic serif) | None |
| 5-22s | Three solution beats (6 seconds each) | Steel → Copper → Ember |
| 22-30s | CTA hold | Ember |

**15-second format:**

| Time | Act |
|------|-----|
| 0-4s | Problem hook |
| 4-11s | One solution point |
| 11-15s | CTA hold (minimum 4 seconds) |

**Color assignment by act:**
- Opening: void dominates, accent barely present
- Problem/context: Steel (infrastructure, things that exist)
- Solution beats: Copper marks the structure, Ember fires at the resolution
- CTA: Ember only

The rule of three appears naturally in the solution act. Don't force it elsewhere.

---

## 2 · The Visual Vocabulary

### 2.1 Backgrounds (in priority order)

| # | Background | Where it lives | How to build |
|---|-----------|---------------|--------------|
| 1 | **Pure void** | Always | `body { background: #06060A }`. The default. |
| 2 | **Ambient ember radial** | Hero frames, CTA section, impact beats | `radial-gradient(ellipse at 50% 60%, rgba(255,106,26,0.08) 0%, transparent 60%)`. Subtle. Breathes. |
| 3 | **Vignette** | Every scene, always on top | `radial-gradient(ellipse at center, transparent 30%, #040408 95%)`. Non-negotiable. |
| 4 | **Particle drift** | All scenes (barely visible) | 15-25 absolute `<div>` elements, 1-2px, white at 10-20% opacity, GSAP `sine.inOut yoyo repeat`, slow (4-8s per cycle), stagger from random. |
| 5 | **Steel grid (sparse)** | Infrastructure / system beats | Two-axis repeating-linear-gradient at Steel (`rgba(79,109,138,0.06)`), 80px spacing. Never rotated. |
| 6 | **Copper marks** | Structure beats, step reveals | SVG `+` crosshair marks at grid intersections in Copper (`#D4892F` at 40% opacity). Fade in as structure establishes. |
| 7 | **Glass card surface** | Product UI beats, data panels | 4-stop diagonal gradient + `backdrop-filter: blur(14px) saturate(1.12)` + inner highlight. See `DESIGN.md`. |
| 8 | **Ember stage** | CTA, decisive hero moments | Concentrated `radial-gradient` at center, `rgba(255,106,26,0.12)` at peak. Animate opacity 0 → 0.12 → 0.08 (settle). |
| 9 | **Film grain** | Every scene | `npx hyperframes add grain-overlay` or pure CSS three-radial dot pattern. Subtle. Always present. |

No iridescent backgrounds. No conic gradients. No full-screen warm washes.

### 2.2 Type System

Hihnala uses two fonts across all compositions. No exceptions.

**Headings:** Source Serif 4 (Google Fonts), weight 400, optical size axis active.
**Body / UI:** Plus Jakarta Sans (Google Fonts), weight 400 regular / 500 medium for labels.

Three typographic voices:

- **Serif regular** — all headline beats, step titles, compositional anchors
- **Serif italic** — closing statements, pull quotes, brand tagline. Always Silver (`#CDCDD4`).
- **Sans** — body copy, UI labels, captions, meta text

**Text color hierarchy in compositions:**

| Role | Color | Hex |
|------|-------|-----|
| Primary statements | Soft White | `#F5F5F7` |
| Substatements, supporting | Silver | `#CDCDD4` |
| Body, descriptions | Pewter | `#8E8E99` |
| Labels, meta | Ash | `#5A5A66` |
| Section labels (uppercase) | Copper | `#D4892F` |
| CTA emphasis | Ember | `#FF6A1A` |

Hihnala does not use chrome gradients on type. Flat text colors from the hierarchy above. The brand signal comes from the font's authority at scale, not from metallic effects.

**Kinetic type in video:**
- Word-by-word reveals hit harder than character-by-character
- Hero statements can scale to 4-6× their base size as the camera passes through
- Use `clamp()` for base sizes, animate via `scale` — never change `font-size` mid-tween
- Serif italic anchor lines at the close of a beat, in Silver, weight 400

### 2.3 Color Story

| Color | Hex | Meaning | Where |
|-------|-----|---------|-------|
| **Deep Void** | `#06060A` | Canvas / silence | Always dominant |
| **Soft White** | `#F5F5F7` | Primary voice | Headings, key statements |
| **Silver** | `#CDCDD4` | Supporting voice, warmth | Substatements, italic anchor lines |
| **Pewter** | `#8E8E99` | Background voice | Body copy, descriptions |
| **Ember Orange** | `#FF6A1A` | Decision / action | One per beat, at the decisive moment |
| **Strategic Steel** | `#4F6D8A` | Infrastructure / systems | Context beats, network traces |
| **Structural Copper** | `#D4892F` | Structure / labels | Step markers, grid registration |

**Discipline:** assign a color before placing it. Ask what role it plays in this beat. If the answer is "it looks nice," remove it.

### 2.4 Motion Vocabulary

The moves you'll use across every Hihnala composition:

| Move | What it does | GSAP recipe |
|------|-------------|-------------|
| **Ember pulse** | A warm radial glow expands at a decisive moment, then settles | `tl.to(ember, { '--glow-opacity': 0.12, duration: 0.4, ease: 'power2.out' }).to(ember, { '--glow-opacity': 0.07, duration: 1.2, ease: 'sine.inOut' })` |
| **Steel trace** | Energy travels along a path to activate a system node | SVG `stroke-dashoffset` from `length` to `0`, `power2.inOut`, then `tl.to(node, { boxShadow: '0 0 24px rgba(79,109,138,0.5)' })` |
| **Copper mark** | Registration marks appear at structural moments | `gsap.from('.copper-mark', { opacity: 0, scale: 0.6, duration: 0.3, ease: 'back.out(1.4)', stagger: 0.06 })` |
| **Serif scale** | Source Serif 4 grows 1× → 4-6×, camera passes through | `tl.fromTo(text, { scale: 1, opacity: 1 }, { scale: 5, opacity: 0, duration: 1.2, ease: 'power2.in' })` |
| **Word cascade** | Words reveal with slight upward motion and scale | `tl.from('.word', { y: 24, opacity: 0, scale: 0.92, duration: 0.5, ease: 'power3.out', stagger: 0.3 })` |
| **Void breathe** | Vignette opacity cycles to keep still frames alive | `gsap.to(vignette, { opacity: 0.85, duration: 4, repeat: -1, yoyo: true, ease: 'sine.inOut' })` |
| **Amber whip** | Ember-tinted light streak masks the cut | `gsap.fromTo(streak, { xPercent: -150 }, { xPercent: 250, duration: 0.4, ease: 'power3.in' })` — fire at the cut |
| **Particle drift** | Slow ambient motion in the void | `gsap.to(particles, { y: '-=12', duration: 5, repeat: -1, yoyo: true, ease: 'sine.inOut', stagger: { each: 0.6, from: 'random' } })` |
| **Card materialize** | Double-bezel card rises from 0.95 scale with ember glow | `tl.from(card, { scale: 0.95, opacity: 0, duration: 0.6, ease: 'power2.out' }).from(glow, { opacity: 0, duration: 0.8 }, '<0.1')` |
| **Glass slide** | Glass panel enters from below, blur activates | `tl.from(panel, { y: 60, opacity: 0, duration: 0.8, ease: 'power3.out' })` with `backdrop-filter` already set |
| **Ember outro** | CTA section: ember radial expands, settles, holds | Animate `--glow-opacity` 0 → 0.14, settle to 0.09, then hold for 4+ seconds |
| **Color recolor (no cut)** | Same composition, accent shifts via CSS variables | `tl.to(':root', { '--accent': '#4F6D8A', duration: 0.6, ease: 'power2.inOut' })` |
| **Energy pulse along path** | SVG edge "activates" a network node | `stroke-dasharray + stroke-dashoffset` animated 1 → 0. Node lights via `boxShadow` tween at path end. |
| **Hold shimmer** | Subtle glint passes over held logo/type | `npx hyperframes add shimmer-sweep`, set `data-interval` |

**The amber whip** replaces the pure-white whip from generic motion graphics. The tint stays in brand without pulling attention from the transition's job (covering the cut).

### 2.5 Transition Catalog

| Transition | When to use | Approach |
|-----------|-------------|----------|
| **Amber whip** | Default cut between scenes | Custom div + GSAP, or `npx hyperframes add whip-pan` |
| **Ember flash** | Act 1 → Act 2, decisive moments | White-to-ember overlay: `opacity 0 → 0.4 → 0`, 0.5s |
| **Blur crossfade** | Brand reveal, CTA landing | Two layered scenes, opacity cross with `filter: blur(8px)` on exit |
| **Void fade** | Between major acts | Both scenes fade through pure void, 0.6s each |
| **Slide-up reveal** | Product/UI panels, glass cards | `from y: 80px`, `power3.out`, 0.7s |
| **Steel cut-to-build** | Infrastructure scenes | Scene cuts on steel trace peak, new scene builds from same position |
| **Serif dolly** | Hero kinetic-type beats | `scale: 1 → 5, opacity: 1 → 0, power2.in` |
| **Hard cut on action** | When the whip streak peaks | Align `data-start` with streak mid-frame |

### 2.6 Pacing Discipline

- **Default scene length:** 1.0-2.0 seconds mid-section. Opening can hold 2-3s to let void establish.
- **New visual element:** every 0.3-0.6 seconds within a scene. No dead air over 1 second mid-piece.
- **Word-reveal stagger:** 0.25-0.35 seconds per word for narrative reads. 0.5-0.6 seconds for single-word emphasis.
- **Whip transition duration:** 0.35-0.45 seconds. Faster feels glitchy.
- **Hold durations:**
  - Brand mark reveal: 1.5-2 seconds
  - Act transition beat: 0.8-1.2 seconds
  - Final CTA card: 4-6 seconds (the longest single shot in the piece)
- **The breathing rule:** every 6-8 seconds of kinetic density, give the viewer a 1-second rest beat. The ember radial settling counts as a rest.

### 2.7 Audio Defaults

| Layer | Volume | Role |
|-------|--------|------|
| Voiceover | `1.0` | Primary, drives timing |
| Underscore (warm ambient pad) | `0.12-0.15` | Barely present. Sets mood. |
| SFX (settle clicks, soft whooshes) | `0.18` | Tails may bleed into next beat |

Wire as sibling `<audio>` elements in root composition. Music-free is valid. Pad-only is the default.

---

## 3 · Building in HyperFrames — Concrete Recipes

### 3.1 Composition shell

```
project-name/
├── index.html
├── compositions/
│   ├── 01-opening.html
│   ├── 02-problem.html
│   ├── 03-solution-a.html
│   ├── 04-solution-b.html
│   ├── 05-solution-c.html
│   ├── 06-outcome.html
│   └── 07-cta-outro.html
└── assets/
    ├── brand-tokens.css
    ├── hihnala-logo.jpg
    └── ambient-pad.mp3
```

`index.html` chains compositions via `<template>` + `data-composition-src`.

### 3.2 The void background (base for every scene)

```html
<div class="stage" data-composition-id="...">
  <!-- Layer 0: pure void -->
  <!-- Just body { background: #06060A } — the void is the default -->

  <!-- Layer 1: ambient ember radial (most scenes) -->
  <div class="ember-ambient clip" data-start="0" data-duration="5" data-track-index="0"></div>

  <!-- Layer 2: particle drift -->
  <div class="particles clip" data-start="0" data-duration="5" data-track-index="1"></div>

  <!-- Layer 3: vignette (always on top of bg, below content) -->
  <div class="vignette clip" data-start="0" data-duration="5" data-track-index="9"></div>

  <!-- Layer 4: grain overlay -->
  <div class="grain clip" data-start="0" data-duration="5" data-track-index="10"></div>

  <!-- Content layers go in tracks 2-8 -->
</div>

<style>
body { background: #06060A; }

.ember-ambient {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 60% 40% at 50% 65%,
    rgba(255, 106, 26, 0.08) 0%,
    rgba(255, 106, 26, 0.03) 40%,
    transparent 70%
  );
}

.vignette {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse at center, transparent 30%, #040408 95%);
}
</style>

<script>
// Void breathe — keeps still frames alive
gsap.to('.ember-ambient', {
  opacity: 0.7,
  duration: 4,
  repeat: -1,
  yoyo: true,
  ease: 'sine.inOut'
});

gsap.to('.vignette', {
  opacity: 0.85,
  duration: 5,
  repeat: -1,
  yoyo: true,
  ease: 'sine.inOut'
});
</script>
```

### 3.3 Kinetic serif type opener

```html
<div class="kinetic-serif">
  <span class="word w1">AI</span>
  <span class="word w2">implementation</span>
  <span class="word w3">takes</span>
  <span class="word w4">too</span>
  <span class="word w5 hero">long.</span>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&display=swap');

.word {
  font-family: 'Source Serif 4', serif;
  font-weight: 400;
  font-size: 72px;
  optical-sizing: auto;
  color: #F5F5F7;
  display: block;
}

.hero {
  font-size: 72px;  /* base — GSAP scales it */
  color: #CDCDD4;  /* Silver — carries weight differently */
  font-style: italic;
}
</style>

<script>
const tl = gsap.timeline({ paused: true });

tl.from('.w1', { y: 24, opacity: 0, scale: 0.92, duration: 0.5, ease: 'power3.out' }, 0)
  .from('.w2', { y: 24, opacity: 0, scale: 0.92, duration: 0.5, ease: 'power3.out' }, 0.3)
  .from('.w3', { y: 24, opacity: 0, scale: 0.92, duration: 0.5, ease: 'power3.out' }, 0.55)
  .from('.w4', { y: 24, opacity: 0, scale: 0.92, duration: 0.5, ease: 'power3.out' }, 0.75)
  .from('.w5', { y: 24, opacity: 0, scale: 0.92, duration: 0.5, ease: 'power3.out' }, 0.95)
  // Hero scale — camera passes through the anchor word
  .fromTo('.w5',
    { scale: 1, opacity: 1 },
    { scale: 5, opacity: 0, duration: 1.1, ease: 'power2.in' },
    1.8
  );

window.__timelines['kinetic-serif'] = tl;
</script>
```

### 3.4 Ember pulse event

For decisive moments — a resolution beat, a CTA approach, a key statistic.

```html
<div class="ember-stage"></div>

<style>
.ember-stage {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 50% 35% at 50% 60%,
    rgba(255, 106, 26, var(--glow-opacity, 0)) 0%,
    transparent 70%
  );
}
</style>

<script>
const tl = gsap.timeline({ paused: true });

// Pulse in on the decisive beat
tl.to('.ember-stage', { '--glow-opacity': 0.14, duration: 0.4, ease: 'power2.out' }, 0)
  // Settle — not a flash, a landing
  .to('.ember-stage', { '--glow-opacity': 0.08, duration: 1.2, ease: 'sine.inOut' }, 0.4);

window.__timelines['ember-pulse'] = tl;
</script>
```

### 3.5 Steel energy trace

For infrastructure beats — showing systems connecting, processes linking.

```html
<svg class="network" viewBox="0 0 1920 1080">
  <path id="trace-path" d="M 400,540 Q 760,300 960,540 Q 1160,780 1520,540"
    fill="none"
    stroke="rgba(79,109,138,0.3)"
    stroke-width="1.5"
    stroke-dasharray="800"
    stroke-dashoffset="800"
  />
  <circle class="node" cx="400" cy="540" r="6" fill="#4F6D8A" opacity="0.4"/>
  <circle class="node" cx="960" cy="540" r="6" fill="#4F6D8A" opacity="0.4"/>
  <circle class="node" cx="1520" cy="540" r="6" fill="#4F6D8A" opacity="0.4"/>
</svg>

<script>
const tl = gsap.timeline({ paused: true });

// Trace activates along the path
tl.to('#trace-path', { strokeDashoffset: 0, duration: 1.5, ease: 'power2.inOut' }, 0)
  // Nodes light up as the trace reaches them
  .to('.node:nth-child(2)', {
    opacity: 1,
    filter: 'drop-shadow(0 0 12px rgba(79,109,138,0.7))',
    duration: 0.3,
    ease: 'power2.out'
  }, 0.75)
  .to('.node:nth-child(3)', {
    opacity: 1,
    filter: 'drop-shadow(0 0 12px rgba(79,109,138,0.7))',
    duration: 0.3,
    ease: 'power2.out'
  }, 1.5);

window.__timelines['steel-trace'] = tl;
</script>
```

### 3.6 Amber whip transition

```html
<div class="whip-streak clip"
     data-start="2.8" data-duration="0.45" data-track-index="8"></div>

<style>
.whip-streak {
  position: absolute; top: 50%; left: 0;
  width: 35%; height: 6px;
  background: linear-gradient(90deg,
    transparent,
    rgba(255, 140, 66, 0.9),
    rgba(255, 106, 26, 0.6),
    transparent
  );
  filter: blur(4px);
  transform: translateY(-50%);
}
</style>

<script>
gsap.fromTo('.whip-streak',
  { xPercent: -100, scaleX: 0.6 },
  { xPercent: 250, scaleX: 1.4, duration: 0.45, ease: 'power3.in' }
);
</script>
```

The next scene's `data-start` should land at the streak's peak (around 60% through the streak duration).

### 3.7 Copper structure marks

```html
<div class="copper-marks">
  <div class="mark" style="left: 480px; top: 270px;"></div>
  <div class="mark" style="left: 960px; top: 270px;"></div>
  <div class="mark" style="left: 1440px; top: 270px;"></div>
</div>

<style>
.mark {
  position: absolute;
  width: 16px; height: 16px;
  opacity: 0;
}

.mark::before,
.mark::after {
  content: '';
  position: absolute;
  background: rgba(212, 137, 47, 0.5);
}

/* Horizontal bar */
.mark::before { left: 0; top: 50%; width: 100%; height: 1px; transform: translateY(-50%); }
/* Vertical bar */
.mark::after  { top: 0; left: 50%; height: 100%; width: 1px; transform: translateX(-50%); }
</style>

<script>
const tl = gsap.timeline({ paused: true });

tl.from('.mark', {
  opacity: 0,
  scale: 0.5,
  duration: 0.3,
  ease: 'back.out(1.4)',
  stagger: 0.08
});

window.__timelines['copper-marks'] = tl;
</script>
```

### 3.8 The timeline-padding rule (Law #10)

Every sub-composition ends its timeline with a no-op duration anchor:

```javascript
const tl = gsap.timeline({ paused: true });
// … all your tweens …
tl.to({}, { duration: SLOT_DURATION }, 0);  // anchor: forces timeline.duration() >= SLOT_DURATION
window.__timelines['my-comp'] = tl;
```

HyperFrames sets `visibility: hidden` on the composition the moment `timeline.duration()` falls short of `data-duration`, producing a black frame flash at the beat tail. The anchor tween has zero animation cost. Diagnose with:

```javascript
const p = document.querySelector('hyperframes-player');
const iw = p.shadowRoot.querySelector('iframe').contentWindow;
Object.fromEntries(Object.entries(iw.__timelines).map(([k, v]) =>
  [k, +v.duration().toFixed(4)]));
```

Any value where `timeline.duration() < data-duration` is a black-frame risk.

### 3.9 Velocity-matched easing at beat seams

When an entry tween hands off to a linear hold, derive a custom ease so end-velocity matches the next tween's start-velocity. The eye reads any velocity discontinuity as a stall.

```javascript
// Entry goes 0 → 1 over 0.9s, then holds linearly at −0.123/s for 0.65s.
// Match at seam: p'(1) = 0.194. Quadratic: a = −0.806, b = 1.806.
const entryEase = (t) => -0.806 * t * t + 1.806 * t;

tl.to(card, { z: -50, duration: 0.9, ease: entryEase }, 0);
tl.to(card, { z: -80, duration: 0.65, ease: 'none' }, 0.9);
```

### 3.10 GSAP proxy pattern — Canvas 2D inside a timeline

Drive arbitrary Canvas 2D rendering from a single tween that advances a proxy time value:

```javascript
const proxy = { time: 0 };
tl.to(proxy, {
  time: DURATION,
  duration: DURATION,
  ease: 'none',
  onUpdate: () => renderAtTime(proxy.time)
}, 0);
```

Two rules:
1. Canvas 2D is headless-safe. Live WebGL can stall the render — ship a Canvas 2D fallback keyed off `renderOptions.headless`.
2. No `Math.random()` or `Date.now()` inside. Use seeded PRNGs or harmonic-sin hashes. Renders must be deterministic.

### 3.11 Tall-canvas camera pan

```css
.viewport { width: 1920px; height: 1080px; overflow: hidden; }
.canvas   { width: 1920px; height: 5400px; position: absolute; top: 0; left: 0; }
```

```javascript
tl.to(canvas, { y: 0 }, 0);
tl.to(canvas, { y: -1080, duration: 1.2, ease: 'power2.inOut' }, 1.8);
tl.to(canvas, { y: -3240, duration: 2.1, ease: 'power2.inOut' }, 3.2);
```

Use `power2.inOut` for topic changes. Use `none` for constant-velocity scrolls through related content.

### 3.12 Video poster + lastframe bracketing

```html
<img id="beat-poster"    src="assets/beat-poster.jpg">
<video id="beat-video"   src="assets/beat-clip.mp4"
       data-start="7.1" data-duration="8.94" data-track-index="5" muted></video>
<img id="beat-lastframe" src="assets/beat-lastframe.jpg">
```

```javascript
tl.set('#beat-poster',    { display: 'none' }, 7.1);
tl.set('#beat-lastframe', { opacity: 1 }, 16.04);
```

Generate stills with ffmpeg:
```bash
ffmpeg -y -ss 0       -i clip.mp4 -frames:v 1 -q:v 2 poster.jpg
ffmpeg -y -sseof -0.04 -i clip.mp4 -frames:v 1 -q:v 2 lastframe.jpg
```

### 3.13 Captions as body-level siblings

Keep captions out of sub-composition timelines:

```html
<!-- In index.html, outside the master composition div -->
<div class="cap clip" data-start="3.2"  data-duration="2.1"  data-track-index="30">Deployed in weeks, not quarters.</div>
<div class="cap clip" data-start="5.4"  data-duration="2.8"  data-track-index="31">Three engagements. One clear outcome.</div>
```

```css
.cap {
  position: absolute; bottom: 72px; left: 50%; transform: translateX(-50%);
  padding: 10px 20px; border-radius: 50px;
  background: rgba(6, 6, 10, 0.6);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  font: 500 26px/1.3 'Plus Jakarta Sans', sans-serif;
  color: #CDCDD4;
}
```

Central control, zero coupling to scene timelines.

### 3.14 Tween-comment convention

Every entry/exit tween explicitly names the matching tween in the adjacent beat:

```javascript
// ENTRY — blur de-ramps from 18px to match the outgoing "infrastructure" beat's 18px exit.
gsap.set(wrap, { filter: 'blur(18px)' });
tl.to(wrap, { filter: 'blur(0px)', duration: 0.35, ease: 'power2.out' }, 0);

// EXIT (at local 1.65) — matches the incoming "outcome" beat's 60px y + 18px blur entry.
tl.to(wrap, { y: -60, filter: 'blur(18px)', duration: 0.35, ease: 'power2.in' }, 1.65);
```

If you can't name the matching tween in a comment, the seam isn't designed.

---

## 4 · Pre-flight Checklist

- [ ] **Average scene length ≤ 2s** in mid-section (opening/outro can hold longer)
- [ ] **No dead air over 1s** except deliberate hold moments
- [ ] **Every transition uses motion** (amber whip, ember flash, blur crossfade, slide — never a hard fade between unrelated beats)
- [ ] **Color palette: three accent families maximum** (Ember, Steel, Copper). One dominant per scene.
- [ ] **One Ember moment per section** — no more
- [ ] **Void and vignette present in every scene** — don't ship a flat-lit composition
- [ ] **Grain overlay on every scene** — subtle, but always there
- [ ] **Source Serif 4 weight 400 on all headings** — never 700
- [ ] **Ambient ember radial present** in at least the opening, Act 2 resolution beats, and the CTA
- [ ] **Breathing moments every 6-8s** — ember settling, coin reveal equivalent, brand statement hold
- [ ] **At least one callback** — a visual element that returns (Copper marks reappearing, the brand mark appearing mid-piece and again at outro)
- [ ] **CTA card holds 4+ seconds** — no exceptions
- [ ] **Visual verification done** — extracted frames, confirmed: no text overflow, no broken transitions, no scene landing mid-word
- [ ] **Every sub-composition timeline ends with `tl.to({}, { duration: SLOT_DURATION }, 0)`** (Law #10)
- [ ] **All tween end-times snap to multiples of `1/fps`** — at 30fps: 0.0333, 0.0667, 0.1...
- [ ] **Ran the timeline-duration diagnostic** and confirmed no `timeline.duration() < data-duration` gaps

---

## 5 · The "What Would Hihnala Do?" Test

Before shipping any motion piece:

1. **Could I cut this scene in half?** If yes, do it.
2. **Is this color carrying a meaning?** If no, remove it.
3. **Is the void dominant?** If more than 20% of the frame is lit, you're over-designing.
4. **Does the ambient ember radial breathe?** If the background is completely static, add drift.
5. **Where's the one ember moment in this section?** If there are two, pick one.
6. **Does the type scale, or just fade in?** Fading in is the lowest-effort reveal. Scale.
7. **Does the serif carry this beat, or the sans?** Default to serif for authority moments. Reserve the italic for the close.
8. **Will the viewer see this visual element again?** If no, consider whether a callback is possible.
9. **What's the unifying texture?** Void + ambient ember + particle drift. If a scene is missing all three, it doesn't belong to the piece.
10. **Where does the viewer rest?** Identify the breathing moments. If there are none, build them in.

---

## 6 · Anti-patterns

- No chrome gradients on type. Hihnala uses the four-level text color hierarchy.
- No flat white on flat black. Use the proper text levels: Soft White, Silver, Pewter, Ash.
- No iridescent, conic, or teal/magenta accents. Three families: Ember, Steel, Copper.
- No bold Source Serif 4. Weight 400, always.
- No multiple ember moments in one scene. One decisive beat per section.
- No hard cuts between unrelated scenes. Every cut needs a transition element.
- No outro that ends on the last kinetic beat. Hold the CTA for 4+ seconds minimum.
- No scenes that say two things. Split them.
- No static backgrounds. Every background has at least ambient particle drift and vignette breath.
- No decorative grain. Grain is a texture layer that belongs on every scene, not a stylistic choice applied unevenly.
- No `Math.random()` / `Date.now()` inside render loops. Use harmonic hashes: `Math.abs(Math.sin(i * 0.7 + 0.3) * Math.cos(i * 1.3 + 0.7))` gives reproducible "random-looking" values.
- No catalog blocks as a shortcut for hero moments. Build the CTA outro and brand reveal by hand. Use catalog blocks for production velocity on secondary beats.
- No elastic easing (`elastic.out`) for primary entrances. `back.out(1.2)` settling is allowed for cards. `elastic.out` reads as playful, not authoritative.
- No `transparent` keyword in CSS gradients — use `rgba(6,6,10,0)` for shader compatibility.
- No rendering without checking frames. Lint passing is not design working. Extract frames. Look at them.

---

## 7 · GSAP Reference

**Easings by purpose:**

| Purpose | Ease | Typical duration |
|---------|------|-----------------|
| Word reveal | `expo.out` | 0.20-0.35s |
| Element enter | `power3.out` | 0.3-0.6s |
| Element exit | `power2.in` | 0.2-0.35s |
| Amber whip exit | `power3.in` | 0.35-0.45s |
| Beat-to-beat entry | `power2.out` | 0.5-0.9s |
| Camera pan | `power2.inOut` | 1.2-2.3s |
| Linear hold | `none` | 0.4-0.65s |
| Card settle | `back.out(1.2)` | 0.3-0.5s |
| Ember settle | `sine.inOut` | 0.8-1.5s |
| Continuous breathe | `sine.inOut` yoyo | 3-6s, `repeat: -1` |
| Steel trace | `power2.inOut` | 1.0-2.0s |
| Copper mark appear | `back.out(1.4)` | 0.25-0.35s |

**Stagger values:**
- Word reveals: `stagger: 0.28-0.35`
- Copper marks: `stagger: 0.06-0.10`
- Particle drift (stagger from random): `each: 0.5-0.8`
- Caption lines: `0.08-0.12s` explicit delays

**Don't use `gsap.defaults()`.** Every tween declares its ease and duration explicitly. Inheritance bugs are harder to find than verbose tweens.

**Timeline skeleton:**

```javascript
(() => {
  const tl = gsap.timeline({ paused: true });
  // … tweens …
  tl.to({}, { duration: SLOT_DURATION }, 0);  // Law #10 anchor
  window.__timelines['<data-composition-id>'] = tl;
})();
```

Key must match `data-composition-id` exactly.

---

## 8 · TL;DR

> **One idea per beat, void dominant, serif at authority scale, one ember moment per section, copper marks the structure, steel traces the path — ambient breath in every still frame, amber whip on every cut, hold the CTA in silence, and every timeline fills its slot.**
