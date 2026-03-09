#!/usr/bin/env python3
"""Generate all transformer audio MP3s using OpenAI TTS (shimmer voice)."""

import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv(os.path.expanduser("~/eestream/.env"))

client = OpenAI()

SCRIPT_DIR = Path(__file__).parent

# All transformer audio files to generate
AUDIO_FILES = [
    # REND1
    "REND1_brief",
    "REND1_explains_p1",
    "REND1_explains_p2",
    "REND1_explains_p3",
    "REND1_waste_howto",
    "REND1_savings_howto",
    # REND2
    "REND2_brief",
    "REND2_explains_p1",
    "REND2_explains_p2",
    "REND2_explains_p3",
    "REND2_waste_howto",
    "REND2_savings_howto",
    # REND3
    "REND3_brief",
    "REND3_explains_p1",
    "REND3_explains_p2",
    "REND3_explains_p3",
    "REND3_waste_howto",
    "REND3_savings_howto",
]

def generate_audio(name):
    """Generate MP3 from text file."""
    input_file = SCRIPT_DIR / f"{name}.txt"
    output_file = SCRIPT_DIR / f"{name}.mp3"
    
    if not input_file.exists():
        print(f"⚠️  Skipping {name} - text file not found")
        return False
    
    if output_file.exists():
        print(f"⏭️  Skipping {name} - MP3 already exists")
        return True
    
    text = input_file.read_text().strip()
    
    if len(text) > 4096:
        print(f"❌ {name}: Text too long ({len(text)} chars)")
        return False
    
    print(f"🎤 Generating {name}.mp3 ({len(text)} chars)...")
    
    try:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="shimmer",
            input=text,
        )
        response.stream_to_file(str(output_file))
        size_kb = output_file.stat().st_size / 1024
        print(f"   ✅ Done! {size_kb:.0f} KB")
        return True
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Unity Energy Audio Generator - Study260305r0 Rendering")
    print("=" * 60)
    print()
    
    success = 0
    failed = 0
    
    for name in AUDIO_FILES:
        if generate_audio(name):
            success += 1
        else:
            failed += 1
    
    print()
    print("=" * 60)
    print(f"Complete! {success} generated, {failed} failed/skipped")
    print("=" * 60)
