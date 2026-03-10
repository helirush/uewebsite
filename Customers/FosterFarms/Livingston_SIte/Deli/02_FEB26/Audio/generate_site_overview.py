#!/usr/bin/env python3
"""Generate site overview MP3 using OpenAI TTS (shimmer voice)."""

import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv(os.path.expanduser("~/eestream/.env"))

client = OpenAI()

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "site_overview.txt"
OUTPUT_FILE = SCRIPT_DIR / "site_overview.mp3"

text = INPUT_FILE.read_text().strip()
print(f"Text length: {len(text)} chars")

# OpenAI TTS limit is 4096 chars; this script should be well under
if len(text) > 4096:
    raise ValueError(f"Text too long ({len(text)} chars). Max is 4096.")

print("Generating site_overview.mp3 ...")
response = client.audio.speech.create(
    model="tts-1-hd",
    voice="shimmer",
    input=text,
)

response.stream_to_file(str(OUTPUT_FILE))
size_kb = OUTPUT_FILE.stat().st_size / 1024
print(f"Done! {OUTPUT_FILE.name} — {size_kb:.0f} KB")
