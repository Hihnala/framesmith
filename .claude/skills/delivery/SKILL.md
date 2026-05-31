---
name: delivery
description: Run the Framesmith delivery gate before any video is uploaded or shared. Produces a signed-off DELIVERY.md in the project folder. Use when the user says "ready to publish", "ship it", "final check", "delivery", or after a final render is approved. Blocks delivery until all critical items pass.
---

# Delivery — Pre-Publish Gate

Runs a structured checklist across four categories before any video is considered done. Produces `DELIVERY.md` in the project folder as a permanent record of the sign-off.

**No video ships without a completed DELIVERY.md.**

---

## How to run the gate

Go through each category in order. For each item:
- Check the actual file, composition, or render — do not assume
- Mark `[x]` if confirmed, `[!]` if it needs fixing, `[n/a]` if genuinely not applicable
- Block delivery if any critical item (`*`) is marked `[!]`

Non-critical items (`[!]` without `*`) produce a warning but do not block.

---

## Category 1 — Content

| Item | Critical | How to verify |
|---|---|---|
| Hook lands within the first 3 seconds | * | Extract frame at t=2s, confirm the hook line is visible |
| Single clear CTA at the end | * | Read the CTA scene in `SCRIPT.md` or final scene in composition |
| No banned words in VO or captions | * | Search `SCRIPT.md` for: revolutionary, cutting edge, disruptive, seamless, unleash, leverage, next-gen, game-changer, basically, kind of |
| Script exists and was approved | * | `SCRIPT.md` present in project folder |
| Captions are word-accurate | * | Compare transcript against rendered captions in draft MP4 |
| Duration fits platform limits | * | YouTube: no hard limit; LinkedIn: ≤10min; verify with ffprobe |

## Category 2 — Brand

| Item | Critical | How to verify |
|---|---|---|
| Source Serif 4 used for all headings (weight 400) | * | Search compositions for any other heading font |
| Plus Jakarta Sans used for body and labels | * | Search compositions for system fonts (Inter, Roboto, Arial) |
| Only Hihnala brand colors — no hardcoded hex outside tokens | * | Search compositions for hex values not in `assets/brand-tokens.css` |
| No `transparent` keyword in gradients | * | Search compositions for `transparent` inside `linear-gradient` or `radial-gradient` |
| Logo present in outro or lower-third (if applicable) | — | Check final scene of composition |
| Double-bezel applied to all elevated containers | — | Review key frames from draft render |
| No flat cards on elevated surfaces | — | Review key frames |

## Category 3 — Technical

| Item | Critical | How to verify |
|---|---|---|
| `npx hyperframes lint` — zero errors | * | Run lint, confirm exit code 0 |
| Studio preview reviewed (Gate 1) | * | Confirmed in `JOURNAL.md` |
| Draft render reviewed (Gate 2) | * | Confirmed in `JOURNAL.md` |
| Renders produced for chosen platform(s) | * | Check which platform(s) were selected in Gate 3; verify `renders/<project>-<platform>.mp4` exists for each |
| Render durations match (within 0.1s) | * | Only applies when both YouTube and LinkedIn were rendered; `render-all.sh` duration check passed |
| No `Math.random()` or `Date.now()` in compositions | * | Search all HTML files |
| No render-time network fetches | * | Search all HTML files for fetch(), XMLHttpRequest, `<script src="http` |
| All GSAP timelines end with no-op duration anchor | — | Check each composition's timeline registration |

## Category 4 — Platform readiness

| Item | Critical | How to verify |
|---|---|---|
| Thumbnail ready for chosen platform(s) | * | Check which platform(s) were chosen; verify `renders/thumbnail-<platform>-<size>.png` exists for each |
| Thumbnail text readable at small sizes (~168px wide) | * | Visually verify — zoom out the PNG to thumbnail size |
| Face (if present) is not clipped by gradient mask | — | Inspect thumbnail PNG |
| `JOURNAL.md` updated with this session | — | Check last entry date |
| Series spec followed (if series episode) | * | If applicable — `/series` check passed |

---

## Producing DELIVERY.md

After running all checks, create `DELIVERY.md` in the project folder:

```markdown
# Delivery Sign-off — <project-name>

**Date:** YYYY-MM-DD
**Platform:** [list only the platform(s) chosen in Gate 3]
**Renders:**
- `renders/<project>-<platform>.mp4` — Xs  (one line per rendered platform)

## Content
- [x] Hook lands within first 3 seconds
- [x] Single clear CTA
- [x] No banned words
- [x] Script approved (SCRIPT.md)
- [x] Captions word-accurate
- [x] Duration fits platform limits

## Brand
- [x] Source Serif 4 headings (weight 400)
- [x] Plus Jakarta Sans body
- [x] Brand colors only — no hardcoded hex
- [x] No `transparent` in gradients
- [x] Logo in outro
- [x] Double-bezel on elevated containers
- [x] No flat cards

## Technical
- [x] lint — zero errors
- [x] Studio preview reviewed
- [x] Draft render reviewed
- [x] Renders produced for chosen platform(s)
- [x] Durations match (if multiple 16:9 platforms rendered)
- [x] No Math.random() / Date.now()
- [x] No render-time network fetches

## Platform
- [x] Thumbnail ready for chosen platform(s)
- [x] Thumbnail readable at small sizes
- [x] JOURNAL.md updated

## Warnings (non-blocking)
- [list any [!] items that were noted but did not block]

---
✓ Cleared for upload.
```

---

## If any critical item fails

Do not produce `DELIVERY.md`. Instead:

1. List the failing items clearly
2. Fix each one — do not skip or mark as n/a unless it genuinely does not apply
3. Re-run the affected checks after fixing
4. Only produce `DELIVERY.md` when all critical items pass

A delivered video with a broken hook, wrong font, or missing thumbnail is worse than a delayed one.
