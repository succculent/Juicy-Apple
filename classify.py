import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
from google.cloud.vision import types
from google.cloud import vision

API_KEY = "AIzaSyB1g5SVzfrZqzNQc_7HzJEJFzrnFG_kJEo"

# To exectue the request:
# python predict.py YOUR_LOCAL_IMAGE_FILE juicy-apple ICN2381291597882699746
client = vision.ImageAnnotatorClient()


def is_rotten(content):
    project_id = "juicy-apple"
    #model_id = sys.argv[3]
    model_id = ICN2381291597882699746
    prediction_client = automl_v1beta1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(
        project_id, model_id)
    payload = {'image': {'image_bytes': content}}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned


def is_apple(content):
    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    for label in labels:
        if label.description == "Apple":
            return True

    return False
