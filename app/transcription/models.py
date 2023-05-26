from django.db import models

# Create your models here.


# File: transcription/models.py
class Transcription(models.Model):
    audio_file = models.FileField(upload_to="audio_files/")
    transcription_text = models.TextField()
    transcribed_at = models.DateTimeField(auto_now_add=True)
