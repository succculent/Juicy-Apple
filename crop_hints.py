import argparse
import io
from classify import localize_objects

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

def crop_to_hint(image_file):
    vects = localize_objects(image_file)
    im = Image.open(io.BytesIO(image_file))
    im_list = []
    for i in range(0, len(vects)):
        x_, y_ = im.size
        im_list.append(im.crop([
            vects[i][0][0]*x_, vects[i][0][1]*y_,
            vects[i][2][0]*x_, vects[i][2][1]*y_]))
    return im_list

