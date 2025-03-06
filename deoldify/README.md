# DeOldify automated colorization

Colorize all images in source directory.

## Build

```bash
docker image build -t deoldify:latest .
```

## Running

```bash
docker run --rm --gpus=all \
    -v $(pwd)/source:/DeOldify/source_images \
    -v $(pwd)/result:/DeOldify/result_images \
    deoldify:latest
```

Optional environment variables:

* `COLORIZE_RENDER_FACTOR`
* `COLORIZE_ARTISTIC`
* `COLORIZE_WATERMARK`

## Uses

* [jantic/DeOldify](https://github.com/jantic/DeOldify) - MIT
