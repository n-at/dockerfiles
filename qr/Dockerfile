FROM alpine:latest as builder
RUN apk add git
RUN cd /opt && git clone -b gh-pages https://github.com/n-at/qr
RUN cd /opt/qr && rm -rf .git

###############################################################################

FROM nginx:latest
COPY --from=builder /opt/qr /usr/share/nginx/html
