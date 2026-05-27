---
name: video-pipeline
description: Level 3 guided video pipeline for Framesmith. Use when the user has raw footage, a screen recording, or a talking-head video that needs to be edited and turned into a finished MP4 with HyperFrames motion overlays. Covers the full pipeline: silence-cut → transcribe → retake-cut → ElevenLabs Scribe (optional) → HyperFrames composition → final render.
---

# Video Pipeline — Level 3 Guided Video

Full production pipeline for raw footage → finished MP4.

## Pipeline overview

```
raw.mp4
  └── Step 1: Silence cut        → raw-silence-cut.mp4
  └── Step 2: Transcribe         → .transcript.json + .transcript.txt
  └── Step 3: Retake cut         → retakes-removed.mp4
  └── Step 3.5: Eye contact      → eye-contact.mp4  (optional — NVIDIA Eye Contact NIM)
  └── Step 4: Storyboard overlays → plan scenes and motion graphic beats
  └── Step 5: HyperFrames build  → index.html + compositions/
  └── Step 6: Lint + preview     → Studio at localhost:3002
  └── Step 7: Draft render       → renders/draft.mp4
  └── Step 8: Final render       → renders/final.mp4
```

**Audio is the source of truth.** Edit audio first. All composition timing anchors to the edited video's duration.

---

## Step 1: Silence cut

Run the silence detector first to identify where silences are:

```bash
ffmpeg -i "video-projects/<name>/raw.mp4" \
  -af "silencedetect=noise=-32dB:d=0.25" -f null - 2>&1 | grep silence
```

This prints silence start/end times. From those, calculate keep ranges (non-silent segments + 0.1s pad).

Then edit `tools/silence-cut.sh`:
- Set `IN` and `OUT` paths
- Update `filter_complex` with your keep ranges
- Update `n=<count>` in the concat line

```bash
bash tools/silence-cut.sh
```

Output: `video-projects/<name>/raw-silence-cut.mp4`

---

## Step 2: Transcribe

### Option A — faster-whisper (local, free, English)

```bash
python tools/transcribe-whisper.py video-projects/<name>/raw-silence-cut.mp4
```

Outputs: `.transcript.json` (word-level with timestamps) and `.transcript.txt` (human-readable).

### Option B — ElevenLabs Scribe (multilingual, speaker diarization)

Use when: non-English content, multiple speakers, or you need high-accuracy timestamps for karaoke captions.

Requires `ELEVENLABS_API_KEY` in `video-projects/.env`.

```bash
# HyperFrames CLI wraps ElevenLabs Scribe:
npx hyperframes transcribe video-projects/<name>/raw-silence-cut.mp4 --json
```

Or use the ElevenLabs API directly for diarization:

```python
import httpx, os, pathlib
key = os.environ["ELEVENLABS_API_KEY"]
audio = pathlib.Path("video-projects/<name>/raw-silence-cut.mp4").read_bytes()
r = httpx.post(
    "https://api.elevenlabs.io/v1/speech-to-text",
    headers={"xi-api-key": key},
    files={"audio": ("audio.mp4", audio, "video/mp4")},
    data={"model_id": "scribe_v1", "timestamps_granularity": "word"},
    timeout=120,
)
print(r.json())
```

---

## Step 3: Retake cut (last-take rule)

Review the transcript. Identify which takes to keep (the last good take for each sentence).

Edit `tools/cut-retakes.py`:
- Set `IN` = `raw-silence-cut.mp4`
- Set `OUT` = `edit.mp4`
- Fill `KEEPS` list with `(start, end)` tuples from the transcript

```bash
python tools/cut-retakes.py
```

Output: `video-projects/<name>/edit.mp4`

**Measure the final duration** — this is the composition's `data-duration`:
```bash
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  video-projects/<name>/edit.mp4
```

---

## Step 4: Storyboard motion graphic overlays

Before writing composition HTML, storyboard the motion overlay:

1. Read the transcript — identify natural scene breaks (topic changes, pauses)
2. Plan one overlay per scene (title card, data point, visual beat)
3. Map each overlay's `data-start` to edited-video timestamps
4. Read `DESIGN.md` and `MOTION_PHILOSOPHY.md` before designing any scene

Rule: **All timestamps must be in edited-video time**, not original recording time.

---

## Step 5: HyperFrames composition

Scaffold the project if not already done:

```bash
cd video-projects
npx hyperframes init <name> --video <name>/edit.mp4 --non-interactive
cd <name>
```

For talking-head + motion overlay, use the four-layer scaffold:

```
index.html (root, 1920×1080, data-composition-id="main")
├── ambient-bg.html        track-index="3" — brand bg + grain + vignette
├── face-video.html        track-index="0" — edit.mp4 talking head
├── scene1-<label>.html    track-index="1" — overlay scenes (back-to-back)
├── scene2-<label>.html    track-index="1"
└── captions.html          track-index="2" — word-synced captions (optional)
```

Invoke `/hyperframes` for composition authoring rules.
Invoke `/short-form-video` for 9:16 vertical with face-mode choreography.

---

## Step 6: Lint

Always lint before rendering. Zero errors required.

```bash
cd video-projects/<name>
npx hyperframes lint
```

Fix all errors before proceeding.

---

## Step 7: Studio preview → Draft render

```bash
npx hyperframes preview          # Studio at localhost:3002
```

Review live. Then draft render:

```bash
npx hyperframes render --quality draft --output renders/draft.mp4
```

Scrub the draft. Verify:
- Captions are word-accurate
- Overlays land on the right beats
- Pacing matches the transcript
- Brand (colors, fonts, logo) is correct

---

## Step 8: Final render

After draft is approved:

```bash
npx hyperframes render --quality standard --output renders/final.mp4
```

For delivery quality:

```bash
npx hyperframes render --quality high --fps 30 --output renders/final-hq.mp4
```

---

## Critical rules

1. **Never mix original-time and edited-time timestamps** in the same composition.
2. **Audio is a separate `<audio>` element** from the `<video>` element — HyperFrames mixer needs them separate.
3. **`class="clip"` never goes on `<video>` or `<audio>`** — only on wrapper divs.
4. **Every GSAP timeline ends with a no-op duration anchor:**
   ```js
   tl.to({}, { duration: SLOT_DURATION }, 0);
   ```
5. **No `Math.random()` or `Date.now()`** — compositions must be deterministic.
6. **One `<audio>` element per source file** — prevents echo on re-render.
