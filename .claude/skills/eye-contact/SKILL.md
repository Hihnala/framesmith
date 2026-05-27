---
name: eye-contact
description: NVIDIA Eye Contact NIM — correct gaze toward camera in talking-head footage. Use when the user runs /eye-contact, asks to fix eye contact, or wants to redirect gaze toward the camera in a talking-head video. Run after retake removal, before audio enhancement.
---

# /eye-contact

Redirect gaze toward the camera in talking-head footage using the NVIDIA Eye Contact NIM preview API.

Run this step **after** retake removal (`tools/cut-retakes.py`), **before** audio enhancement (`tools/process-audio.py`).

---

## What the tool does

Three steps in sequence:

| Step | Action | Why |
|------|--------|-----|
| 1 | Convert input to CFR 30fps H.264 + faststart | NIM rejects VFR footage silently — this is the most common failure mode with camera footage |
| 2 | Clone `NVIDIA-Maxine/nim-clients` into `tools/nim-clients/` (first run only) | The NIM client library; cloned automatically, never committed |
| 3 | Send prepared video to `grpc.nvcf.nvidia.com:443` in streaming mode | NIM returns a video with gaze redirected; audio is preserved unchanged |

Flags used: `--detect-closure 1` (natural blinks), `--enable-lookaway 0` (gaze stays fixed on camera).

---

## Requirements

- `NVIDIA_API_KEY` in `video-projects/.env`
- `NVIDIA_EYE_CONTACT_FUNCTION_ID` in `video-projects/.env`
  → Find the function ID at: https://build.nvidia.com/nvidia/eyecontact/api (click API tab — it appears in the example snippet)
- `ffmpeg` (already required by Framesmith)
- Internet access (calls `grpc.nvcf.nvidia.com:443`)

---

## Usage

```bash
python tools/eye-contact.py \
  --input  video-projects/<name>/retakes-removed.mp4 \
  --output video-projects/<name>/eye-contact.mp4
```

Skip the CFR conversion if the input is already CFR H.264 (e.g. from a previous run):

```bash
python tools/eye-contact.py \
  --input        video-projects/<name>/retakes-removed.mp4 \
  --output       video-projects/<name>/eye-contact.mp4 \
  --skip-prepare
```

---

## File naming convention

Follow this naming sequence through the Level 3 pipeline:

```
raw.mp4                    → source footage
raw-silence-cut.mp4        → after silence-cut.sh
retakes-removed.mp4        → after cut-retakes.py
eye-contact.mp4            → after eye-contact.py       ← this tool
audio-processed.mp4        → after process-audio.py
renders/final.mp4          → after HyperFrames render
```

Use `eye-contact.mp4` as the input to `process-audio.py` and as the base video clip in HyperFrames compositions.

---

## Where it fits in the Level 3 pipeline

```
tools/silence-cut.sh           → removes silences
tools/transcribe-whisper.py    → word-level transcript
tools/cut-retakes.py           → removes duplicate takes
tools/eye-contact.py           ← run here
tools/process-audio.py         → audio enhancement
HyperFrames compositions       → build overlays on audio-processed.mp4
```

---

## Agent instructions

When the user runs `/eye-contact`:

1. Check that `NVIDIA_API_KEY` and `NVIDIA_EYE_CONTACT_FUNCTION_ID` are both set in `video-projects/.env`. If either is missing, stop and tell the user what's needed — the tool exits immediately without them.
2. Ask for the input file path if not already known (look for `retakes-removed.mp4` in the active project folder).
3. Propose the output path: same folder, filename `eye-contact.mp4`.
4. Confirm the command before running. Warn that first run will clone `nim-clients` (~a few seconds) and install its requirements.
5. After success, confirm the output path and tell the user the next step is `tools/process-audio.py --input eye-contact.mp4`.

If the user has not yet run retake removal, flag this. Eye contact correction should run on the final edited cut, not raw footage.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Tool exits immediately with `NVIDIA_API_KEY is not set` | Key not in `video-projects/.env` | Add `NVIDIA_API_KEY=nvapi-...` to `video-projects/.env` |
| Tool exits immediately with `NVIDIA_EYE_CONTACT_FUNCTION_ID is not set` | Function ID not set | Get it from build.nvidia.com/nvidia/eyecontact/api and add to `.env` |
| NIM returns an error with no useful message | Input was VFR — NIM rejects silently | The tool converts to CFR automatically; if using `--skip-prepare`, remove that flag |
| Output file missing or empty | API call failed | Check terminal output for gRPC error details; verify API key and function ID are correct |
| `git clone` fails on first run | No internet or git not installed | Check internet access; `brew install git` if needed |
| `pip install` fails on first run | Python environment issue | Run `pip install -r tools/nim-clients/eye-contact/requirements.txt` manually |
| `ffmpeg: command not found` | ffmpeg not installed | `brew install ffmpeg` |
| Gaze correction looks unnatural | Fast head movement or extreme off-axis angle | Normal — the NIM works best with moderate head movement; no fix available at API level |
