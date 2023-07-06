FROM ubuntu:22.04 as builder
RUN apt-get update &&\
    apt-get install -y wget git nodejs npm &&\
    cd /opt &&\
    git clone https://github.com/n-at/local-ocr app &&\
    cd app &&\
    npm install &&\
    mkdir models &&\
    ./download_models.sh

###############################################################################

FROM nginx:latest
COPY --from=builder /opt/app /usr/share/nginx/html
