FROM golang:1.17 as builder
RUN git clone "https://github.com/n-at/box" /build &&\
    cd /build &&\
    CGO_ENABLED=0 GOOS=linux go build -a -o app .

###############################################################################

FROM debian:bullseye
RUN apt-get update &&\
    apt-get install -y wget gnupg libncurses5 &&\
    \
    echo "deb http://apt.postgresql.org/pub/repos/apt bullseye-pgdg main" > /etc/apt/sources.list.d/pgdg.list &&\
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&\
    apt-get update &&\
    apt-get install -y postgresql-client-14 &&\
    \
    wget "https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2004-x86_64-100.5.2.tgz" -O mongodb5.tar.gz &&\
    tar -xvf mongodb5.tar.gz &&\
    rm mongodb5.tar.gz &&\
    mv "mongodb-database-tools-ubuntu2004-x86_64-100.5.2" "mongodb5" &&\
    \
    wget "https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.0.28.tgz" -O mongodb4.tar.gz &&\
    tar -xvf mongodb4.tar.gz &&\
    rm mongodb4.tar.gz &&\
    mv "mongodb-linux-x86_64-ubuntu1604-4.0.28" "mongodb4" &&\
    \
    wget "https://github.com/FirebirdSQL/firebird/releases/download/R2_5_9/FirebirdSS-2.5.9.27139-0.amd64.tar.gz" -O firebird.tar.gz &&\
    tar -xvf firebird.tar.gz &&\
    rm firebird.tar.gz &&\
    cd "FirebirdSS-2.5.9.27139-0.amd64" &&\
    tar -xvf buildroot.tar.gz &&\
    mv ./opt/firebird/ /opt &&\
    cd / &&\
    rm -rf "FirebirdSS-2.5.9.27139-0.amd64" &&\
    \
    apt-get purge --auto-remove -y wget gnupg

COPY --from=builder /build/app /app/
WORKDIR /app
USER 1000
VOLUME ["/app/logs"]
CMD ./app | tee -ia "/app/logs/$(date +"%Y_%m_%d_%H_%M_%S").log"