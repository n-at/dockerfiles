FROM golang:1.22 as builder

RUN cd / &&\
    git clone https://github.com/xvzc/SpoofDPI build &&\
    cd /build &&\
    git checkout c31fc376108be11e02daa1b09c5fedee921fd7ee &&\
    go build -o app ./cmd/... &&\
    ls -hal

FROM ubuntu:22.04
COPY --from=builder /build/app /app/
ADD run.sh /app/
RUN useradd --user-group --system worker
USER worker
WORKDIR /app
EXPOSE 8080
CMD ["./run.sh"]
