import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
from google.cloud.vision import types
from google.cloud import vision

API_KEY = "AIzaSyB1g5SVzfrZqzNQc_7HzJEJFzrnFG_kJEo"

# To exectue the request:
# python predict.py YOUR_LOCAL_IMAGE_FILE juicy-apple ICN2381291597882699746
client = vision.ImageAnnotatorClient()

def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    o_v = []
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        if ((object_.name == "Apple") or (object_.name == "Orange") or (object_.name == "Banana")):
            a = []
            for vertex in object_.bounding_poly.normalized_vertices:
                a.append((vertex.x, vertex.y))
            o_v.append(a)
    return (o_v)

def is_rotten(content):
    project_id = "juicy-apple"
    model_id = "ICN2381291597882699746"
    prediction_client = automl_v1beta1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(
        project_id, model_id)
    payload = {'image': {'image_bytes': content}}
    params = {}
    request = prediction_client.predict(name, payload, params)
    for result in request.payload:
        if(result.display_name == "rotten"):
            return True
    return False
    #return request  # waits till request is returned


def is_fruit(content):
    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        if label.description == "Apple":
            return True

    return False
