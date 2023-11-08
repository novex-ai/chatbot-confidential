# chatbot-confidential
Fully-contained private knowledgebase chatbot.  Ask questions about your own documents without data privacy issues.

# Installation and Usage

1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/) and install it on your local machine.
2. Download [ollama.ai](https://ollama.ai/download) and install it on your local machine
3. Download the chatbot-confidential [compose.yaml](https://raw.githubusercontent.com/novex-ai/chatbot-confidential/main/compose.yaml) (right click and Save As...)
4. Open your local command line terminal - [Mac Instructions](https://www.idownloadblog.com/2019/04/19/ways-open-terminal-mac/) | [Windows Instructions](https://www.digitalcitizen.life/open-windows-terminal/)
5. Navigate (cd _foldername_) to the folder where you downloaded `compose.yaml`.  Then type `docker compose up` in the command line terminal, and hit enter.  (To stop, close the terminal window, or use Ctl-C)
6. Open http://localhost:8000/ in a browser on your machine

# Features:
- runs entirely on LOCAL desktop machine: NO data in the cloud, NO API calls to the cloud
- includes data upload and processing of documents - supported file types: `.pdf` `.docx` `.txt`
- uses Retrieval Augmentation (RAG) to find documents relevant to your chat question, and use that in answering
- uses [Hypothetical Document Embeddings (HyDE)](https://arxiv.org/abs/2212.10496) for improved document relevance
- also uses NEW question-generation approach for further improved document relevance (see future blog post) 

Implementation:
- local LLM model: [OpenOrca - Mistral - 7B](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca) run using [ollama.ai](https://ollama.ai/)
- local embedding model: [gte-large](https://huggingface.co/thenlper/gte-large) run using [ONNX Runtime](https://onnxruntime.ai/)
- uses [pgvector](https://github.com/pgvector/pgvector) for local vector database - using cosine similarity and HNSW
- uses [Docker Compose](https://docs.docker.com/compose/features-uses/)
- Data is stored locally using [Docker Desktop Volumes](https://docs.docker.com/desktop/use-desktop/volumes/)

# Developer Setup

Instructions on developer setup for macOS

Pre-requisites:
- [pyenv](https://github.com/pyenv/pyenv)
- [Python Poetry](https://python-poetry.org/)
- [nvm](https://github.com/nvm-sh/nvm)

### Python Developer Setup

```bash
pyenv install 3.11
pyenv local 3.11
```

```bash
poetry install
```

Install and initialize [mkcert](https://github.com/FiloSottile/mkcert)
This enables local https via [sanic](https://sanic.dev/en/guide/deployment/development.html#automatic-tls-certificate)

```bash
brew install mkcert
brew install nss

mkdir ~/dev-tls
cd ~/dev-tls
mkcert -install
mkcert example.com "*.example.com" example.test localhost 127.0.0.1 ::1

cp example.com+5-key.pem privkey.pem
cp example.com+5.pem fullchain.pem
chmod 0600 *.pem
```

### Web Developer Setup

```bash
nvm install v18
nvm use v18
```

```bash
cd frontend_quasar_vue
npm install
npm run build
```

### Develop

create a local .env file in the `chatbot-confidential` folder:
```
APP_DATA_PATH=/tmp/chatbot-data
APP_OLLAMA_HOST=0.0.0.0:11434
APP_POSTGRES_HOST=0.0.0.0:5432
APP_POSTGRES_USER=postgres
APP_POSTGRES_PASSWORD=notsoseekret
APP_POSTGRES_DB=postgres
```
and create the data path locally on your own machine 

in the `chatbot-confidential` folder:
```bash
poetry run sanic server:app --dev --tls=`echo ~/dev-tls/`
```

in a new terminal window:
```bash
docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=notsoseekret \
  -p 5432:5432 \
  -v postgres:/var/lib/postgresql/data \
  ankane/pgvector:v0.5.1
```

in a new terminal window, in the `chatbot-confidential` folder:
```bash
cd frontend_quasar_vue
npm run dev
```
