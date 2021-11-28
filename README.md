# dockerfiles

Dockerfiles for some services

## Building

```bash
docker image build -f releases-stream/Dockerfile -t releases-stream:latest 
docker image build -f trending-stream/Dockerfile -t trending-stream:latest 
docker image build -f stock-monitoring/Dockerfile -t stock-monitoring:latest 
```
