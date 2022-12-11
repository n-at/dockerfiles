FROM alpine:latest as builder
RUN apk add git
RUN cd /opt && git clone -b gh-pages https://github.com/n-at/webrtc-screenshot app
RUN cd /opt/app &&\
    git checkout gh-pages &&\
    rm -rf .git

###############################################################################

FROM nginx:latest
COPY --from=builder /opt/app /usr/share/nginx/html
