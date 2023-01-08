FROM ubuntu:22.04 as builder
RUN apt-get update &&\
    apt-get install -y wget git git-lfs nodejs npm &&\
    cd /opt &&\
    git clone https://github.com/n-at/local-translator app &&\
    cd app &&\
    npm install &&\
    ./models-bergamot.sh &&\
    ./models-vosk.sh

###############################################################################

FROM nginx:latest
COPY --from=builder /opt/app /usr/share/nginx/html
