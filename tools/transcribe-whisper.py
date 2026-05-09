"""
transcribe-whisper.py — Word-level transcription using faster-whisper.

Usage:
    python tools/transcribe-whisper.py video-projects/<name>/raw.mp4

Outputs:
    <file>.transcript.json  — full word-level transcript with timestamps
    <file>.transcript.txt   — human-readable with timestamps per segment

Requirements:
    pip install faster-whisper  (or: pip install -r tools/requirements.txt)
"""

import json
import sys
from pathlib import Path
from faster_whisper import WhisperModel

if len(sys.argv) < 2:
    sys.exit("Usage: python tools/transcribe-whisper.py <video.mp4>")

VIDEO = Path(sys.argv[1])
OUT_JSON = VIDEO.with_suffix(".transcript.json")
OUT_TXT = VIDEO.with_suffix(".transcript.txt")

print("Loading model (base, cpu, int8)...", flush=True)
model = WhisperModel("base", device="cpu", compute_type="int8")

print(f"Transcribing {VIDEO.name}...", flush=True)
segments, info = model.transcribe(
    str(VIDEO),
    language="en",
    word_timestamps=True,
    vad_filter=False,
)

segs = []
lines = []
for s in segments:
    seg = {
        "id": s.id,
        "start": round(s.start, 2),
        "end": round(s.end, 2),
        "text": s.text.strip(),
        "words": [
            {"start": round(w.start, 2), "end": round(w.end, 2), "word": w.word}
            for w in (s.words or [])
        ],
    }
    segs.append(seg)
    lines.append(f"[{seg['start']:6.2f} -> {seg['end']:6.2f}] {seg['text']}")
    print(lines[-1], flush=True)

OUT_JSON.write_text(
    json.dumps(
        {"info": {"duration": info.duration, "language": info.language}, "segments": segs},
        indent=2,
    )
)
OUT_TXT.write_text("\n".join(lines))
print(f"\nWrote: {OUT_JSON}\nWrote: {OUT_TXT}", flush=True)
