from django.db import models
from accounts.models import User

class Room(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    file = models.FileField(upload_to='chat_files/', blank=True, null=True)
    voice_recording = models.FileField(upload_to='voice_recordings/', blank=True, null=True)

