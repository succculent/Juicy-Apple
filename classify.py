import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
from google.cloud.vision import types
from google.cloud import vision

API_KEY = "AIzaSyB1g5SVzfrZqzNQc_7HzJEJFzrnFG_kJEo"

client = vision.ImageAnnotatorClient()

def localize_objects(content):
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    o_v = []

    for object_ in objects:
        if object_.name == "Fruit":
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
