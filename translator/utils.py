import io
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech
from google.cloud import translate_v2 as translate

def translate_text(text, source_lang, target_lang):
    translate_client = translate.Client()
    result = translate_client.translate(text, source_language=source_lang, target_language=target_lang)
    return result['translatedText']

def text_to_speech(text, language_code):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)
    return io.BytesIO(response.audio_content)

def speech_to_text(audio_file, language_code):
    client = speech.SpeechClient()
    with io.open(audio_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript
