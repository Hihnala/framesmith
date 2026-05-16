# Tools

Framesmith includes seven shell and Python tools in the `tools/` directory. They handle the parts of video production that the HyperFrames CLI does not: raw footage editing, multi-platform rendering, and thumbnail export.

All shell scripts should be made executable once:

```bash
chmod +x tools/silence-cut.sh tools/render-all.sh tools/extract-frame.sh tools/thumbnail-render.sh
```

---

## Python tools

Install Python dependencies before using:

```bash
pip install -r tools/requirements.txt
```

### transcribe-whisper.py

**Local word-level transcription using faster-whisper.**

```bash
python tools/transcribe-whisper.py video-projects/<name>/raw-silence-cut.mp4
```

Loads the `base` Whisper model (CPU, int8) and transcribes the audio with word-level timestamps. Prints segment text to the terminal as it processes.

**Outputs:**

- `<file>.transcript.json` — full word-level transcript with start/end times per word
- `<file>.transcript.txt` — human-readable segments with `[start → end] text`

**When to use:** after cutting silence from raw footage, before deciding on retake cuts. The transcript is your roadmap for `cut-retakes.py`.

**Notes:**
- English only. For other languages, use ElevenLabs Scribe via `npx hyperframes transcribe --json` (requires `ELEVENLABS_API_KEY`).
- First run downloads the model (~150MB). Subsequent runs are fast.
- No API key required — runs entirely offline.

---

### cut-retakes.py

**Apply the last-take rule: keep only the final good take of each sentence.**

This is not an automatic tool — it requires you to read the transcript first and decide which ranges to keep.

**Workflow:**

1. Read the transcript (`.transcript.txt`) and identify which takes you want
2. Open `tools/cut-retakes.py` and edit the configuration at the top:

```python
IN  = Path("video-projects/<name>/raw-silence-cut.mp4")
OUT = Path("video-projects/<name>/edit.mp4")

KEEPS = [
    (0.0, 14.36),   # Sentence 1 — best take
    (14.65, 17.64), # Sentence 2 — best take
    (17.82, 21.32), # Sentence 3 — best take
]
```

3. Run: `python tools/cut-retakes.py`

**Output:** `video-projects/<name>/edit.mp4` — the final edited video that becomes the source of truth for all composition timing.

**After running:** always measure the output duration:

```bash
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  video-projects/<name>/edit.mp4
```

This number is `data-duration` for your root composition.

**Notes:**
- Pads are not added automatically — bake them into the start and end times in `KEEPS`
- Uses libx264 with CRF 18 and tight 1s GOP keyframes for accurate HyperFrames seeking
- Requires FFmpeg on PATH

---

### process-audio.py

Enhances the audio of a talking-head video using a two-pass EBU R128 loudnorm
chain. Run after `cut-retakes.py`, on the final edited video.

**No additional dependencies.** Requires only ffmpeg, which Framesmith already requires.

### Filter chain

| Order | Filter | Purpose |
|-------|--------|---------|
| 1 | High-pass at 80 Hz | Removes clothing rustle, HVAC hum, surface vibration |
| 2 | Compression (3:1, -18 dBFS) | Evens out conversational speech dynamics |
| 3 | EBU R128 loudnorm (-16 LUFS) | YouTube-standard loudness, -1 dBTP ceiling |
| 4 | Limiter (-1 dBTP) | Hard true-peak safety ceiling |

### Usage

```bash
# Voice only
python tools/process-audio.py \
  --input  video-projects/my-project/edited.mp4 \
  --output video-projects/my-project/audio-processed.mp4

# With ambient pad (recommended)
python tools/process-audio.py \
  --input  video-projects/my-project/edited.mp4 \
  --output video-projects/my-project/audio-processed.mp4 \
  --pad    assets/ambient-pad.mp3

# Custom pad level
python tools/process-audio.py \
  --input      video-projects/my-project/edited.mp4 \
  --output     video-projects/my-project/audio-processed.mp4 \
  --pad        assets/ambient-pad.mp3 \
  --pad-volume -24
```

### Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--input` | Yes | — | Input video file (post-edit) |
| `--output` | Yes | — | Output file with processed audio |
| `--pad` | No | None | Ambient pad file to mix under voice |
| `--pad-volume` | No | `-22` | Pad mix level in dB |

### Notes

- The video stream is copied without re-encoding (`-c:v copy`).
- Designed for mics with built-in ENC (Hollyland Lark M2 etc.). Does not add noise reduction, de-essing, or fine EQ.
- The pad is looped automatically to match the video length.
- To change the loudness target (e.g. -23 LUFS for broadcast), edit `TARGET_LUFS` at the top of the script. No other changes needed.
- Claude Code users: run as `/process-audio`.

---

## Shell tools

### silence-cut.sh

**Remove silences from a raw recording using ffmpeg.**

This is a template script — you edit it before each use.

**Workflow:**

1. First, detect silences (this does not encode — it only prints):

```bash
ffmpeg -i "video-projects/<name>/raw.mp4" \
  -af "silencedetect=noise=-32dB:d=0.25" -f null - 2>&1 | grep silence
```

The output looks like:
```
silence_start: 14.36
silence_end: 14.65 | silence_duration: 0.29
silence_start: 17.64
silence_end: 17.82 | silence_duration: 0.18
```

2. From the silence markers, calculate keep ranges — the segments of non-silent audio you want to keep, with a 0.1s pad on each edge

3. Open `tools/silence-cut.sh` and edit the top section:

```bash
IN="video-projects/<name>/raw.mp4"
OUT="video-projects/<name>/raw-silence-cut.mp4"
```

4. Update the `filter_complex` section with your keep ranges (the template has three example ranges — replace them with yours)

5. Update `concat=n=<count>` to match the number of keep ranges

6. Run: `bash tools/silence-cut.sh`

**Output:** `video-projects/<name>/raw-silence-cut.mp4`

**Tunable knobs (edit inside the script):**
- `silencedetect=noise=-32dB` — threshold: -30dB is more aggressive, -35dB more lenient
- `d=0.25` — minimum silence duration to detect; lower catches shorter pauses
- `-r 30` — output frame rate; match your composition (24 or 30)
- `-crf 18` — quality: lower = better (18 is high quality, 23 is good)

**Notes:**
- Run `silence-cut.sh` before `transcribe-whisper.py` — transcribe the cut file, not the raw
- The output uses tight 1s GOP keyframes for accurate HyperFrames seeking
- Requires FFmpeg on PATH

---

### render-all.sh

**Render to all configured platform formats in one pass.**

```bash
# Run from inside the project folder
cd video-projects/<name>
bash ../../tools/render-all.sh
```

**What it produces:**

| File | Quality | Platform |
| --- | --- | --- |
| `renders/<name>-youtube.mp4` | high (CRF 15) | YouTube |
| `renders/<name>-linkedin.mp4` | standard (CRF 18) | LinkedIn |
| `renders/<name>-tiktok.mp4` | standard (CRF 18) | TikTok/Reels (only if `index-vertical.html` exists) |

After rendering, the script measures the YouTube and LinkedIn durations and warns if they differ by more than 0.1 seconds — a sign that the two compositions have diverged.

**Adding TikTok/Reels:** create `index-vertical.html` (1080×1920) in the project folder. The script detects it automatically on the next run. If it does not exist, TikTok is skipped with a note.

**Notes:**
- Must be run from inside the project folder (the CLI reads `meta.json` and `hyperframes.json` relative to `$PWD`)
- Requires Node.js ≥ 22, FFmpeg, and Chrome (bundled by HyperFrames)
- Render time scales with video length and machine speed — `--quality high` takes roughly 2× longer than `--quality standard`

---

### extract-frame.sh

**Extract a single frame from a rendered video at a given timestamp.**

```bash
# Run from inside the project folder
bash ../../tools/extract-frame.sh renders/<name>-youtube.mp4 12.5
```

**Output:** `renders/<name>-youtube-frame-12.5s.png`

Use this to:
- Find a strong candidate frame before building the dedicated thumbnail composition
- Generate a quick reference image at any point in the video
- Verify that a specific beat or caption lands correctly

**Notes:**
- Timestamp is in seconds (decimal allowed)
- Uses `-q:v 1` for maximum PNG quality
- Requires FFmpeg on PATH

---

### thumbnail-render.sh

**Render ****`thumbnail.html`**** to YouTube and LinkedIn PNGs.**

```bash
# Run from inside the project folder — thumbnail.html must exist first
bash ../../tools/thumbnail-render.sh
```

**What it does:**

1. Renders `thumbnail.html` as a 1-second MP4 at high quality
2. Extracts the frame at t=0.5 seconds (fully animated, safe from entrance transitions)
3. Saves as `renders/thumbnail-youtube-1280x720.png`
4. Scales to LinkedIn dimensions: `renders/thumbnail-linkedin-1200x627.png`
5. Removes the intermediate MP4

**Output:**

| File | Dimensions | Platform |
| --- | --- | --- |
| `renders/thumbnail-youtube-1280x720.png` | 1280×720 | YouTube |
| `renders/thumbnail-linkedin-1200x627.png` | 1200×627 | LinkedIn |

**Before running:** lint `thumbnail.html` first:

```bash
npx hyperframes lint thumbnail.html
```

**Notes:**
- `thumbnail.html` must be a valid HyperFrames composition with `data-width="1280"` and `data-height="720"`
- If the entrance animations are longer than 0.5 seconds, adjust the extraction timestamp in the script
- Requires Node.js ≥ 22, FFmpeg, and Chrome

---

## Tool sequence for Level 3 videos

```
raw.mp4
  1. bash tools/silence-cut.sh              → raw-silence-cut.mp4
  2. python tools/transcribe-whisper.py     → .transcript.json + .transcript.txt
  3. python tools/cut-retakes.py            → edit.mp4
  4. python tools/process-audio.py          → audio-processed.mp4
     [Build composition from audio-processed.mp4]
  5. bash ../../tools/render-all.sh         → youtube.mp4 + linkedin.mp4
  6. [Build thumbnail.html]
     bash ../../tools/thumbnail-render.sh   → thumbnail-youtube.png + thumbnail-linkedin.png
```

Steps 1–4 are run from the workspace root (paths in the scripts reference the project folder).
Steps 5–6 are run from inside the project folder.
