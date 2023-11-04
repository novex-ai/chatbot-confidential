FROM ollama/ollama:0.1.7

RUN apt-get update \
    && apt-get install -y netcat \
    && apt-get clean

ARG OLLAMA_MODEL=mistral-openorca

COPY run_ollama_pull.sh run_ollama_pull.sh

RUN bash ./run_ollama_pull.sh ${OLLAMA_MODEL}

ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]
