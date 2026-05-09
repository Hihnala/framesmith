---
name: series
description: Manage video series — define series specs, start new episodes, check consistency, and track episode history. Use when the user says "new episode", "this is part of a series", "series check", "add to the series", or when starting a project that belongs to a recurring format. Series definitions live in series.json at the workspace root.
---

# Series Management

Maintains consistency across episodes of a recurring video series. Series specs define the structural and brand constraints that every episode must follow — intro/outro timing, lower-third position, caption style, CTA, title format. Episodes are tracked in `series.json`.

---

## series.json

Located at the workspace root. Create it if it does not exist.

```json
{
  "series": {
    "<series-id>": {
      "name": "Series display name",
      "description": "One sentence on what this series is about",
      "platform": ["youtube", "linkedin"],
      "type": "educational",
      "cadence": "weekly",

      "intro": {
        "composition": "compositions/shared/intro.html",
        "duration": 3.0,
        "note": "Ember flash opener, logo reveal, series title card"
      },

      "outro": {
        "composition": "compositions/shared/outro.html",
        "duration": 6.0,
        "note": "Hold on brand card, logo, CTA line, 4–6s still"
      },

      "lower_third": {
        "enabled": true,
        "name": "Markku Hihnala",
        "title": "AI Strategy",
        "position": "bottom-left",
        "appears_at": 2.0,
        "duration": 4.0,
        "track_index": 4
      },

      "captions": {
        "enabled": true,
        "style": "corporate",
        "font": "Plus Jakarta Sans",
        "size": "28px",
        "color": "#F5F5F7",
        "accent_color": "#FF6A1A",
        "position": "bottom-center",
        "track_index": 2
      },

      "cta": "Clarity before commitment — hihnala.com",

      "title_format": "EP{N:02d}: {title}",

      "episodes": []
    }
  }
}
```

---

## Starting a new episode

When the user says this video belongs to a series:

1. Read `series.json` — load the matching series spec
2. Confirm the episode title and number (auto-increment from last episode in `series.json`)
3. Apply the spec to the project:
   - Copy shared intro/outro compositions if they exist (`compositions/shared/`)
   - Wire intro and outro into `index.html` with the correct `data-start`, `data-duration`, `data-track-index`
   - Set up lower-third with spec values
   - Set up captions with spec style
   - Use the CTA line from the spec in `SCRIPT.md`
4. Generate the episode title using `title_format`
5. Record the episode in `series.json` before building:

```json
"episodes": [
  {
    "number": 1,
    "title": "Episode title",
    "project": "video-projects/<name>",
    "date": "YYYY-MM-DD",
    "status": "in-progress",
    "platforms": {
      "youtube": { "url": null, "published": null },
      "linkedin": { "url": null, "published": null }
    }
  }
]
```

---

## Series consistency check

Run before delivery on any series episode. Compare the project against the series spec:

### Check 1 — Intro timing
Verify the root composition's first sub-composition matches `intro.duration` from the spec.

```bash
npx hyperframes compositions   # check the intro comp's data-duration
```

### Check 2 — Outro timing
Verify the outro sub-composition duration and that it contains a held still for ≥4s.

### Check 3 — Lower-third position and timing
Confirm the lower-third appears at `appears_at` ± 0.2s and uses the correct name and title.

### Check 4 — Caption style
Search the captions composition for font, size, and color values. They must match the spec exactly.

### Check 5 — CTA line
Search `SCRIPT.md` and the outro composition for the CTA line. Must match spec verbatim.

### Check 6 — Title format
Confirm the episode title follows `title_format` — correct episode number, correct format.

Report any deviation as a blocking issue. Do not pass the series check if any item fails.

---

## After delivery — update episode record

When `DELIVERY.md` is signed off, update the episode in `series.json`:

```json
{
  "number": 1,
  "title": "Episode title",
  "project": "video-projects/<name>",
  "date": "YYYY-MM-DD",
  "status": "delivered",
  "platforms": {
    "youtube": { "url": null, "published": null },
    "linkedin": { "url": null, "published": null }
  }
}
```

Update `url` and `published` date when the video is uploaded.

---

## Shared compositions

Store reusable intro/outro compositions in `video-projects/shared/`:

```
video-projects/shared/
├── intro.html          ← series intro (brand reveal, ~3s)
├── outro.html          ← series outro (CTA card, hold, ~6s)
└── lower-third.html    ← lower-third template
```

Each project copies what it needs into its own `compositions/` folder — never reference shared compositions via relative path across projects. Keep each project self-contained and portable.

When the shared compositions change (rebrand, new CTA), update `series.json` with a `last_updated` timestamp and a change note so future episodes use the correct version.

---

## Listing series and episodes

When the user asks "what series do I have" or "what episodes are done":

Read `series.json` and summarise:

```
Series: Hihnala Weekly (youtube, linkedin)
  EP01: "AI Strategy for Small Business" — delivered 2026-05-15
  EP02: "The Clarity Framework" — in-progress
  EP03: [not started]
```

---

## Creating a new series

When the user says "start a new series":

Ask:
1. Series name and ID (e.g. `hihnala-weekly`)
2. Platform(s)
3. Video type (educational / thought leadership / personal)
4. Cadence (weekly / bi-weekly / monthly / irregular)
5. Intro duration (default: 3s)
6. Outro duration (default: 6s)
7. Lower-third: name, title, position, timing
8. Caption style (corporate / hype / minimal)
9. CTA line (default: "Clarity before commitment — hihnala.com")
10. Title format (default: `EP{N:02d}: {title}`)

Add the new series to `series.json` before building the first episode.
