from flask import Flask, request, jsonify
from sms import sendi
from classify import is_rotten, is_fruit
import io
from crop_hints import crop_to_hint

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/classify", methods=['POST'])
def classify():
    status = {}
    if 'file' not in request.files:
        status['success'] = 0
        return jsonify(status)

    r = 0
    t = 0
    status['success'] = 1
    images = crop_to_hint(request.files['file'].read())
    for content in range(len(images)):
        if is_fruit(images[content]):
            t += 1
            status[content]['supported'] = 1
            if is_rotten(images[content]):
                status[content]['rotten'] = 1
                r += 1
            else:
                status[content]['rotten'] = 0
        else:
            status[content]['supported'] = 0

        if r > 0:
            sendi(r, t)

    return jsonify(status)


app.run(host='0.0.0.0')
