import argparse
import io
from classify import localize_objects

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

'''def get_crop_hint(path):
    """Detect crop hints on a single image and return the first result."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    crop_hints_params = types.CropHintsParams(aspect_ratios=[1.77])
    image_context = types.ImageContext(crop_hints_params=crop_hints_params)

    response = client.crop_hints(image=image, image_context=image_context)
    hints = response.crop_hints_annotation.crop_hints

    # Get bounds for the first crop hint using an aspect ratio of 1.77.
    vertices = hints[0].bounding_poly.vertices

    return vertices
'''

'''def draw_hint(image_file):
    """Draw a border around the image using the hints in the vector list."""
    vects = localize_objects(image_file)
    im = Image.open(image_file)
    draw = ImageDraw.Draw(im)
    for i in range(0, vects.len()-1):
        draw.polygon([
            vects[i][0].x, vects[i][0].y,
            vects[i][1].x, vects[i][1].y,
            vects[i][2].x, vects[i][2].y,
            vects[i][3].x, vects[i][3].y], None, 'red')
    return im
'''
def crop_to_hint(image_file):
    """Crop the image using the hints in the vector list."""
    '''vects = localize_objects(image_file)

    im = Image.open(image_file)
    im2 = im.crop([vects[0].x, vects[0].y,
                  vects[2].x - 1, vects[2].y - 1])
    im2.save('output-crop.jpg', 'JPEG')
    print('Saved new image to output-crop.jpg')
    return im2
    '''

    vects = localize_objects(image_file)
    im = Image.open(image_file)
    im_list = []
    for i in range(0, len(vects)-1): #something
        im_list.append(im.crop([
            vects[i][0][0], vects[i][0][1],
            vects[i][1][0], vects[i][2][1]]))
            #vects[i][2][0], vects[i][2][1],
            #vects[i][3][0], vects[i][3][1]

    return im_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='The image you\'d like to crop.')
    parser.add_argument('mode', help='Set to "crop" or "draw".')
    args = parser.parse_args()

    parser = argparse.ArgumentParser()

    a = crop_to_hint(args.path)

    for i in range(0, len(a)-1): #something
        a[i].save(str(i) + ".jpg")
