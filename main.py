import streamlit as st


MENSAGENS_EXEMPLO = [
    ('user', 'Olá'),
    ('assistant', 'Olá, tudo bem?'),
    ('user', 'Tudo em paz'),
    ('assistant', 'então blz')
]


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


def main():
    pagina_chat()


if __name__ == "__main__":
    main()