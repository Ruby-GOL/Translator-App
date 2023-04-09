from django.shortcuts import render
from .forms import TranslationForm
from .models import Translation
from .utils import translate_text, text_to_speech, speech_to_text

def index(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            source_language = form.cleaned_data['source_language']
            target_language = form.cleaned_data['target_language']
            output_format = form.cleaned_data['output_format']
            
            # Translate text
            translated_text = translate_text(input_text, source_language, target_language)
            
            if output_format == 'audio':
                # Generate audio
                audio_file = text_to_speech(translated_text, target_language)
                # Save the translation
                translation = Translation(input_text=input_text, translated_text=translated_text, source_language=source_language, target_language=target_language, audio_file=audio_file)
                translation.save()
            else:
                # Save the translation
                translation = Translation(input_text=input_text, translated_text=translated_text, source_language=source_language, target_language=target_language)
                translation.save()

            return render(request, 'translator/result.html', {'translation': translation})
    else:
        form = TranslationForm()

    return render(request, 'translator/index.html', {'form': form})
