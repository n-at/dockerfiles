FROM golang:1.17 as builder
ARG REPO_LOGIN
ARG REPO_PASSWORD
RUN apt-get update &&\
    apt-get install -y git &&\
    \
    git clone "https://${REPO_LOGIN}:${REPO_PASSWORD}@github.com/n-at/mm-auto-status-update" /build &&\
    cd /build &&\
    CGO_ENABLED=0 GOOS=linux go build -a -o app .

############################################################################### \

FROM alpine:latest
ARG TIMEZONE="Europe/Moscow"
RUN apk -update add tzdata &&\
    cp "/usr/share/zoneinfo/${TIMEZONE}" "/etc/localtime" &&\
    echo "${TIMEZONE}" > "/etc/timezone" &&\
    apk del tzdata
COPY --from=builder /build/app /app/
USER 1000
WORKDIR app
CMD ["./app"]
