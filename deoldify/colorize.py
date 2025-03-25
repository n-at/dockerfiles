import os
import fnmatch
import torch
from deoldify.visualize import *

torch.backends.cudnn.benchmark = True

def get_files_with_extensions(directory, patterns):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                matched_files.append(os.path.join(root, filename))
    return matched_files

artistic = os.environ.get('COLORIZE_ARTISTIC')
artistic = (artistic == '1')

watermark = os.environ.get('COLORIZE_WATERMARK')
watermark = (watermark == '1')

render_factor = os.environ.get('COLORIZE_RENDER_FACTOR')
if render_factor is None or render_factor == '':
    render_factor = 28 if artistic else 20
else:
    render_factor = int(render_factor)

file_patterns = ['*.png', '*.jpg']
files_list = get_files_with_extensions('/DeOldify/source_images', file_patterns)

colorizer = get_image_colorizer(
    artistic=artistic,
    render_factor=render_factor
)

for file in files_list:
    print(file)
    colorizer.plot_transformed_image(
        path=file,
        figsize=(20, 20),
        render_factor=render_factor,
        display_render_factor=True,
        compare=False,
        watermarked=watermark
    )
