from langchain_community.document_loaders import (WebBaseLoader,
                                                  YoutubeLoader,
                                                  CSVLoader,
                                                  PyPDFLoader,
                                                  TextLoader)


def carrega_site(url):
    loader = WebBaseLoader(url)
    lista_docs = loader.load()
    docs = '\n\n'.join([doc.page_content for doc in lista_docs])
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