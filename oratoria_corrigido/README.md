🚀 ORATÓRIA IA - VERSÃO FINAL CORRIGIDA PARA MACOS (INTEL)

PASSOS PARA INSTALAR E EXECUTAR:

cd /Users/user/Documents/ORATORIA_IA/oratoria_ia_final

1. Certifique-se de usar Python 3.10.13 com pyenv:
   pyenv install 3.10.13
   pyenv local 3.10.13

2. Crie o ambiente virtual:
   python -m venv venv
   source venv/bin/activate

3. Instale os pacotes:
   pip install --upgrade pip
   pip install -r requirements.txt

4. Insira sua chave da OpenAI no arquivo: config.py

5. Execute o sistema:
   streamlit run main.py

👉 Esse pacote já vem com correções específicas para macOS (ml_dtypes, tensorflow, deepface).