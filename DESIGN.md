# Framesmith — Brand Design System

**Default brand: Hihnala**
*Quiet Power. Editorial Authority. Physical Depth.*

Source of truth: `/Users/markku/Documents/Hihnala/Docs-v3/Hihnala Brand System.md`
To swap to a different brand, see `BRAND_SETUP.md`.

---

## Style Prompt

Hihnala is the Strategic Architect — calm, analytical, structured, ROI-driven. Decisive without being aggressive. Authoritative without being loud.

Brand promise: **Clarity before complexity. Operational freedom before novelty. Execution before hype.**

Compositions should feel like a premium intelligence briefing: near-black canvases layered with physical depth, ember-orange as a single decisive accent, editorial serif headlines, clean sans UI labels, and copper structure markers.

---

## Colors

Import tokens from `assets/brand-tokens.css`. Three accent families — Ember, Steel, Copper. No fourth.

**Psychological order:** Dark base → Intelligence (Steel) → Structure (Copper) → Action (Ember)

| Role | Token | Hex |
| --- | --- | --- |
| Primary bg | `--hihnala-bg` | `#06060A` (Deep Void) |
| Alt section | `--hihnala-carbon` | `#0C0C11` |
| Cards | `--hihnala-surface` | `#141419` (Graphite) |
| Headings | `--hihnala-text` | `#F5F5F7` |
| Body | `--hihnala-pewter` | `#8E8E99` |
| CTA / Ember | `--hihnala-ember` | `#FF6A1A` |
| Section labels | `--hihnala-copper` | `#D4892F` |
| System accents | `--hihnala-steel` | `#4F6D8A` |

**Never:** full-screen gradients, new accent families, tinted backgrounds, colored paragraph text.

---

## Typography

**Headings:** Source Serif 4 (Google Fonts), weight 400. Never bold. Optical size axis active.
**Body / UI:** Plus Jakarta Sans (Google Fonts), weight 400 / 500 for labels.

| Level | Size | Weight | Use |
| --- | --- | --- | --- |
| H1 | 56px | 400 | Hero, page titles |
| H2 | 44px | 400 | Section headings |
| H3 | 32px | 400 | Sub-section headings |
| H4 | 24px | 400 | Card titles |
| Lead | 20px | 400 | Opening paragraphs |
| Body | 16px | 400 | Standard paragraphs |
| Labels | 13px | 500 | Nav, UI labels |
| Meta | 11px | 500 | Section tags, uppercase |

Three voices: **Serif regular** (all headings), **Serif italic** (anchor lines, pull quotes, Silver `#CDCDD4`), **Sans** (everything else).

---

## Motion Rules (HyperFrames compositions)

**Primary easing:** `cubic-bezier(0.32, 0.72, 0, 1)` — controlled spring, slight overshoot. Physical momentum.
**Subtle easing:** `cubic-bezier(0.22, 1, 0.36, 1)` — bg transitions, content swaps.

In GSAP: use `power3.out` for entrances, `expo.out` for snappy reveals.

**Rules:**
- Animate only `transform` and `opacity` — never `top`, `left`, `width`, `height`
- Entrance only via `gsap.from()` — transitions handle exits
- Scroll entry: fade + y: 20px → 0, 400–600ms, stagger 0.08s
- Duration bands: snap 0.3–0.5s, headline 0.6–0.9s, ambient 3–5s
- No parallax, no scroll hijacking, no elastic easing

**Transitions:**
| Scene change | Transition | Duration | Ease |
| --- | --- | --- | --- |
| 1 → 2 | Ember flash (opacity + scale) | 0.4s | `power4.inOut` |
| 2 → 3 | Push slide left | 0.35s | `power2.inOut` |
| 3+ | Push slide left | 0.35s | `power2.inOut` |
| Final | Blur crossfade | 0.5s | `sine.inOut` |

---

## Logo

- `assets/hihnala-logo.jpg` — ember logo (1024×1024), use on dark backgrounds
- `assets/hihnala-logo-sm.jpeg` — smaller variant
- `assets/hihnala-youtube-banner.png` — 2560×1440 YouTube banner
- CSS glow on dark: `filter: drop-shadow(0 0 32px rgba(255, 106, 26, 0.35));`
- Never recolor, stretch, or add effects beyond the spec glow

---

## What NOT to Do

1. No full-screen linear gradients (H.264 banding). Use solid `--hihnala-bg` + localized radial ember glow.
2. No neon colors, playful saturation, or additional accent families.
3. No Source Serif 4 at weight 700. Always 400.
4. No system fonts, Inter, Roboto, Arial. Only Source Serif 4 + Plus Jakarta Sans.
5. No `transparent` keyword in gradients — use `rgba(6,6,10,0)` for shader compatibility.
6. No `Math.random()` or `Date.now()` — render determinism. Use seeded PRNG.
7. No exit animations on any scene except the final.
8. No hype words: "revolutionary," "cutting edge," "disruptive," "seamless," "unleash," "leverage," "next-gen."
9. No flat cards on elevated surfaces — always use the double-bezel treatment.
10. Never stretch the logo. Respect clearspace (half logo-height on all sides).
