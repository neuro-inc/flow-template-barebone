FROM ghcr.io/neuro-inc/base:v24.12.0-runtime

COPY apt.txt .
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -qq update && \
    cat apt.txt | tr -d "\r" | xargs -I % apt-get -qq install --no-install-recommends % && \
    apt-get -qq clean && \
    apt-get autoremove -y --purge && \
    rm -rf apt.txt /var/lib/apt/lists/* /tmp/* ~/*

COPY requirements.txt .
RUN pip install --progress-bar=off -U --no-cache-dir -r requirements.txt
