# Framesmith — Brand Design System

**Default brand: Hihnala** *Quiet Power. Editorial Authority. Physical Depth.*

To swap to a different brand, see `BRAND_SETUP.md`.

---

## Style Prompt

Hihnala is the Strategic Architect — calm, analytical, structured, ROI-driven. Decisive without being aggressive. Authoritative without being loud.

Brand promise: **Clarity before complexity. Operational freedom before novelty. Execution before hype.**

Compositions should feel like a premium intelligence briefing: near-black canvases layered with physical depth, a single ember-orange moment of decision per scene, editorial serif headlines, clean sans UI labels, and copper structure markers.

---

## Colors

Import tokens from `assets/brand-tokens.css`. Three accent families — Ember, Steel, Copper. No fourth.

**Psychological order (also the storytelling order in video):** Dark base → Intelligence (Steel) → Structure (Copper) → Action (Ember)

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

**Ember glow:** `rgba(255, 106, 26, 0.35)` for button shadows and radial pulses.
**Steel glow:** `rgba(79, 109, 138, 0.35)` for system traces and node activations.
**Copper line:** `rgba(212, 137, 47, 0.25)` for structural separators.

**Never:** full-screen gradients, new accent families, tinted backgrounds, colored paragraph text.

---

## Typography

**Headings:** Source Serif 4 (Google Fonts), weight 400. Never bold. Optical size axis active.
**Body / UI:** Plus Jakarta Sans (Google Fonts), weight 400 / 500 for labels.

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

Three voices: **Serif regular** (all headings, H1-H4), **Serif italic** (anchor lines, pull quotes, closing statements — rendered in Silver `#CDCDD4`), **Sans** (everything else: body, nav, buttons, labels, meta).

**In video:** Source Serif 4 can scale dramatically for kinetic type beats. The weight stays 400 — authority comes from scale and contrast, not thickness.

---

## Cards and Surfaces

**Double-bezel treatment** (required on all elevated surfaces, including video cards and UI panels):

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

For Glass variant (video compositions):
```css
.card-glass {
  background: linear-gradient(
    135deg,
    rgba(255,255,255,0.075),
    rgba(255,255,255,0.025),
    rgba(255,255,255,0.010),
    rgba(255,255,255,0.055)
  );
  backdrop-filter: blur(14px) saturate(1.12);
  border: 1px solid rgba(255, 255, 255, 0.10);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.22);
}
```

Never use flat cards on elevated surfaces.

---

## Dividers

**Glow divider** (major section transitions): A gradient line simulating a physical seam catching light.
```css
background: linear-gradient(90deg,
  transparent 0%,
  rgba(79, 109, 138, 0.2) 25%,
  rgba(212, 137, 47, 0.3) 50%,
  rgba(79, 109, 138, 0.2) 75%,
  transparent 100%
);
height: 1px;
```

**Quiet divider** (internal separation): A white line fading at both edges.
```css
background: linear-gradient(90deg,
  transparent 0%,
  rgba(255, 255, 255, 0.06) 20%,
  rgba(255, 255, 255, 0.06) 80%,
  transparent 100%
);
height: 1px;
```

Never use a hard 1px edge-to-edge border.

---

## Motion Rules

**Primary easing:** `cubic-bezier(0.32, 0.72, 0, 1)` — controlled spring with slight overshoot. Physical momentum.
**Subtle easing:** `cubic-bezier(0.22, 1, 0.36, 1)` — background transitions and content swaps.

In GSAP: `power3.out` for entrances, `expo.out` for snappy reveals.

**Web rules** (strict):
- Animate only `transform` and `opacity`
- Entrance only via `gsap.from()` — transitions handle exits
- Scroll entry: fade + y: 20px → 0, 400-600ms, stagger 0.08s
- No parallax. No scroll hijacking. No elastic easing.
- Backdrop-blur only on fixed nav.

**Video rules** (expanded — see `MOTION_PHILOSOPHY.md`):
- All web rules apply unless explicitly overridden
- `back.out(1.2)` settling is allowed for cards and UI elements
- Ember can pulse radially as a compositional event
- Steel can trace along paths for infrastructure beats
- Backdrop-blur valid on glass cards

---

## Logo

- `assets/hihnala-logo.jpg` — ember logo (1024×1024), use on dark backgrounds
- `assets/hihnala-logo-sm.jpeg` — smaller variant
- `assets/hihnala-youtube-banner.png` — 2560×1440 YouTube banner
- CSS glow on dark: `filter: drop-shadow(0 0 32px rgba(255, 106, 26, 0.35));`
- Clearspace: half the logo height on all sides, minimum
- Never recolor, stretch, or add effects beyond the spec glow

---

## What NOT to Do

1. No full-screen linear gradients (H.264 banding). Use solid `--hihnala-bg` + localized radial ember glow.
2. No neon colors, playful saturation, or additional accent families.
3. No Source Serif 4 at weight 700. Always 400.
4. No chrome gradients on type. Hihnala uses flat text colors from the four-level hierarchy.
5. No system fonts, Inter, Roboto, Arial. Only Source Serif 4 + Plus Jakarta Sans.
6. No `transparent` keyword in gradients — use `rgba(6,6,10,0)` for shader compatibility.
7. No `Math.random()` or `Date.now()` — render determinism. Use seeded PRNG.
8. No exit animations on any scene except the final.
9. No hype words: "revolutionary," "cutting edge," "disruptive," "seamless," "unleash," "leverage," "next-gen."
10. No flat cards on elevated surfaces — always use the double-bezel treatment.
11. Never stretch the logo. Respect clearspace.
12. No multiple active accents in one scene — one dominant accent per beat.
