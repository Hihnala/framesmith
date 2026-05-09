# Framesmith — Brand Setup Guide

Framesmith ships with the **Hihnala** brand as its default. This guide explains how to replace the brand system with your own.

---

## What to replace

| File | What it contains | Your action |
| --- | --- | --- |
| `DESIGN.md` | Colors, fonts, motion rules, logo spec | Replace with your brand system |
| `assets/brand-tokens.css` | CSS custom properties for all brand tokens | Replace variable names and values |
| `assets/hihnala-logo.*` | Hihnala logo files | Add your own logos |
| `MOTION_PHILOSOPHY.md` | Motion discipline (brand-neutral) | Keep as-is or extend |

---

## Step-by-step

### 1. Replace DESIGN.md

Write your own `DESIGN.md` at the workspace root. At a minimum, include these sections:

```markdown
## Style Prompt
One paragraph describing the brand's visual personality and emotional target.

## Colors
Table of: token name | hex | role
Three accent families maximum.

## Typography
Heading font + body font. Size scale. Weight rules.

## Motion Rules
Primary easing curve. Duration bands. What NOT to animate.

## Logo
File paths. Clear space rules. Glow treatment if any.

## What NOT to Do
5–10 anti-patterns specific to your brand.
```

### 2. Update brand-tokens.css

Replace `--hihnala-` prefixes with your own brand name prefix. Keep the same token structure (bg, surface, text, ember/primary, steel/secondary, copper/tertiary) — the skills reference this structure.

```css
/* Replace: */
--hihnala-ember: #FF6A1A;

/* With: */
--yourbrand-primary: #your-hex;
```

Then update `DESIGN.md` to reference your new token names.

### 3. Add your logo files

Drop your logos into `assets/`. Update the Logo section in `DESIGN.md` with the correct file paths.

### 4. Update CLAUDE.md references

In `CLAUDE.md`, update the brand name in the "Brand" section heading and the `DESIGN.md` source of truth pointer.

---

## What stays the same

- All HyperFrames skills (framework rules are brand-neutral)
- `MOTION_PHILOSOPHY.md` (motion discipline applies to any brand)
- All Python tools (`tools/`) — fully brand-neutral
- The three-level workflow — works for any brand
- The gate system — works for any brand

---

## Keeping it public

If you publish your fork publicly, the MIT license allows it. Just:
1. Keep the `LICENSE` file with attribution intact
2. Add your own name/org to the `package.json` author field
3. Update the `README.md` to reflect your brand
