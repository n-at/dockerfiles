FROM golang:1.17 as builder
RUN apt-get update &&\
    apt-get install -y git curl gpg &&\
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | gpg --dearmor >> /nodesource-key.gpg &&\
    echo "deb [signed-by=/nodesource-key.gpg] https://deb.nodesource.com/node_16.x bullseye main" >> /etc/apt/sources.list.d/nodesource.list &&\
    echo "deb-src [signed-by=/nodesource-key.gpg] https://deb.nodesource.com/node_16.x bullseye main" >> /etc/apt/sources.list.d/nodesource.list &&\
    apt-get install -y nodejs npm &&\
    \
    git clone "https://github.com/n-at/contest-registration-bot" /build &&\
    cd /build &&\
    CGO_ENABLED=0 GOOS=linux go build -a -o app . &&\
    cd assets &&\
    npm install

###############################################################################

FROM alpine
COPY --from=builder /build/assets /app/assets/
COPY --from=builder /build/templates /app/templates/
COPY --from=builder /build/app /app/
USER 1000
WORKDIR /app
VOLUME ["/app/data"]
EXPOSE 3000
CMD ["./app"]
