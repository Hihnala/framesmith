# Framesmith — Brand Design System

**Default brand: Hihnala** *Quiet Power. Editorial Authority. Physical Depth.*

To swap to a different brand, see `BRAND_SETUP.md`.

---

## Style Prompt

Hihnala is the Strategic Architect — calm, analytical, structured, ROI-driven. Decisive without being aggressive. Authoritative without being loud.

Brand promise: **Clarity before complexity. Operational freedom before novelty. Execution before hype.**

**Website compositions:** near-black canvases, single ember accent, editorial serif headlines, clean sans UI labels.

**Video overlays on talking-head footage:** the void moves into the cards. White-wall footage is the canvas. Dark glass cards carry the brand. Every text element must be readable at a glance without the viewer pausing or squinting.

---

## Colors

Import tokens from `assets/brand-tokens.css`. Three accent families — Ember, Steel, Copper. No fourth.

**Psychological order:** Dark base → Intelligence (Steel) → Structure (Copper) → Action (Ember)

| Role | Token | Hex |
|------|-------|-----|
| Primary bg | `--hihnala-bg` | `#06060A` (Deep Void) |
| Deepest bg | `--hihnala-abyss` | `#040408` |
| Alt section | `--hihnala-carbon` | `#0C0C11` |
| Cards | `--hihnala-surface` | `#141419` (Graphite) |
| Hover state | `--hihnala-slate` | `#1C1C23` |
| Headings | `--hihnala-text` | `#F5F5F7` (Soft White) |
| Subheadings / anchor lines | `--hihnala-silver` | `#CDCDD4` |
| Body / descriptions | `--hihnala-pewter` | `#8E8E99` |
| Meta / labels | `--hihnala-ash` | `#5A5A66` |
| CTA / Ember | `--hihnala-ember` | `#FF6A1A` |
| Ember hover | `--hihnala-ember-hover` | `#FF8C42` |
| Section labels | `--hihnala-copper` | `#D4892F` |
| System accents | `--hihnala-steel` | `#4F6D8A` |

**Ember glow:** `rgba(255, 106, 26, 0.35)`
**Steel glow:** `rgba(79, 109, 138, 0.35)`
**Copper line:** `rgba(212, 137, 47, 0.25)`

### Contrast rules for white-background video footage

White-wall footage is the brightest possible canvas. Most of the Hihnala palette is designed for dark surfaces and is invisible at normal scale on white.

| Color | Directly on white footage | Inside dark card (≥88% opacity) |
|-------|--------------------------|----------------------------------|
| Ember `#FF6A1A` | ✅ 48px+ only | ✅ any size |
| Deep Void `#06060A` | ✅ 40px+ only | — |
| Copper `#D4892F` | ⚠️ 64px+ only, short durations | ✅ 32px+ |
| Steel `#4F6D8A` | ❌ never | ✅ 32px+ |
| Soft White `#F5F5F7` | ❌ never | ✅ any size |
| Silver `#CDCDD4` | ❌ never | ✅ 28px+ |
| Pewter `#8E8E99` | ❌ never | ✅ supporting text only |
| Ash `#5A5A66` | ❌ never | ❌ too subtle for video at any size |

**Rule:** Steel, Silver, Pewter, and Ash never appear directly on footage. They live inside dark cards only.

---

## Typography

**Headings:** Source Serif 4 (Google Fonts), weight 400. Never bold. Optical size axis active.
**Body / UI:** Plus Jakarta Sans (Google Fonts), weight 400 / 500 for labels.

### Website scale

| Level | Size | Weight | Use |
|-------|------|--------|-----|
| H1 | 56px | 400 | Hero, page titles |
| H2 | 44px | 400 | Section headings |
| H3 | 32px | 400 | Sub-section headings |
| H4 | 24px | 400 | Card titles |
| Lead | 20px | 400 | Opening paragraphs |
| Body | 16px | 400 | Standard paragraphs |
| Labels | 13px | 500 | Nav, UI labels |
| Meta | 11px | 500 | Section tags, uppercase |

### Video scale (minimum sizes in a 1920×1080 composition)

These are hard minimums. Video is watched at varying screen sizes and distances. Below these sizes, text is unreadable during normal playback.

| Element | Minimum size | Font | Color |
|---------|-------------|------|-------|
| Captions / subtitles | 36px | Plus Jakarta Sans 500 | Soft White on dark pill |
| Card supporting text | 40px | Plus Jakarta Sans 400 | Soft White |
| Card labels / meta | 32px | Plus Jakarta Sans 500 uppercase | Copper or Silver |
| Stat numbers | 72–96px | Source Serif 4 400 | Soft White |
| Stat labels | 32px | Plus Jakarta Sans 500 uppercase | Copper |
| Pull quote text | 52–64px | Source Serif 4 400 italic | Silver |
| Chapter marker heading | 48px | Source Serif 4 400 | Soft White |
| Lower third name | 52px | Source Serif 4 400 | Soft White |
| Lower third title/role | 34px | Plus Jakarta Sans 400 | Silver |
| Ember emphasis word | 64px+ | Source Serif 4 400 italic | Ember |

Three typographic voices remain: **Serif regular** (authority headings), **Serif italic** (pull quotes, anchor lines, Ember emphasis), **Sans** (captions, labels, body).

---

## Video Overlay System

Hihnala videos are talking-head footage on a white background. The overlay system carries the brand. Four types cover all use cases.

### Overlay card spec

All cards use this dark glass treatment. The opacity is higher than the website spec because white footage reads through any transparency aggressively.

```css
.overlay-card {
  background: rgba(6, 6, 10, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 12px;
  box-shadow:
    0 0 0 1px rgba(255, 255, 255, 0.04),
    0 8px 32px rgba(0, 0, 0, 0.5);
  padding: 28px 36px;
  /* Start hidden — show/hide via GSAP autoAlpha only */
  opacity: 0;
  visibility: hidden;
}
```

### Type 1 — Lower Third

Speaker intro. Appears at 0–6s. Identifies who is speaking and why the viewer should listen.

- Position: left-aligned, 72px from left, 80px from bottom
- Width: 480–600px
- Name line: Source Serif 4, 52px, Soft White
- Role line: Plus Jakarta Sans, 34px, Silver
- Copper accent: 2px horizontal rule, 40px wide, above name
- Entry: `y: 40 → 0`, `autoAlpha: 0 → 1`, 0.6s `power3.out`
- Hold: 4–5 seconds
- Exit: `autoAlpha: 1 → 0`, 0.4s `power2.in`

### Type 2 — Stat Callout

Fires when a number, percentage, or key metric is spoken. Confirms and amplifies the claim.

- Position: right-anchored or centered, clear of speaker's face
- Width: 320–500px
- Number: Source Serif 4, 80–96px, Soft White
- Label: Plus Jakarta Sans, 32px uppercase, Copper
- Ember underline: 3px in `#FF6A1A`, 60% of number width, appears 0.15s after number lands
- Entry: `scale: 0.92 → 1`, `autoAlpha: 0 → 1`, 0.4s `back.out(1.2)`
- Hold: match spoken duration (minimum 2.5s)
- Exit: `y: 0 → -10`, `autoAlpha: 1 → 0`, 0.35s `power2.in`

### Type 3 — Pull Quote

Appears when a key principle, claim, or reusable insight is stated. These are the shareable moments.

- Position: centered, or left-anchored at 72px from left
- Width: 680–880px
- Left accent: 4px vertical Ember bar, full card height
- Quote text: Source Serif 4, 52px italic, Silver
- Context line (optional): Plus Jakarta Sans, 28px, Pewter
- Entry: `x: -40 → 0`, `autoAlpha: 0 → 1`, 0.7s `power3.out`
- Hold: spoken duration + 1 second
- Exit: `autoAlpha: 1 → 0`, 0.4s `sine.in`

### Type 4 — Chapter Marker

Between major topics. Brief orientation so the viewer knows where they are.

- Position: centered, pill-shaped
- Chapter label: Plus Jakarta Sans, 24px uppercase, Copper
- Topic heading: Source Serif 4, 48px, Soft White
- Background: `rgba(6, 6, 10, 0.92)`, `border-radius: 50px`
- Entry: `scale: 0.94 → 1`, `autoAlpha: 0 → 1`, 0.5s `expo.out`
- Hold: 2.5–3 seconds
- Exit: `scale: 1 → 0.96`, `autoAlpha: 1 → 0`, 0.4s `power2.in`

### Kinetic captions

Word-by-word captions sync to speech. These are the highest single retention lever in talking-head video.

- Font: Plus Jakarta Sans, 36px, weight 500
- Color: Soft White `#F5F5F7`
- Background: dark pill, `rgba(6, 6, 10, 0.80)`, `border-radius: 50px`, `padding: 10px 24px`
- Position: bottom, 64px from edge, horizontally centered
- Reveal: `y: 14 → 0`, `autoAlpha: 0 → 1`, 0.22s `power3.out`, stagger 0.16s per word
- Ember emphasis: key words can render in `#FF6A1A` — one per caption line maximum

---

## Cards and Surfaces (website / full-screen beats)

**Double-bezel treatment:**

```css
.card {
  background: #141419;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  box-shadow:
    0 0 0 1px rgba(255, 255, 255, 0.03),
    0 4px 24px rgba(0, 0, 0, 0.6);
}
```

---

## Dividers

**Glow divider:**
```css
background: linear-gradient(90deg,
  transparent 0%, rgba(79,109,138,0.2) 25%,
  rgba(212,137,47,0.3) 50%, rgba(79,109,138,0.2) 75%, transparent 100%);
height: 1px;
```

**Quiet divider:**
```css
background: linear-gradient(90deg,
  transparent 0%, rgba(255,255,255,0.06) 20%,
  rgba(255,255,255,0.06) 80%, transparent 100%);
height: 1px;
```

---

## Motion Rules

**Primary easing:** `cubic-bezier(0.32, 0.72, 0, 1)`. GSAP: `power3.out` entrances, `expo.out` snappy reveals.
**Subtle easing:** `cubic-bezier(0.22, 1, 0.36, 1)`. GSAP: `sine.inOut`.

**Full-screen composition beats** (dark void canvas, no footage):
- `back.out(1.2)` settling allowed for cards
- Ember can pulse radially as a compositional event
- Steel can trace along paths

**Overlay beats** (on top of white-background video footage):
- All overlays: `opacity: 0; visibility: hidden` in CSS at start
- Show/hide via GSAP `autoAlpha` only — `class="clip"` has no timing effect inside sub-compositions
- One overlay card visible at a time
- Captions always active regardless of card state
- No overlay covers the speaker's face

See `MOTION_PHILOSOPHY.md` for the full Laws, overlay recipes, sub-composition rules, and pre-flight checklist.

---

## Logo

- `assets/hihnala-logo.jpg` — 1024×1024, dark backgrounds
- `assets/hihnala-logo-sm.jpeg` — smaller variant
- `assets/hihnala-youtube-banner.png` — 2560×1440
- CSS glow: `filter: drop-shadow(0 0 32px rgba(255, 106, 26, 0.35));`
- Clearspace: half logo height on all sides. Never recolor, stretch, or add effects beyond the spec glow.

---

## What NOT to Do

1. **No Steel, Silver, Pewter, or Ash text directly on video footage.** These only live inside dark cards.
2. **No text below 32px in any video composition.** It cannot be read on standard screens at normal viewing distance.
3. **No `class="clip"` inside sub-compositions.** It does nothing. Use GSAP `autoAlpha`.
4. **No multiple overlay cards active simultaneously.** One card at a time.
5. **No overlay that covers the speaker's face.** In talking-head footage the face occupies the vertical center of the frame. Never use `top: 50%`, `margin: auto` with centered vertical position, or any equivalent that places a card at mid-frame height. Safe zones: chapter markers at `top: 48px` (top edge), pull quotes top-left (`top: 88px; left: 72px`), stat callouts top-right (`top: 280–350px; right: 80px`), lower thirds bottom-left (`bottom: 160px+`). When in doubt, position above the eye line or below the chin — never at chest/face height.
6. **No exit animations competing with spoken content.** Cards exit during natural pauses only.
7. **No full-screen linear gradients.** H.264 banding. Use `--hihnala-bg` + localized radial ember glow.
8. **No Source Serif 4 at weight 700.** Always 400.
9. **No system fonts, Inter, Roboto, Arial.** Source Serif 4 + Plus Jakarta Sans only.
10. **No `transparent` in CSS gradients.** Use `rgba(6,6,10,0)` for shader compatibility.
11. **No `Math.random()` or `Date.now()`.** Render determinism only.
12. **No hype words in captions or overlays:** revolutionary, cutting edge, disruptive, seamless, unleash, leverage, next-gen.
