import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    audio_segment = AudioSegment.from_file(audio_file)
    audio_data = audio_segment.export(format="wav")
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            text = ""
    return text
