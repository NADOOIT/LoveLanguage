# File: transcription/views.py

from django.shortcuts import render
from .models import Transcription
from .services import transcribe_audio


def handle_audio_file(request):
    if request.method == "POST":
        audio_file = request.FILES["audio_file"]  # Get the uploaded audio file
        transcription_text = transcribe_audio(
            audio_file.temporary_file_path()
        )  # Transcribe the audio file

        # Create and save the Transcription object
        Transcription.objects.create(
            audio_file=audio_file,
            transcription_text=transcription_text,
        )
