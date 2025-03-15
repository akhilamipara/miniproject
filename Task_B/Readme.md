# 🎙️ AI Speech Processing App

##  Overview
This AI-powered Speech Processing App allows users to:
1. **Convert Text to Speech (TTS)** - Enter text, select a language, and generate AI-powered speech.
2. **Convert Speech to Text (STT)** - Upload an audio file, and the app will transcribe the speech into text.

This application uses `Gradio` for the UI, `gTTS` for text-to-speech, `SpeechRecognition` for speech-to-text, and `pydub` for audio format conversion.

---

##  Features
- **Text-to-Speech (TTS)**: Supports multiple languages for speech synthesis.  
- **Speech-to-Text (STT)**: Converts audio recordings into text.  
- **Supports Multiple Audio Formats**: Automatically converts MP3, WAV, and other formats to WAV for speech recognition.  
- **Downloadable Speech Files**: Save generated speech output as an MP3 file.  
- **Adjustable Speech Speed**: Control the playback speed of generated speech.  
- **Male/Female Voice Selection**: Future support for different voice types.  
- **AI-generated Realistic Voices**: Planned feature for enhanced speech synthesis.  
**User-Friendly UI**: Built with `Gradio` for an interactive web-based experience.  

---

##  Tech Stack
- **Python** - Core programming language.
- **Gradio** - For building an interactive UI.
- **gTTS** - Google Text-to-Speech API.
- **SpeechRecognition** - Converts speech to text using Google Speech API.
- **pydub** - Handles audio conversion.

---

##  Installation

```sh
pip install gradio gtts ffmpeg
```
##  Usage
Run the application using the command:
```sh
python task_b.py
```

The Gradio interface will open in your browser, allowing you to interact with the app.

---

##  Supported Languages for TTS
- English (`en`)
- French (`fr`)
- Spanish (`es`)
- German (`de`)
- Hindi (`hi`)
- Chinese (`zh`)
- Japanese (`ja`)
- Italian (`it`)
- Russian (`ru`)

---

##  UI Preview
The app provides two tabs:
-  Text-to-Speech (TTS)**: Enter text, select language, and generate speech.
-  Speech-to-Text (STT)**: Upload an audio file and convert it to text.