FROM continuumio/miniconda3:25.1.1-2

ENV COLORIZE_RENDER_FACTOR=""
ENV COLORIZE_ARTISTIC="1"
ENV COLORIZE_WATERMARK="1"

RUN apt-get update &&\
    apt-get install -y ffmpeg &&\
    git clone https://github.com/jantic/DeOldify &&\
    cd DeOldify &&\
    mkdir -m 0777 source_images result_images &&\
    conda env create -f environment.yml &&\
    wget -O "models/ColorizeArtistic_gen.pth" "https://local.doublebyte.ru/static/DeOldify/ColorizeArtistic_gen.pth" &&\
    wget -O "models/ColorizeStable_gen.pth" "https://local.doublebyte.ru/static/DeOldify/ColorizeStable_gen.pth" &&\
    mkdir -p /root/.cache/torch/hub/checkpoints/ &&\
    wget -O "/root/.cache/torch/hub/checkpoints/resnet34-b627a593.pth" "https://download.pytorch.org/models/resnet34-b627a593.pth"
    
ADD colorize.py /DeOldify/

VOLUME ["/DeOldify/source_images", "/DeOldify/result_images"]

WORKDIR /DeOldify

CMD /bin/bash -c 'source activate base && conda activate deoldify && python colorize.py && chmod 0666 result_images/*'
