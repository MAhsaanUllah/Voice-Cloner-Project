import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from datetime import datetime
import os
from TTS.api import TTS

st.title("🎙️ Voice Cloner App (Multi-Speaker Demo)")

# Load Multi-Speaker Model
MODEL_NAME = "tts_models/en/vctk/vits"
tts = TTS(model_name=MODEL_NAME, gpu=False)

# Speakers list (if supported)
speakers = tts.speakers

# Show dropdown if model supports multiple speakers
if speakers:
    selected_speaker = st.sidebar.selectbox("🎤 Select a Speaker", speakers)
else:
    selected_speaker = None
    st.sidebar.warning("This is a single-speaker model.")

# Text input box
user_text = st.text_area("📝 Enter text to synthesize:", "Hello, this is a multi-speaker voice cloning demo.")

if st.button("Generate Voice 🎧"):
    os.makedirs("output", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    # Generate speech
    if selected_speaker:
        tts.tts_to_file(text=user_text, speaker=selected_speaker, file_path="output/output.wav")
    else:
        tts.tts_to_file(text=user_text, file_path="output/output.wav")

    # Play audio
    audio_file = open("output/output.wav", "rb")
    st.audio(audio_file.read(), format="audio/wav")
    st.download_button("⬇️ Download Audio", data=audio_file, file_name="output.wav")

    # Show spectrogram
    y, sr = librosa.load("output/output.wav")
    fig, ax = plt.subplots()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    ax.set_title('📊 Spectrogram of Generated Audio')
    st.pyplot(fig)

    # Save logs
    with open("logs/project_log.txt", "a") as f:
        f.write(f"{datetime.now()} | Speaker: {selected_speaker} | Text: {user_text}\n")

    st.success("✅ Audio generated, spectrogram plotted, and log saved.")

# Log viewer
with st.expander("📜 View Logs"):
    if os.path.exists("logs/project_log.txt"):
        with open("logs/project_log.txt", "r") as f:
            logs = f.read()
        st.text_area("Log File", logs, height=200)
    else:
        st.info("No logs yet.")

