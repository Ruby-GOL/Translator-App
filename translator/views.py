import os
# from .googletrans_patch import translator
from django.shortcuts import render
from .translation import translate, detect_language
from .speech_to_text import speech_to_text
from django.core.files.storage import default_storage
from .forms import TranslationForm


# Create your views here.

def landing_page(request):
    return render(request=request,template_name='landing page/landing.html')
def homepage(request):
    return render(request=request,template_name='homepage/home.html')

def about(request):
    return render(request=request,template_name='aboutpage/about.html')

def services(request):
    return render(request=request,template_name='servicespage/services.html')

def index(request):
    if request.method == "POST":
        # Get user input
        input_text = request.POST.get("input_text", "")
        target_language = request.POST.get("target_language", "en")
        audio_file = request.FILES.get("audio_file", None)

        if audio_file:
            # Save the uploaded file temporarily
            file_name = default_storage.save(audio_file.name, audio_file)
            file_path = default_storage.path(file_name)

            # Convert speech to text
            input_text = speech_to_text(file_path)

            # Remove the temporary file
            default_storage.delete(file_path)

        # Detect the input language
        src_lang = detect_language(input_text)

        # Translate the text
        translation = translate(input_text, src_lang, target_language)

        context = {"input_text": input_text, "translation": translation, "target_language": target_language}
    else:
        context = {}
    form = TranslationForm()
    context['form'] = form

    return render(request, "translate.html", context)


