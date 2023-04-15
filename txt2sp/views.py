from django.shortcuts import render
from django.http import JsonResponse
from .forms import TextForm
from .models import Text
from .utils import translator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def translate(request):
    form = TextForm()
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            sound_dir = translator(text)
            print(sound_dir)
    
    return render(request, 'txt2sp/index.html', {'Form': form, "dir": sound_dir})
