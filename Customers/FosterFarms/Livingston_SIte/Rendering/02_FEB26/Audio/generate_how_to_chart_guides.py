#!/usr/bin/env python3
"""Generate reusable how-to chart guide MP3 files using OpenAI TTS."""

import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv(os.path.expanduser("~/eestream/.env"))

client = OpenAI()

SCRIPT_DIR = Path(__file__).parent

GUIDE_FILES = [
    ("how-to-read-waste-chart.txt", "how-to-read-waste-chart.mp3"),
    ("how-to-read-savings-chart.txt", "how-to-read-savings-chart.mp3"),
]

for txt_name, mp3_name in GUIDE_FILES:
    input_file = SCRIPT_DIR / txt_name
    output_file = SCRIPT_DIR / mp3_name

    text = input_file.read_text().strip()
    print(f"{txt_name}: {len(text)} chars")

    if len(text) > 4096:
        raise ValueError(f"Text too long in {txt_name} ({len(text)} chars). Max is 4096.")

    print(f"Generating {mp3_name} ...")
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="shimmer",
        input=text,
    )

    response.stream_to_file(str(output_file))
    size_kb = output_file.stat().st_size / 1024
    print(f"Done! {mp3_name} — {size_kb:.0f} KB")
