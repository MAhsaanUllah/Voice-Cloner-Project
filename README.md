---
title: Voice Cloner App
emoji: 🗣️
colorFrom: pink
colorTo: purple
sdk: streamlit
sdk_version: "1.30.0"
app_file: app.py
pinned: false
---


# 🎙️ Custom AI Voice Cloner & Text-to-Speech Generator

This is my internship project to build an AI-based voice cloning and TTS (Text-to-Speech) application using pretrained models.

---

## ✅ Features

- Uses Coqui TTS `tts_models/en/vctk/vits` pretrained model
- Choose from multiple synthetic speakers
- Input any custom text
- Generate voice output in the selected speaker’s voice
- Download the audio file
- View audio spectrogram
- All generations are logged with timestamp and speaker

---

## 🚀 How to Run

### 1. Clone the Repository


git clone https://github.com/MAhsaanUllah/Voice-Cloner-Project.git
cd Voice-Cloner-Project
2. Create Virtual Environment (Recommended)



# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies

pip install -r requirements.txt
4. Run the Streamlit App

streamlit run app.py


📂 Project Structure

Voice-Cloner-Project/
├── app.py              # Streamlit web app
├── requirements.txt    # Required Python libraries
├── README.md           # Project overview and instructions
├── logs/               # Log file of all generations (auto-created)
└── output/             # Generated audio files (auto-created)


📚 Notes
Uses a pretrained multi-speaker Coqui TTS model (vits) for speech synthesis

Allows speaker selection and real-time TTS generation

Ideal for learning inference pipelines without GPU-based training

🔧 Future Upgrades
Fine-tune on custom recorded voice datasets

Add ability to upload your own dataset

Deploy on Hugging Face Spaces or Streamlit Cloud

🧠 Technologies Used
Python

Coqui TTS

Streamlit

Librosa

Matplotlib

📸 Screenshot

![App Screenshot](samples/demo.png)
🙋 Author
Made with ❤️ by Ahsaan Ullah
GitHub

 