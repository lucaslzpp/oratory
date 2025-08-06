from fpdf import FPDF
from PIL import Image
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
import os

def generate_report(transcription, feedback, output_path, chart_path, analysis=None):
    # Salvar imagem do gráfico sunburst se dados estiverem disponíveis
    sunburst_path = "outputs/sunburst_chart.png"
    if analysis:
        labels = []
        parents = []
        values = []
        for key, value in analysis.items():
            labels.append(key)
            parents.append("")
            values.append(value)

        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
        ))
        pio.write_image(fig, sunburst_path, format='png', width=600, height=600, scale=2)

    # Criar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Relatório de Análise de Comunicação e Oratória", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "🗣️ Feedback detalhado:")
    pdf.ln(2)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, feedback)

    if os.path.exists(chart_path):
        pdf.ln(8)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "🎭 Gráfico de Emoções Detectadas:", ln=True)
        pdf.image(chart_path, w=150)

    if os.path.exists(sunburst_path):
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "📊 Avaliação por Quesito:", ln=True)
        pdf.image(sunburst_path, w=150)

    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "💡 Dica personalizada:")
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, "Continue praticando com foco nos quesitos com menor desempenho. Foque em pausas estratégicas, reforço de expressividade e criação de analogias marcantes. Lembre-se: a evolução é fruto da repetição consciente.")

    pdf.output(output_path)
