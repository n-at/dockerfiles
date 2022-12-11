FROM node:latest as builder
RUN cd /opt &&\
    git clone https://github.com/n-at/doublebyte-local app &&\
    cd app &&\
    rm -rf .git &&\
    npm install

###############################################################################

FROM nginx:latest
COPY --from=builder /opt/app /usr/share/nginx/html
