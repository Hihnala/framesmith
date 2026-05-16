# /process-audio

Enhance the audio of a talking-head video using `tools/process-audio.py`.

Run this skill **after** silence cutting and retake removal, **before** building HyperFrames compositions. It processes the final edited video, not raw footage.

---

## What the tool does

Four filters applied in this order:

| Step | Filter | What it fixes |
|------|--------|--------------|
| 1 | High-pass at 80 Hz | Clothing rustle, HVAC hum, surface vibration |
| 2 | Light compression (3:1, -18 dBFS threshold) | Peaks-and-valleys in conversational speech |
| 3 | EBU R128 loudnorm, -16 LUFS, -1 dBTP ceiling | YouTube-standard loudness (two-pass, linear) |
| 4 | Limiter at -1 dBTP | Hard safety ceiling after normalization |

The video stream is copied without re-encoding. Audio is output as AAC 256 kbps.

---

## Usage

```bash
# Voice processing only
python tools/process-audio.py \
  --input  video-projects/my-project/edited.mp4 \
  --output video-projects/my-project/audio-processed.mp4

# With ambient pad (recommended — masks residual hiss at -22 dB)
python tools/process-audio.py \
  --input  video-projects/my-project/edited.mp4 \
  --output video-projects/my-project/audio-processed.mp4 \
  --pad    assets/ambient-pad.mp3

# Custom pad level (default is -22 dB)
python tools/process-audio.py \
  --input      video-projects/my-project/edited.mp4 \
  --output     video-projects/my-project/audio-processed.mp4 \
  --pad        assets/ambient-pad.mp3 \
  --pad-volume -24
```

---

## Where it fits in the Level 3 pipeline

```
tools/silence-cut.sh           cut silence from raw footage
tools/transcribe-whisper.py    transcribe for caption timing
tools/cut-retakes.py           remove retakes
tools/process-audio.py         ← run here, on the final edited video
HyperFrames compositions       build overlays on the processed video
```

Use `audio-processed.mp4` as the base video clip in your root `index.html`. Do not apply further normalization inside HyperFrames.

---

## Agent instructions

When the user runs `/process-audio`:

1. Ask for the input file path if not already known (look in the active project folder under `video-projects/`).
2. Propose the output path: same folder, filename `audio-processed.mp4`.
3. Ask whether to include the ambient pad (`assets/ambient-pad.mp3`). Default: yes.
4. Confirm the command before running.
5. After success, report the output path and confirm the audio is ready for the HyperFrames composition step.

If the user has not yet run silence cutting and retake removal, flag this. The tool should run on the final edit, not raw footage.

---

## Lark M2 note

The Hollyland Lark M2 records at 24-bit/48 kHz with Environmental Noise Cancellation (ENC) active by default. The tool does not add a noise reduction pass — stacking noise reduction on top of ENC introduces artefacts. The high-pass filter and compression chain are calibrated for a mic that is already clean at capture.

If you disable ENC on the transmitter before recording (via the LarkSound app), the raw audio will have more ambient noise. The tool's chain still works, but the result will have a slightly higher noise floor than ENC-on recordings. In that case, reduce the pad volume a few dB to compensate.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| `ffmpeg: command not found` | ffmpeg not installed | `brew install ffmpeg` |
| Output audio is louder than expected | Input was very quiet; loudnorm lifts it correctly | Normal — the tool targets -16 LUFS |
| Output audio is quieter than expected | Input was already near target; no lift needed | Normal — loudnorm is accurate |
| Pad ends before video ends | Should not happen; pad is looped automatically | Check that `--pad` path is correct |
| ffmpeg error on filter_complex | Input has no audio stream | Verify the input file has an audio track |

To change the loudness target (e.g. for Spotify at -14 LUFS or broadcast at -23 LUFS), edit `TARGET_LUFS` in the script header. No other changes needed.
