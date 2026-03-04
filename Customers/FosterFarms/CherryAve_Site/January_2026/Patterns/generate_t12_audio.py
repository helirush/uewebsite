#!/usr/bin/env python3
"""
Generate T12 Main audio narrations for Cherry Ave January 2026.
Uses OpenAI TTS-HD with 'shimmer' voice (Unity's voice).

Generates:
  T12_brief.mp3
  T12_explains_p1.mp3
  T12_explains_p2.mp3
  T12_explains_p3.mp3
  T12_waste_howto.mp3
  T12_savings_howto.mp3
"""

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

    if chars > 4096:
        print("    ⚠ Text exceeds 4096 chars — chunking...")
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
    """Generate MP3 from long text by chunking and concatenating."""
    import subprocess
    import tempfile

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

        if len(chunk_files) == 1:
            import shutil
            shutil.copy2(str(chunk_files[0]), str(output_path))
        else:
            list_path = Path(tmpdir) / "filelist.txt"
            with open(list_path, 'w') as f:
                for cf in chunk_files:
                    f.write(f"file '{cf}'\n")

            try:
                subprocess.run(
                    ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(list_path), '-c', 'copy', str(output_path)],
                    check=True,
                    capture_output=True
                )
            except FileNotFoundError:
                with open(output_path, 'wb') as out:
                    for cf in chunk_files:
                        out.write(cf.read_bytes())

    size_kb = output_path.stat().st_size / 1024
    print(f"    ✓ Saved ({size_kb:.0f} KB)")


def main():
    print("\n🎙️  eeAUDIO — T12 Main, Cherry Ave, January 2026")
    print(f"   Model: {MODEL}  |  Voice: {VOICE}")
    print(f"   Output: {PATTERNS_DIR}\n")

    brief_text = (PATTERNS_DIR / "T12_brief.txt").read_text()
    generate_mp3(brief_text, PATTERNS_DIR / "T12_brief.mp3")

    narrative_text = (PATTERNS_DIR / "T12_narrative.txt").read_text()
    parts = [p.strip() for p in narrative_text.split('---') if p.strip()]
    if len(parts) != 3:
        print(f"  ⚠ Expected 3 narrative parts, got {len(parts)} — using available parts")
    for i, part in enumerate(parts):
        generate_mp3(part, PATTERNS_DIR / f"T12_explains_p{i+1}.mp3")

    waste_text = (PATTERNS_DIR / "T12_waste_howto.txt").read_text()
    generate_mp3(waste_text, PATTERNS_DIR / "T12_waste_howto.mp3")

    savings_text = (PATTERNS_DIR / "T12_savings_howto.txt").read_text()
    generate_mp3(savings_text, PATTERNS_DIR / "T12_savings_howto.mp3")

    print("\n✅ T12 audio generation complete!")
    print("   Files generated:")
    for f in sorted(PATTERNS_DIR.glob("T12_*.mp3")):
        size_kb = f.stat().st_size / 1024
        print(f"   • {f.name} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
