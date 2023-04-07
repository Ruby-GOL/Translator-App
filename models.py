from django.http import JsonResponse
from audio_recorder.views import record
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from audio_recorder.models import AudioRecord


class Recording(models.Model):
    audio_file = models.ForeignKey(AudioRecord, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


@csrf_exempt
def record_audio(request):
    audio_file = record(request)
    recording = Recording.objects.create(audio_file=audio_file)
    return JsonResponse({'status': 'success', 'recording_id': recording.id})
