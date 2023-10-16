# chatbot-confidential
fully-contained (no external API calls) knowledgebase chatbot

- deployable on AWS
- leverages AWS Bedrock for LLM
- includes data upload and processing of documents to use as knowledgebase

_Naming: elephants are often described as having excellent memory.  This is like putting those pachyderms into a pen where you can keep an eye on that knowledge_

## Dev Setup

Instructions on developer setup for macOS

Pre-requisites:
- [pyenv](https://github.com/pyenv/pyenv)
- [Python Poetry](https://python-poetry.org/)
- [nvm](https://github.com/nvm-sh/nvm)

### Python Dev Setup

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

### Web Dev Setup

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

in the `chatbot-confidential` folder:
```bash
poetry run sanic server:app --dev --tls=`echo ~/dev-tls/`
```

```bash
cd frontend_quasar_vue
npm run dev
```
