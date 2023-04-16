from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text