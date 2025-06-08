import os
from openai import OpenAI
import soundfile as sf
import sounddevice as sd
import streamlit as st
from io import BytesIO
from google.generativeai import GenerativeModel, configure

# Configure o Gemini API com sua chave
configure(api_key=os.getenv("GEMINI_API_KEY"))

client = OpenAI(api_key=os.getenv("API_KEY"))
st.set_page_config(page_title="Agente Tradutor de Áudio com IA", page_icon=":globe_with_meridians:")

# Importando bibliotecas
if "gravado" not in st.session_state:
    st.session_state.gravado = False
if "buffer_do_audio" not in st.session_state:
    st.session_state.buffer_do_audio = False

st.title("Agente Tradutor de Áudio com IA")

# Configurando o layout
duração = st.slider("Duração do áudio (segundos)", 1, 60, 10)

#
if st.button("Gravar Áudio", key = "record"):
       with st.info("Gravando..."):
            # Iniciando a gravação
           gravação = sd.rec(int(duração * 44100), samplerate=44100, channels=1)
           sd.wait()
           # Salvando o áudio gravado
           # Convertendo o áudio gravado para BytesIO
           buffer = BytesIO()
           sf.write(buffer, gravação, 44100, format='WAV') # Use sf.write to write to BytesIO
           buffer.seek(0)
           st.session_state.buffer_do_audio = buffer
           st.session_state.gravado = True

           st.success("Áudio gravado com sucesso!")

           if st.session_state.gravado:
                st.audio(st.session_state.buffer_do_audio, format="wav")

# Traduzindo o áudio gravado
if st.button("Traduzir Áudio", key="tradutor") :
    if not st.session_state.gravado or not st.session_state.buffer_do_audio:
        st.error("Por favor, grave um áudio primeiro.")
    else:
        with st.spinner("Transcrevendo e Traduzindo..."):
            buffer_ia = st.session_state.buffer_do_audio
            buffer_ia.seek(0)  # Certificando-se de que o buffer está no início
            buffer_ia.name = "audio.wav" # Necessário para a API da OpenAI

            # Transcrição do áudio usando OpenAI Whisper
            try:
                trancricao = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=buffer_ia,
                    language="pt"  # Definindo o idioma de origem como português
                ).text
            except Exception as e:
                st.error(f"Erro ao transcrever o áudio com OpenAI Whisper: {e}")
                trancricao = "Erro na transcrição."

            # Tradução do texto transcrito usando Google Gemini
            try:
                gemini_model = GenerativeModel("gemini-2.0-flash")  # Use o modelo Gemini apropriado
                resposta_em_ingles_gemini = gemini_model.generate_content(
                    f"Traduza o seguinte texto para o inglês: \"{trancricao}\""
                ).text
            except Exception as e:
                st.error(f"Erro ao traduzir o texto com Google Gemini: {e}")
                resposta_em_ingles_gemini = "Erro na tradução."

        st.success("Áudio processado com sucesso!")

        st.subheader("Transcrição do Áudio:")
        st.write(trancricao)  # Exibindo a transcrição do áudio
        st.subheader("Tradução em Inglês (Gemini):")
        st.write(resposta_em_ingles_gemini)  # Exibindo a tradução do áudio