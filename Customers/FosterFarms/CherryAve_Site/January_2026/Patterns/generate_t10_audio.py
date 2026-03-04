#!/usr/bin/env python3
"""
Generate T10 Air Chiller audio narrations for Cherry Ave January 2026.
Uses OpenAI TTS-HD with 'shimmer' voice (Unity's voice).

Generates:
  T10_brief.mp3          - 60-second Unity Brief
  T10_explains_p1.mp3    - Part 1: Current State
  T10_explains_p2.mp3    - Part 2: MPTS Solution
  T10_explains_p3.mp3    - Part 3: Expected Results
  T10_waste_howto.mp3    - How to Read Energy Waste (Baseline)
  T10_savings_howto.mp3  - How to Read Energy Savings (MPTS)
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment
load_dotenv('/Users/mdhowell/eestream/.env')
client = OpenAI()

PATTERNS_DIR = Path(__file__).parent
MODEL = "tts-1-hd"
VOICE = "shimmer"


def generate_mp3(text: str, output_path: Path):
    """Generate a single MP3 from text using OpenAI TTS."""
    chars = len(text)
    print(f"  → Generating {output_path.name} ({chars} chars)")
    
    # OpenAI TTS limit is 4096 chars. If over, we need to chunk and concatenate.
    if chars > 4096:
        print(f"    ⚠ Text exceeds 4096 chars — chunking...")
        generate_chunked_mp3(text, output_path)
        return
    
    try:
        response = client.audio.speech.create(
            model=MODEL,
            voice=VOICE,
            input=text
        )
        response.stream_to_file(str(output_path))
        size_kb = output_path.stat().st_size / 1024
        print(f"    ✓ Saved ({size_kb:.0f} KB)")
    except Exception as e:
        print(f"    ✗ Error: {e}")
        sys.exit(1)


def generate_chunked_mp3(text: str, output_path: Path):
    """Generate MP3 from long text by chunking at sentence boundaries, then concatenating."""
    import subprocess
    import tempfile
    
    # Split into chunks at sentence boundaries, respecting 4096 char limit
    sentences = text.replace('\n\n', '\n').split('. ')
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        candidate = current_chunk + (". " if current_chunk else "") + sentence
        if len(candidate) > 3900 and current_chunk:
            chunks.append(current_chunk + ".")
            current_chunk = sentence
        else:
            current_chunk = candidate
    if current_chunk:
        chunks.append(current_chunk if current_chunk.endswith('.') else current_chunk + ".")
    
    print(f"    Split into {len(chunks)} chunks")
    
    # Generate each chunk
    chunk_files = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for i, chunk in enumerate(chunks):
            chunk_path = Path(tmpdir) / f"chunk_{i}.mp3"
            try:
                response = client.audio.speech.create(
                    model=MODEL,
                    voice=VOICE,
                    input=chunk
                )
                response.stream_to_file(str(chunk_path))
                chunk_files.append(chunk_path)
                print(f"    ✓ Chunk {i+1}/{len(chunks)} ({len(chunk)} chars)")
            except Exception as e:
                print(f"    ✗ Chunk {i+1} error: {e}")
                sys.exit(1)
        
        # Concatenate with ffmpeg if available, otherwise just use first chunk
        if len(chunk_files) == 1:
            import shutil
            shutil.copy2(str(chunk_files[0]), str(output_path))
        else:
            # Create file list for ffmpeg
            list_path = Path(tmpdir) / "filelist.txt"
            with open(list_path, 'w') as f:
                for cf in chunk_files:
                    f.write(f"file '{cf}'\n")
            
            try:
                subprocess.run([
                    'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
                    '-i', str(list_path),
                    '-c', 'copy', str(output_path)
                ], check=True, capture_output=True)
            except FileNotFoundError:
                # No ffmpeg — fall back to binary concatenation (works for MP3)
                with open(output_path, 'wb') as out:
                    for cf in chunk_files:
                        out.write(cf.read_bytes())
    
    size_kb = output_path.stat().st_size / 1024
    print(f"    ✓ Saved ({size_kb:.0f} KB)")


def main():
    print("\n🎙️  eeAUDIO — T10 Air Chiller, Cherry Ave, January 2026")
    print(f"   Model: {MODEL}  |  Voice: {VOICE}")
    print(f"   Output: {PATTERNS_DIR}\n")
    
    # 1. Unity Brief
    brief_text = (PATTERNS_DIR / "T10_brief.txt").read_text()
    generate_mp3(brief_text, PATTERNS_DIR / "T10_brief.mp3")
    
    # 2. Three-part narrative (split at --- markers)
    narrative_text = (PATTERNS_DIR / "T10_narrative.txt").read_text()
    parts = [p.strip() for p in narrative_text.split('---') if p.strip()]
    
    if len(parts) != 3:
        print(f"  ⚠ Expected 3 narrative parts, got {len(parts)} — using as-is")
    
    for i, part in enumerate(parts):
        # Strip the "PART N: TITLE" header line for cleaner audio
        lines = part.split('\n')
        # Keep the header for context but clean it
        clean_part = part
        generate_mp3(clean_part, PATTERNS_DIR / f"T10_explains_p{i+1}.mp3")
    
    # 3. Waste how-to-read
    waste_text = (PATTERNS_DIR / "T10_waste_howto.txt").read_text()
    generate_mp3(waste_text, PATTERNS_DIR / "T10_waste_howto.mp3")
    
    # 4. Savings how-to-read
    savings_text = (PATTERNS_DIR / "T10_savings_howto.txt").read_text()
    generate_mp3(savings_text, PATTERNS_DIR / "T10_savings_howto.mp3")
    
    # Summary
    print("\n✅ T10 audio generation complete!")
    print("   Files generated:")
    for f in sorted(PATTERNS_DIR.glob("T10_*.mp3")):
        size_kb = f.stat().st_size / 1024
        print(f"   • {f.name} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
