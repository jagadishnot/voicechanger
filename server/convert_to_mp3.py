#!/usr/bin/env python3
"""
Script to convert WAV audio samples to MP3 format for better web compatibility
"""

import os
import sys
from pathlib import Path

try:
    from pydub import AudioSegment
    PYDUB_AVAILABLE = True
except ImportError:
    PYDUB_AVAILABLE = False
    print("pydub not available. Install with: pip install pydub")

def convert_wav_to_mp3(wav_path, mp3_path):
    """Convert a WAV file to MP3"""
    if not PYDUB_AVAILABLE:
        return False
    
    try:
        # Load WAV file
        audio = AudioSegment.from_wav(wav_path)
        
        # Export as MP3
        audio.export(mp3_path, format="mp3", bitrate="128k")
        
        print(f"Converted: {wav_path} -> {mp3_path}")
        return True
        
    except Exception as e:
        print(f"Error converting {wav_path}: {e}")
        return False

def convert_all_samples():
    """Convert all WAV samples to MP3"""
    
    # Get samples directory
    samples_dir = Path(__file__).parent / "static" / "samples"
    
    if not samples_dir.exists():
        print(f"Samples directory not found: {samples_dir}")
        return
    
    # Find all WAV files
    wav_files = list(samples_dir.glob("*.wav"))
    
    if not wav_files:
        print("No WAV files found in samples directory")
        return
    
    print(f"Found {len(wav_files)} WAV files to convert")
    
    converted_count = 0
    
    for wav_file in wav_files:
        # Create MP3 filename
        mp3_file = wav_file.with_suffix('.mp3')
        
        # Skip if MP3 already exists
        if mp3_file.exists():
            print(f"MP3 already exists: {mp3_file.name}")
            converted_count += 1
            continue
        
        # Convert WAV to MP3
        if convert_wav_to_mp3(str(wav_file), str(mp3_file)):
            converted_count += 1
    
    print(f"\nConversion complete! {converted_count} files processed.")
    
    if not PYDUB_AVAILABLE:
        print("\nTo convert audio files, install pydub and ffmpeg:")
        print("pip install pydub")
        print("Also install ffmpeg for MP3 support")

if __name__ == "__main__":
    convert_all_samples()