from pydub import AudioSegment
import numpy as np
from utils import whisper_transcribe

def analyze_audio(audio_path):
    audio = AudioSegment.from_file(audio_path)

    # Duração em segundos
    duration = len(audio) / 1000
    duration_minutes = duration / 60

    # Volume médio (em dBFS)
    loudness = audio.dBFS

    # Pausas longas (> 800 ms de silêncio abaixo de -40 dBFS)
    silence_threshold = -40
    min_silence_len = 800  # ms
    silence_count = 0

    silence_ms = 0
    for chunk in audio[::100]:  # Verifica a cada 100ms
        if chunk.dBFS < silence_threshold:
            silence_ms += 100
            if silence_ms >= min_silence_len:
                silence_count += 1
                silence_ms = 0
        else:
            silence_ms = 0

    # Transcrição simplificada para contagem de palavras
    transcript = whisper_transcribe.transcribe(audio_path)
    word_count = len(transcript.split()) if transcript else 0
    speech_rate = word_count / duration_minutes if duration_minutes > 0 else 0

    return {
        "duration_seconds": duration,
        "loudness_db": loudness,
        "volume_avg": loudness,  # compatível com o prompt GPT
        "long_pauses": silence_count,
        "speech_rate": round(speech_rate, 2)
    }
