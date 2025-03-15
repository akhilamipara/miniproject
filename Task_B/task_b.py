import gradio as gr
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import os

LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh",
    "Japanese": "ja",
    "Italian": "it",
    "Russian": "ru"
}

def text_to_speech(text, language):
    if not text.strip():
        return "Error: Please enter some text.", None

    lang_code = LANGUAGES.get(language, "en")
    tts = gTTS(text=text, lang=lang_code, slow=False)
    output_file = "output.mp3"
    tts.save(output_file)

    return output_file, output_file
def speech_to_text(audio):
    recognizer = sr.Recognizer()
    wav_file = "converted_audio.wav"

    try:
        audio_segment = AudioSegment.from_file(audio)
        audio_segment.export(wav_file, format="wav")

        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if os.path.exists(wav_file):
            os.remove(wav_file)

with gr.Blocks() as app:
    gr.Markdown("# AI Speech Processing App")
    
    with gr.Tab("🗣️ Text-to-Speech (TTS)"):
        text_input = gr.Textbox(label="Enter Text")
        language_input = gr.Dropdown(choices=list(LANGUAGES.keys()), label="Select Language", value="English")
        tts_output = gr.Audio(label="Generated Speech")
        tts_download = gr.File(label="Download Speech")
        tts_btn = gr.Button("Generate Speech")

        tts_btn.click(text_to_speech, inputs=[text_input, language_input], outputs=[tts_output, tts_download])

    with gr.Tab("🎤 Speech-to-Text (STT)"):
        audio_input = gr.Audio(type="filepath", label="Upload Speech")  # FIXED: Support for MP3 & WAV
        text_output = gr.Textbox(label="Recognized Text")
        stt_btn = gr.Button("Convert to Text")

        stt_btn.click(speech_to_text, inputs=audio_input, outputs=text_output)

app.launch()
