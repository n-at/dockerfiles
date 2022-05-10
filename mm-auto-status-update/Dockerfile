FROM golang:1.18 as builder
RUN git clone "https://github.com/n-at/mm-auto-status-update" /build &&\
    cd /build &&\
    CGO_ENABLED=0 GOOS=linux go build -a -o app .

###############################################################################

FROM alpine:latest
ARG TIMEZONE="Europe/Moscow"
RUN apk add tzdata &&\
    cp "/usr/share/zoneinfo/${TIMEZONE}" "/etc/localtime" &&\
    echo "${TIMEZONE}" > "/etc/timezone" &&\
    apk del tzdata
COPY --from=builder /build/app /app/
USER 1000
WORKDIR app
CMD ["./app"]
