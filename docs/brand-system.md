# Brand System

Framesmith ships with the **Hihnala** brand as its default. Every composition, thumbnail, and caption is built from a single source of truth: `DESIGN.md` at the workspace root.

If you want to use your own brand, see [Swapping the brand](#swapping-the-brand) at the bottom of this page.

---

## The Hihnala brand

*Quiet Power. Editorial Authority. Physical Depth.*

Hihnala is the Strategic Architect — calm, analytical, ROI-driven. Decisive without being aggressive. Authoritative without being loud.

Compositions should feel like a premium intelligence briefing: near-black canvases layered with physical depth, a single ember-orange accent, editorial serif headlines, and clean sans labels.

---

## Colors

Three accent families. No fourth. No decorative colors.

### Foundation — 80–90% of every frame

| Token | Hex | Role |
| --- | --- | --- |
| `--hihnala-abyss` | `#040408` | Deepest background, luxury screens |
| `--hihnala-bg` | `#06060A` | Primary canvas (Deep Void) |
| `--hihnala-carbon` | `#0C0C11` | Alternate section background |
| `--hihnala-surface` | `#141419` | Cards, elevated surfaces (Graphite) |
| `--hihnala-slate` | `#1C1C23` | Hover states, tertiary surfaces |

Section alternation: Deep Void and Carbon only. Cards always use Graphite. Slate is for hover states — never as a static background.

### Text hierarchy

| Token | Hex | Role |
| --- | --- | --- |
| `--hihnala-text` | `#F5F5F7` | H1–H4 headings, high-emphasis (Soft White) |
| `--hihnala-silver` | `#CDCDD4` | Subheadings, anchor lines, serif italic |
| `--hihnala-pewter` | `#8E8E99` | Body paragraphs |
| `--hihnala-ash` | `#5A5A66` | Meta text, labels, timestamps |

Section labels (uppercase): Copper `#D4892F`. Inline emphasis (rare): Ember `#FF6A1A`. Never use color for paragraph text.

### Ember — action, CTA, commitment

| Token | Hex | Role |
| --- | --- | --- |
| `--hihnala-ember` | `#FF6A1A` | Primary CTA, key emphasis |
| `--hihnala-ember-hover` | `#FF8C42` | Hover state |
| `--hihnala-ember-active` | `#E55300` | Active / pressed state |
| `--hihnala-ember-glow` | `rgba(255,106,26,0.35)` | Button shadow, logo glow |

One Ember-dominant element per scene. Ember is a decision — never decoration.

### Steel — systems, infrastructure

| Token | Hex | Role |
| --- | --- | --- |
| `--hihnala-steel` | `#4F6D8A` | System elements, AI accent |
| `--hihnala-steel-deep` | `#3E566E` | Hover / active |
| `--hihnala-steel-pale` | `#6F8FAE` | Accent lines, tier labels |

### Copper — structure, hierarchy (micro-accent only)

| Token | Hex | Role |
| --- | --- | --- |
| `--hihnala-copper` | `#D4892F` | Section labels, step numbers |
| `--hihnala-copper-dim` | `#9C6424` | Subtle separators |

Never use Copper for buttons or body text.

### Psychological order

**Dark base → Intelligence (Steel) → Structure (Copper) → Action (Ember)**

Never invert this order. Ember must always feel like a decision.

### Borders and dividers

- **Slate line:** `rgba(255,255,255,0.06)` — subtle internal borders
- **Glow divider:** `linear-gradient(90deg, transparent, rgba(79,109,138,0.2) 25%, rgba(212,137,47,0.3) 50%, rgba(79,109,138,0.2) 75%, transparent)` — major section transitions
- **Quiet divider:** `linear-gradient(90deg, transparent, rgba(255,255,255,0.06) 20%, rgba(255,255,255,0.06) 80%, transparent)` — internal separation

Never use a hard 1px border edge-to-edge.

---

## Typography

### Font pairing

**Headings:** Source Serif 4 (Google Fonts), weight 400. The optical size axis automatically adjusts stroke weight — thicker at small sizes, more refined at display. Always 400 — never bold. Authority comes from letterform quality, not thickness.

**Body / UI:** Plus Jakarta Sans (Google Fonts), weight 400 (body) / 500 (labels, nav). Warmer geometry than IBM Plex Sans, better optical balance at small sizes.

### Scale

| Level | Size | Weight | Line height | Use |
| --- | --- | --- | --- | --- |
| H1 | 56px | 400 | 1.05 | Hero, page titles |
| H2 | 44px | 400 | 1.10 | Section headings |
| H3 | 32px | 400 | 1.15 | Sub-section headings |
| H4 | 24px | 400 | 1.20 | Card titles |
| Lead | 20px | 400 | 1.60 | Opening paragraphs |
| Body | 16px | 400 | 1.65 | Standard paragraphs |
| Labels | 13px | 500 | 1.40 | Navigation, UI labels |
| Meta | 11px | 500 | 1.40 | Section tags, uppercase labels |

### Three typographic voices

- **Serif regular** — Source Serif 4 weight 400. All headings (H1–H4), step titles. Calm authority.
- **Serif italic** — Source Serif 4 italic weight 400. Anchor lines, pull quotes, brand tagline. Rendered in Silver `#CDCDD4`.
- **Sans** — Plus Jakarta Sans. Everything else: body, navigation, labels, captions, buttons.

---

## Motion rules

### Easing

**Primary:** `cubic-bezier(0.32, 0.72, 0, 1)` — controlled spring with slight overshoot. Physical momentum. In GSAP: `power3.out` for entrances, `expo.out` for snappy reveals.

**Subtle:** `cubic-bezier(0.22, 1, 0.36, 1)` — background transitions and content swaps. In GSAP: `sine.inOut`.

### Rules

- Animate only `transform` and `opacity`
- Entrances via `gsap.from()` only — transitions handle exits
- No exit animations on any scene except the final
- No parallax, no scroll hijacking, no elastic or bouncing easing
- Duration bands: snap 0.3–0.5s, headline 0.6–0.9s, ambient 3–5s

### Scene transitions

| Change | Transition | Duration | Ease |
| --- | --- | --- | --- |
| Opening | Ember flash (opacity + scale) | 0.4s | `power4.inOut` |
| Mid-video | Push slide left | 0.35s | `power2.inOut` |
| Final | Blur crossfade | 0.5s | `sine.inOut` |

Average scene length: ~1.5 seconds. One idea per beat.

---

## The double-bezel card

Signature elevated surface. Every card or container that needs visual lift uses nested architecture:

- **Outer shell:** Graphite `#141419`, border-radius 20px. Gradient border mask (brighter top-left → transparent bottom-right) simulates directional light.
- **Inner core:** Carbon `#0C0C11`, border-radius 18px, padding 32px. Inner shadows top and bottom.

Never use a flat card on an elevated surface.

---

## Logo

- `assets/hihnala-logo.jpg` — ember logo, 1024×1024, for dark backgrounds
- `assets/hihnala-logo-sm.jpeg` — smaller variant
- `assets/hihnala-youtube-banner.png` — 2560×1440 YouTube banner

CSS glow on dark: `filter: drop-shadow(0 0 32px rgba(255, 106, 26, 0.35));`

Clear space: half the logo height on all sides. Never recolor, stretch, or add effects beyond the spec glow.

---

## What NOT to do

These are enforced by the delivery checklist and caught by the agent during composition review.

1. **No full-screen linear gradients** — H.264 banding. Use solid `--hihnala-bg` + localized radial ember glow.
2. **No additional accent families** — Ember, Steel, Copper only. No fourth color.
3. **No Source Serif 4 at weight 700** — always 400.
4. **No system fonts, Inter, Roboto, Arial** — Source Serif 4 + Plus Jakarta Sans only.
5. **No ****`transparent`**** keyword in gradients** — use `rgba(6,6,10,0)` for shader compatibility.
6. **No ****`Math.random()`**** or ****`Date.now()`** — compositions must be deterministic.
7. **No flat cards on elevated surfaces** — always double-bezel.
8. **No hype words in VO or captions** — revolutionary, cutting edge, disruptive, seamless, unleash, leverage, next-gen, game-changer.
9. **No exit animations** on any scene except the final — transitions handle exits.
10. **Never stretch the logo** — respect clear space on all sides.

---

## Swapping the brand

Framesmith is built to be re-branded. The Hihnala system is the default — anyone cloning the repo can replace it entirely.

### What to change

| File | What it contains | Your action |
| --- | --- | --- |
| `DESIGN.md` | Full brand spec | Replace with your own — same sections, different values |
| `assets/brand-tokens.css` | CSS custom properties | Replace `--hihnala-` prefix and values |
| `assets/hihnala-logo.*` | Logo files | Add your own logos |

`MOTION_PHILOSOPHY.md` is brand-neutral and should be kept as-is.

### How to write your DESIGN.md

At a minimum, include these sections:

```markdown
## Style Prompt
One paragraph: visual personality, emotional target, what the composition should feel like.

## Colors
Three accent families maximum. Table: token | hex | role.
Psychological order of your accents.

## Typography
Heading font + body font. Weight and size scale. Three typographic voices.

## Motion Rules
Primary easing curve. Duration bands. What to animate, what not to.

## Logo
File paths. Clear space. Glow treatment (if any).

## What NOT to Do
5–10 anti-patterns specific to your brand.
```

### How to update brand-tokens.css

Replace the `--hihnala-` prefix with your brand name and update the hex values:

```css
/* Replace: */
--hihnala-ember: #FF6A1A;

/* With: */
--yourbrand-primary: #your-hex;
```

The agent reads `brand-tokens.css` and references these token names in compositions. If you change the prefix, update `DESIGN.md` to use the new names so the agent stays consistent.

### Updating CLAUDE.md and AGENTS.md

In both files, update the brand name reference in the "Brand system" section header and the `DESIGN.md` source of truth pointer.

### Full guide

See [BRAND_SETUP.md](./../BRAND_SETUP.md) at the workspace root for the complete step-by-step.
