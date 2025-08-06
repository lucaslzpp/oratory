import streamlit as st

# Pega as configurações do secrets.toml
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
GPT_MODEL = st.secrets.get("GPT_MODEL", "gpt-4")