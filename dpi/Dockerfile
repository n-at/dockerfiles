FROM golang:1.22 as builder

RUN cd / &&\
    git clone https://github.com/xvzc/SpoofDPI build &&\
    cd /build &&\
    git checkout a2993ac68d87a0525a93bc23984d21e341214199 &&\
    go build -o app ./cmd/... &&\
    ls -hal

FROM ubuntu:24.04
COPY --from=builder /build/app /app/
ADD run.sh /app/
RUN useradd --user-group --system worker
USER worker
WORKDIR /app
EXPOSE 8080
CMD ["./run.sh"]
