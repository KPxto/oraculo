import os
import streamlit as st
from time import sleep
from langchain_community.document_loaders import (WebBaseLoader,
                                                  YoutubeLoader,
                                                  CSVLoader,
                                                  PyPDFLoader,
                                                  TextLoader)
# resolvendo o problema do bloqueio de alguns sites
# q são bloqueados por segurança. Esta lib nos ajuda com a solução
#from fake_useragent import UserAgent


def carrega_site(url):
    docs = ''
    # fazendo 5 tentativas para acessar o site
    for i in range(5):
        try:
            # criando o user agent fake
            #os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url, raise_for_status=True)
            lista_docs = loader.load()
            docs = '\n\n'.join([doc.page_content for doc in lista_docs])
            break
        except:
            print(f'Erro ao carregar site, tentativa: {i + 1}')
            # esperando 2 segundos a cada tentativa
            sleep(2)
    if docs == '':
        st.error('Não foi possível carregar o site')
        st.stop()

    return docs


def carrega_yt(video_id):
    loader = YoutubeLoader(video_id, add_video_info=False, language=['pt'])
    lista_docs = loader.load()
    docs = '\n\n'.join([doc.page_content for doc in lista_docs])
    return docs


def carrega_csv(caminho):
    loader = CSVLoader(caminho)
    lista_docs = loader.load()
    docs = '\n\n'.join([doc.page_content for doc in lista_docs])
    return docs


def carrega_pdf(caminho):
    loader = PyPDFLoader(caminho)
    lista_docs = loader.load()
    docs = '\n\n'.join([doc.page_content for doc in lista_docs])
    return docs


def carrega_txt(caminho):
    loader = TextLoader(caminho)
    lista_docs = loader.load()
    docs = '\n\n'.join([doc.page_content for doc in lista_docs])
    return docs