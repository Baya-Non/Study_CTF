import os
from PIL import Image

img = Image.open('sample2.png')

img_resize = img.resize((500, 500))
img_resize.save('dsample3.png')