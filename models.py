from django.views.decorators.csrf import csrf_exempt
from django_audiofield.views import record
from django.db import models
from django_audiofield.models import AudioRecord


class Recording(models.Model):
    audio_file = models.ForeignKey(AudioRecord, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    from django.http import JsonResponse


@csrf_exempt
def record_audio(request):
    audio_file = record(request)
    recording = Recording.objects.create(audio_file=audio_file)
    return JsonResponse({'status': 'success', 'recording_id': recording.id})
