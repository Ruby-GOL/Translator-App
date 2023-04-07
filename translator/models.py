from django.db import models

# Create your models here.
from django.db import models
from audio_recorder.models import AudioRecord


class Recording(models.Model):
    audio_file = models.ForeignKey(AudioRecord, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
