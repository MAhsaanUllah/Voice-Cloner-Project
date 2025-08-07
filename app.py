import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from datetime import datetime
import os
from TTS.api import TTS

# 🎙️ App Header
st.set_page_config(page_title="Voice Cloner", page_icon="🎙️")
st.title("🎙️ Voice Cloner App (Single-Speaker Model)")
st.markdown("---")

# 📦 Load Stable Single-Speaker Model
MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(model_name=MODEL_NAME, gpu=False)

# ℹ️ Info Sidebar
st.sidebar.info("Using single-speaker model: tacotron2-DDC")

# 📝 Text Input
user_text = st.text_area("📝 Enter text to synthesize:", "Hello, this is a voice cloning demo.")

# 🎧 Voice Generation Button
if st.button("Generate Voice 🎧"):
    os.makedirs("output", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    audio_path = "output/output.wav"

    try:
        # Generate Speech to File
        tts.tts_to_file(text=user_text, file_path=audio_path)

        # 🔊 Play Audio
        with open(audio_path, "rb") as audio_file:
            audio_data = audio_file.read()
            st.audio(audio_data, format="audio/wav")
            st.download_button("⬇️ Download Audio", data=audio_data, file_name="output.wav")

        # 📊 Spectrogram Visualization
        y, sr = librosa.load(audio_path)
        fig, ax = plt.subplots()
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax)
        fig.colorbar(img, ax=ax, format="%+2.0f dB")
        ax.set_title('📊 Spectrogram of Generated Audio')
        st.pyplot(fig)

        # 🧾 Log Generation
        with open("logs/project_log.txt", "a") as log_file:
            log_file.write(f"{datetime.now()} | Text: {user_text}\n")

        st.success("✅ Audio generated, visualized, and logged.")

    except Exception as e:
        st.error(f"❌ Error generating audio: {e}")

# 📜 View Logs
with st.expander("📜 View Logs"):
    log_path = "logs/project_log.txt"
    if os.path.exists(log_path):
        with open(log_path, "r") as log_reader:
            logs = log_reader.read()
        st.text_area("Log File", logs, height=200)
    else:
        st.info("No logs found.")
