import streamlit as st


MENSAGENS_EXEMPLO = [
    ('user', 'Olá'),
    ('assistant', 'Olá, tudo bem?'),
    ('user', 'Tudo em paz'),
    ('assistant', 'então blz')
]

TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'YouTube', 'Pdf', 'Csv', 'Txt'
]

CONFIG_MODELOS = {'Groq':
                {'modelos': ['gemma2-9b-it', 'llama-3.3-70b-versatile']},
                'OpenAI':
                {'modelos': ['o4-mini', 'o3', 'o1-mini']}}


def pagina_chat():
    st.header("🥷 Bem-vindo ao Oráculo!", divider=True)

    mensagens = st.session_state.get("mensagens", MENSAGENS_EXEMPLO)
    for msg in mensagens:
        chat = st.chat_message(msg[0])
        chat.markdown(msg[1])

    input_usuario = st.chat_input("Fale com o Oráculo...")
    if input_usuario:
        mensagens.append(('user', input_usuario))
        st.session_state['mensagens'] = mensagens
        st.rerun()


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


def main():
    pagina_chat()
    with st.sidebar:
        sidebar()


if __name__ == "__main__":
    main()