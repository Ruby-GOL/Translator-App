from django.db import models

# Create your models here.
class Translation(models.Model):
    input_text = models.TextField()
    translated_text = models.TextField()
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    audio_file = models.FileField(upload_to='translations/')