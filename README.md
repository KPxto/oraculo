# 🧙‍♂️ Oráculo - Chat com Documentos

O **Oráculo** é uma aplicação construída com [LangChain](https://www.langchain.com/) e [Streamlit](https://streamlit.io/), que permite que você interaja via chat com conteúdos de **documentos personalizados**. Você pode carregar arquivos como PDFs, textos, CSVs, vídeos do YouTube ou até mesmo sites, e conversar com a IA usando modelos da OpenAI ou da Groq.

---

## 🚀 Funcionalidades

- 💬 Chat com o conteúdo de documentos
- 📄 Suporte a múltiplos formatos: PDF, CSV, TXT, sites e vídeos do YouTube
- 🧠 Suporte a diferentes modelos de linguagem (OpenAI e Groq)
- 🧾 Memória de conversa preservada na sessão
- 🖥️ Interface amigável com Streamlit

---

## 🧠 Modelos Suportados

### 🔹 OpenAI
- `gpt-4o-mini`
- `o3`
- `o1-mini`

### 🔹 Groq
- `gemma2-9b-it`
- `llama-3.3-70b-versatile`

---

## 🛠️ Pré-requisitos

- Python 3.8 ou superior
- Chaves de API válidas da OpenAI e/ou Groq

## 📦 Instalação

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/oraculo-chat.git
cd oraculo-chat
```

2. Crie e ative um ambiente virtual
Linux/Mac
python -m venv venv
source venv/bin/activate

Windows
python -m venv venv
.\venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

---

## 💡 Como Usar

1. Execute o aplicativo com o comando:

```bash
streamlit run main.py
```

2. No navegador que será aberto automaticamente:

- Vá até a barra lateral

- Escolha o tipo de arquivo: PDF, CSV, TXT, Site ou YouTube

- Faça o upload do arquivo ou cole a URL, dependendo do tipo selecionado

- Selecione o provedor de modelo (OpenAI ou Groq)

- Escolha um dos modelos disponíveis

- Insira sua API Key para o provedor escolhido

- Clique em Inicializar Oráculo

- Comece a conversar com o conteúdo no campo de chat!

>> Use o botão "Apagar Histórico de Conversa" se quiser reiniciar o chat.

---

## 📝 Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).
