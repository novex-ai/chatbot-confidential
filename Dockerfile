FROM ubuntu:jammy-20231004

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update \
  && apt upgrade -y \
  && apt install -y build-essential checkinstall locales wget \
  && apt clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# https://devguide.python.org/getting-started/setup-building/#install-dependencies
RUN apt update \
  && apt install -y \
    gdb lcov pkg-config \
    libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
    libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev \
    lzma lzma-dev tk-dev uuid-dev zlib1g-dev \
  && apt clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tgz \
  && tar -xzf Python-3.11.6.tgz \
  && cd Python-3.11.6 \
  && ./configure --enable-optimizations \
  && make -j $(nproc) \
  && make altinstall \
  && cd .. \
  && rm -rf Python-3.11.6 Python-3.11.6.tgz

RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1 \
  && update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.11 1 \
  && pip3.11 install --upgrade pip \
  && update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.11 1 \
  && update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.11 1

WORKDIR /sanic

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ["run_entrypoint.sh", "run_cache_model.py", "run_server.py", "./"]
COPY frontend_quasar_vue/dist frontend_quasar_vue/dist/
COPY backend_sanic/ backend_sanic/

ENV APP_MODEL_CACHE_PATH = /sanic/model_cache

RUN python run_cache_model.py

EXPOSE 8000

CMD ["bash", "run_entrypoint.sh"]
