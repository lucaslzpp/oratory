import streamlit as st

# Pega as configurações do secrets.toml
OPENAI_API_KEY = st.secrets["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"]
GPT_MODEL = st.secrets.get("GPT_MODEL", "gpt-4")
