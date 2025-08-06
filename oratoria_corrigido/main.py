import streamlit as st
import os
import openai
import json
from utils import video_utils, whisper_transcribe, audio_analysis, visual_analysis, gpt_analysis, report_generator
from config import GPT_MODEL, OPENAI_API_KEY

# Configura a chave da OpenAI (caso não esteja no ambiente)
openai.api_key = OPENAI_API_KEY

# Título do app
st.title("Análise de Comunicação e Oratória com IA")

# Upload do vídeo
video_file = st.file_uploader("Envie seu vídeo", type=["mp4"])

# Garante que pastas necessárias existem
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

if video_file:
    # Salva o vídeo enviado
    video_path = f"uploads/{video_file.name}"
    with open(video_path, "wb") as f:
        f.write(video_file.read())

    # Caminho do áudio
    audio_path = "outputs/audio.wav"

    st.info("🔍 Processando vídeo...")

    # Etapas de análise
    video_utils.extract_audio(video_path, audio_path)
    transcription = whisper_transcribe.transcribe(audio_path)
    visual_data = visual_analysis.analyze_video_with_emotions(video_path)
    audio_data = audio_analysis.analyze_audio(audio_path)
    feedback = gpt_analysis.gpt_feedback(transcription, visual_data, audio_data)

    # Prompt para pontuações
    prompt = f"""
Com base no seguinte feedback, extraia uma pontuação de 0 a 10 para cada um dos quesitos abaixo, no formato JSON:

Quesitos:
- Vocabulário
- Voz
- Organização de ideias
- Gestos
- Expressões faciais
- Contato visual
- Estrutura
- Persuasão
- Criatividade

Feedback:
{feedback}
"""

    response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        content = response.choices[0].message.content
        analysis = json.loads(content)
    except Exception as e:
        st.error(f"Erro ao interpretar o JSON de análise: {e}")
        analysis = {}

    # Gerar relatório final
    report_path = f"outputs/{video_file.name}_relatorio.pdf"
    report_generator.generate_report(
        transcription, feedback, report_path,
        visual_data["graph_path"], analysis
    )

    st.success("✅ Análise finalizada!")
    st.image(visual_data["graph_path"], caption="Gráfico de Emoções Detectadas")
    st.download_button("📄 Baixar Relatório", data=open(report_path, "rb").read(), file_name="relatorio.pdf")
