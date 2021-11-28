FROM openjdk:17-slim-bullseye as builder
ARG MAVEN_OPTS
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTENTD=noninteractive
RUN apt-get update &&\
    apt-get install -y git &&\ 
    git clone "https://github.com/n-at/trending-stream" build &&\
    cd build &&\
    ./mvnw clean package

FROM openjdk:17-slim-bullseye
ENV LANG=C.UTF-8
COPY --from=builder /build/target/trending-stream.jar /app/
WORKDIR /app
VOLUME ["/app/logs", "/app/db"]
CMD java ${JAVA_OPTS} -jar /app/trending-stream.jar
