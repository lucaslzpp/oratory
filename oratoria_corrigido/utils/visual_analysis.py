import cv2
from deepface import DeepFace
from collections import Counter
import os
import matplotlib.pyplot as plt

def analyze_video_with_emotions(video_path, frame_interval=60, resize_dim=(320, 240)):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    emotions_detected = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            resized = cv2.resize(frame, resize_dim)

            try:
                result = DeepFace.analyze(
                    img_path = resized,
                    actions = ['emotion'],
                    enforce_detection = False,
                    prog_bar = False
                )
                emotions_detected.append(result[0]['dominant_emotion'])
            except:
                emotions_detected.append("indefinido")

        frame_count += 1

    cap.release()

    emotion_summary = Counter(emotions_detected)

    # Geração de gráfico
    output_graph = "outputs/emotions_chart.png"
    labels = list(emotion_summary.keys())
    counts = list(emotion_summary.values())

    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição de Emoções no Vídeo")
    plt.axis('equal')
    plt.savefig(output_graph)
    plt.close()

    return {
        "emotions_detected": emotions_detected,
        "emotion_summary": emotion_summary,
        "graph_path": output_graph
    }
