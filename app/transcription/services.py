import whisper


def transcribe_audio(file_path):
    model = whisper.load_model("base")  # Load the base model
    result = model.transcribe(file_path)  # Transcribe the audio file
    return result["text"]  # Return the transcribed text
