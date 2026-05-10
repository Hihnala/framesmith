# Framesmith — Brand Setup Guide

Framesmith ships with the **Hihnala** brand as its default. This guide explains how to replace the brand system with your own.

---

## What to replace

| File | What it contains | Your action |
|------|-----------------|-------------|
| `DESIGN.md` | Colors, fonts, motion rules, logo spec | Replace with your brand system |
| `assets/brand-tokens.css` | CSS custom properties for all brand tokens | Replace variable names and values |
| `assets/hihnala-logo.*` | Hihnala logo files | Add your own logos |
| `MOTION_PHILOSOPHY.md` | Motion discipline — Hihnala brand layer pre-filled | Adapt the brand layer — see the adaptation guide at the top of the file |

---

## Step-by-step

### 1. Replace DESIGN.md

Write your own `DESIGN.md` at the workspace root. At a minimum, include these sections:

```
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
5-10 anti-patterns specific to your brand.
```

### 2. Update brand-tokens.css

Replace `--hihnala-` prefixes with your own brand name prefix. Keep the same token structure (bg, surface, text, primary, secondary, tertiary) — the skills reference this structure.

```css
/* Replace: */
--hihnala-ember: #FF6A1A;

/* With: */
--yourbrand-primary: #your-hex;
```

Then update `DESIGN.md` to reference your new token names.

### 3. Adapt MOTION_PHILOSOPHY.md

The file ships pre-filled with the Hihnala brand. The Laws, pacing rules, and technical HyperFrames recipes are universal. The colors, font names, move names, and act assignments are Hihnala-specific.

Open the file. The **For Other Brands** section at the top lists every substitution you need to make, with a table mapping Hihnala values to their generic roles. Fill in your values and update the sections listed there.

### 4. Add your logo files

Drop your logos into `assets/`. Update the Logo section in `DESIGN.md` with the correct file paths.

### 5. Update CLAUDE.md references

In `CLAUDE.md`, update the brand name in the "Brand" section heading and the `DESIGN.md` source of truth pointer.

---

## What stays the same

- All HyperFrames skills — framework rules are brand-neutral
- All Python tools (`tools/`) — fully brand-neutral
- The three-level workflow — works for any brand
- The gate system — works for any brand
- The technical recipes in `MOTION_PHILOSOPHY.md` §3.8–3.14 — no brand values in those sections

---

## Keeping it public

If you publish your fork publicly, the MIT license allows it. Just:

1. Keep the `LICENSE` file with attribution intact
2. Add your own name/org to the `package.json` author field
3. Update `README.md` to reflect your brand
