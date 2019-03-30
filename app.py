API_KEY="AIzaSyB1g5SVzfrZqzNQc_7HzJEJFzrnFG_kJEo"

from flask import Flask
app = Flask(__name__)

from google.cloud import vision
from google.cloud.vision import types

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

client = vision.ImageAnnotatorClient()

def open_image():
	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

@app.route("/")
def hello():
	return "Hello World!"

app.run(host='0.0.0.0')

