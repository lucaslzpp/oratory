from openai import OpenAI
from config import OPENAI_API_KEY, GPT_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def gpt_feedback(transcription, visual_data, audio_data):
    prompt = f"""
Você é um avaliador especialista em oratória. Abaixo estão os dados capturados de um vídeo de apresentação. Seu papel é analisar o desempenho da pessoa com base nos seguintes quesitos:

1. Vocabulário – variedade e precisão na escolha das palavras.
2. Voz – projeção, modulação, ritmo e clareza.
3. Organização de ideias – lógica e fluidez entre os blocos do discurso.
4. Gestos – presença e alinhamento com a fala (com base nas emoções e expressividade).
5. Expressões faciais – coerência emocional e variação (dados de emoções predominantes).
6. Contato visual – estimado com base na detecção contínua de rosto nos frames.
7. Estrutura – início, desenvolvimento e conclusão bem definidos.
8. Persuasão – uso de argumentos, chamadas para ação, impacto emocional.
9. Criatividade – originalidade da fala, uso de analogias ou storytelling.

TRANSCRIÇÃO:
{transcription}

DADOS EMOCIONAIS (detectados a cada 2 segundos):
- Emoções predominantes: {visual_data['emotion_summary']}

DADOS VOCAIS:
- Volume médio: {audio_data['loudness_db']}
- Ritmo da fala: {audio_data['speech_rate']}

Com base nesses dados, faça uma avaliação detalhada, tópico por tópico, e atribua uma nota geral de 0 a 10 no final.
"""

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
