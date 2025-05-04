FROM golang:1.24 as builder
RUN git clone "https://github.com/n-at/releases-stream-v2" /build &&\
    cd /build &&\
    CGO_ENABLED=0 GOOS=linux go build -a -o app .

###############################################################################

FROM ubuntu:24.04
RUN apt-get update && apt-get install -y ca-certificates
COPY --from=builder /build/app /app/
WORKDIR /app
USER 1000
VOLUME ["/app/logs"]
CMD ./app | tee -ia "/app/logs/$(date +"%Y_%m_%d_%H_%M_%S").log"
