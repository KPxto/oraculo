import streamlit as st
from langchain.memory import ConversationBufferMemory

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import tempfile

from loaders import (carrega_csv, carrega_pdf,
                     carrega_site, carrega_txt, carrega_yt)

# ================ App ================

MEMORIA = ConversationBufferMemory()
MEMORIA.chat_memory.add_user_message('Olá IA, blz?')
MEMORIA.chat_memory.add_ai_message('Oi, Humano. Tudo bem e vc?')


TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'YouTube', 'Pdf', 'Csv', 'Txt'
]

CONFIG_MODELOS = {'Groq':
                {'modelos': ['gemma2-9b-it', 'llama-3.3-70b-versatile'],
                 'chat': ChatGroq},
                'OpenAI':
                {'modelos': ['gpt-4o-mini', 'o3', 'o1-mini'],
                 'chat': ChatOpenAI}}


# ================ Funções ================

def carrega_arquivo(tipo_arquivo, arquivo):
    if tipo_arquivo.lower() == 'site':
        doc = carrega_site(arquivo)
    if tipo_arquivo.lower() == 'youtube':
        doc = carrega_yt(arquivo)
    if tipo_arquivo.lower() == 'pdf':
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
            temp.write(arquivo.read())
            caminho_temp = temp.name
        doc = carrega_pdf(caminho_temp)
    if tipo_arquivo.lower() == 'csv':
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp:
            temp.write(arquivo.read())
            caminho_temp = temp.name
        doc = carrega_csv(caminho_temp)
    if tipo_arquivo.lower() == 'txt':
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp:
            temp.write(arquivo.read())
            caminho_temp = temp.name
        doc = carrega_txt(caminho_temp)

    return doc


def carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo):
    doc = carrega_arquivo(tipo_arquivo, arquivo)
    chat = CONFIG_MODELOS[provedor]['chat'](model=modelo, api_key=api_key)
    st.session_state['chat'] = chat


def pagina_chat():
    st.header("🥷 Bem-vindo ao Oráculo!", divider=True)

    chat_model = st.session_state.get('chat')
    memoria = st.session_state.get("memoria", MEMORIA)
    for msg in memoria.buffer_as_messages:
        chat = st.chat_message(msg.type)
        chat.markdown(msg.content)

    input_usuario = st.chat_input("Fale com o Oráculo...")
    if input_usuario:
        chat = st.chat_message('human')
        chat.markdown(input_usuario)

        chat = st.chat_message('ai')
        resposta = chat.write_stream(chat_model.stream(input_usuario))

        memoria.chat_memory.add_user_message(input_usuario)
        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria


def sidebar():
    tabs = st.tabs(['Upload de Arquivos', 'Seleção de Modelos'])
    with tabs[0]:
        tipo_arquivo = st.selectbox('Selecione o tipo de arquivo',
                                     TIPOS_ARQUIVOS_VALIDOS)
        if tipo_arquivo.lower() == 'site':
            arquivo = st.text_input(
                'Digite a URL do site')
        if tipo_arquivo.lower() == 'youtube':
            arquivo = st.text_input(
                'Digite a URL do vídeo')
        if tipo_arquivo.lower() == 'pdf':
            arquivo = st.file_uploader(
                'Faça o upload do arquivo pdf', type='.pdf')
        if tipo_arquivo.lower() == 'csv':
            arquivo = st.file_uploader(
                'Faça o upload do arquivo csv', type='.csv')
        if tipo_arquivo.lower() == 'txt':
            arquivo = st.file_uploader(
                'Faça o upload do arquivo txt', type='.txt')

    with tabs[1]:
        provedor = st.selectbox('Selecione o provedor do modelo',
                                CONFIG_MODELOS.keys())

        modelo = st.selectbox(
            'Selecione o modelo', CONFIG_MODELOS[provedor]['modelos'])

        api_key = st.text_input(
            f'Adicione a Api Key para o provedor {provedor}',
            value=st.session_state.get(f'api_key{provedor}'))

        st.session_state[f'api_key{provedor}'] = api_key

    if st.button('Inicializar Oráculo', use_container_width=True):
        carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo)


def main():
    pagina_chat()
    with st.sidebar:
        sidebar()


if __name__ == "__main__":
    main()