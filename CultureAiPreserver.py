# 🌍 AI-Generated World Cultures Preservation System - Humanized Prototype

"""
This user-friendly app helps preserve cultural heritage by:
1. Uploading a voice recording of a traditional story or ritual
2. Transcribing (fake text for now) and summarizing it
3. Displaying a matching cultural image (placeholder logic)

Built with love to celebrate human history using technology ❤️
"""

# --- Required Imports ---
import os
from PIL import Image
import streamlit as st

# Folder that holds cultural images
IMAGE_DIR = "cultural_images/"

# --- 1. Transcribe the audio file (placeholder) ---
def transcribe_audio(file_path):
    # In a real app, we'd use Whisper to convert speech to text
    # For now, we'll simulate it
    return "Long ago in our village, we used to gather under the moonlight to celebrate with music and stories."

# --- 2. Summarize the transcription (placeholder) ---
def summarize_text(text):
    # Simulates summarizing a story to its core idea
    sentences = text.split('.')
    if len(sentences) > 2:
        return sentences[0].strip() + '.' + sentences[1].strip() + '.'
    return text.strip()

# --- 3. Find a matching image (simplified logic) ---
def find_best_image(prompt):
    # Pretend to choose an image based on the story
    image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not image_files:
        return None
    return image_files[0]  # Just show the first image for now

# --- 4. The Web App Interface ---
def run_ui():
    st.set_page_config(page_title="Culture Preserver", page_icon="🌍")
    st.title("🌍 AI Cultural Story Preserver")
    st.write("""
    Upload a voice recording of a cultural story or ritual (like a festival, tradition, or memory).
    We'll help you preserve it by writing it down and showing a related image.
    """)

    audio_file = st.file_uploader("🎤 Upload a voice recording (.mp3 or .wav)", type=["mp3", "wav"])

    if audio_file:
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_file.read())

        st.info("Transcribing your story... ✍️")
        transcript = transcribe_audio("temp_audio.mp3")
        st.success("Here's what we heard:")
        st.write(transcript)

        st.info("Summarizing the story... 📚")
        summary = summarize_text(transcript)
        st.success("Summary:")
        st.write(summary)

        st.info("Finding a related cultural image... 🖼️")
        best_img = find_best_image(summary)
        if best_img:
            st.image(os.path.join(IMAGE_DIR, best_img), caption="Cultural connection found!", use_column_width=True)
        else:
            st.warning("Hmm... We couldn't find any images in the 'cultural_images' folder.")

if __name__ == "__main__":
    run_ui()