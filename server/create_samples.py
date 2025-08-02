#!/usr/bin/env python3
"""
Script to create sample audio files for celebrity voice previews.
This creates simple text-to-speech samples for demonstration purposes.
"""

import os
import sys
from pathlib import Path

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("pyttsx3 not available. Install with: pip install pyttsx3")

def create_sample_audio(celebrity_id, celebrity_name, text, output_path):
    """Create a sample audio file using text-to-speech"""
    if not TTS_AVAILABLE:
        print(f"Skipping {celebrity_name} - TTS not available")
        return False
    
    try:
        engine = pyttsx3.init()
        
        # Adjust voice properties for variety
        voices = engine.getProperty('voices')
        if voices:
            # Use different voices for different celebrities
            voice_index = hash(celebrity_id) % len(voices)
            engine.setProperty('voice', voices[voice_index].id)
        
        # Adjust rate and volume
        engine.setProperty('rate', 150 + (hash(celebrity_id) % 50))  # 150-200 WPM
        engine.setProperty('volume', 0.8)
        
        # Save to file
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        
        print(f"Created sample for {celebrity_name}: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error creating sample for {celebrity_name}: {e}")
        return False

def create_all_samples():
    """Create sample audio files for all celebrities"""
    
    # Import celebrity data
    sys.path.append(os.path.dirname(__file__))
    from celebrities import get_all_celebrities
    
    # Create samples directory
    samples_dir = Path(__file__).parent / "static" / "samples"
    samples_dir.mkdir(parents=True, exist_ok=True)
    
    celebrities = get_all_celebrities()
    
    # Sample texts for different celebrities
    sample_texts = {
        "amitabh_bachchan": "Hello, this is a voice sample. I am the legendary actor of Indian cinema.",
        "shah_rukh_khan": "Hi there! This is a preview of my voice. Welcome to the world of Bollywood.",
        "aamir_khan": "Greetings! This is a sample of my voice for the voice changer application.",
        "salman_khan": "Hey everyone! This is how my voice sounds. Ready for some action?",
        "deepika_padukone": "Hello! This is a voice sample showcasing the elegance of Indian cinema.",
        "priyanka_chopra": "Hi! This is a voice preview with international appeal and confidence.",
        "hrithik_roshan": "Hello there! This is a smooth and sophisticated voice sample.",
        "akshay_kumar": "Hey! This is an energetic voice sample ready for action and comedy.",
        "prabhas": "Hello! This is the powerful voice of Tollywood cinema.",
        "mahesh_babu": "Hi! This is a stylish and sophisticated voice from Telugu cinema.",
        "jr_ntr": "Hello everyone! This is a dynamic and versatile voice sample.",
        "ram_charan": "Hey there! This is a charismatic voice with modern appeal.",
        "samantha": "Hello! This is a sweet yet strong voice from South Indian cinema.",
        "rashmika_mandanna": "Hi everyone! This is a youthful and energetic voice sample.",
        "rajinikanth": "Hello! This is the iconic voice of the Superstar of Indian cinema.",
        "vijay": "Hey! This is the energetic voice of Thalapathy from Tamil cinema.",
        "kamal_haasan": "Greetings! This is the intellectual and versatile voice of Ulaganayagan.",
        "suriya": "Hello! This is an intense and passionate voice from Tamil cinema.",
        "dhanush": "Hi there! This is a unique and expressive voice sample.",
        "nayanthara": "Hello! This is the confident voice of the Lady Superstar.",
        "yash": "Hey! This is the rugged and intense voice of the Rocking Star.",
        "dulquer_salmaan": "Hello! This is a charming and versatile voice from Malayalam cinema.",
        "allu_arjun": "Hey everyone! This is the stylish voice that became famous with Pushpa.",
        "fahadh_faasil": "Hello! This is an intense and nuanced voice from Malayalam cinema."
    }
    
    created_count = 0
    
    for celebrity in celebrities:
        celebrity_id = celebrity["id"]
        celebrity_name = celebrity["name"]
        
        # Get sample text
        sample_text = sample_texts.get(celebrity_id, f"Hello! This is a voice sample from {celebrity_name}.")
        
        # Create output path
        output_file = samples_dir / f"{celebrity_id}_sample.wav"
        
        # Skip if file already exists
        if output_file.exists():
            print(f"Sample already exists for {celebrity_name}")
            created_count += 1
            continue
        
        # Create the sample
        if create_sample_audio(celebrity_id, celebrity_name, sample_text, str(output_file)):
            created_count += 1
    
    print(f"\nCompleted! Created {created_count} sample files out of {len(celebrities)} celebrities.")
    
    if not TTS_AVAILABLE:
        print("\nTo create actual audio samples, install pyttsx3:")
        print("pip install pyttsx3")
        print("\nThen run this script again.")

if __name__ == "__main__":
    create_all_samples()