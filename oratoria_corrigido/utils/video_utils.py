import cv2

from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    """
    Extrai o áudio de um vídeo e salva como .wav
    """
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        video.close()
    except Exception as e:
        print(f"Erro ao extrair áudio: {e}")
        raise

def extract_frames(video_path, interval_seconds=2):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval_frames = fps * interval_seconds

    frames = []
    frame_index = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_index % interval_frames == 0:
            frames.append(frame)
        frame_index += 1

    cap.release()
    return frames
