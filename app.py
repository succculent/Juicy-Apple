from flask import Flask, request, jsonify
from sms import sendi
from classify import is_rotten
import io
from crop_hints import crop_to_hint
from PIL import Image, ImageDraw

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
    status['fruit'] = []
    images = crop_to_hint(request.files['file'].read())
    for im in images:
        temp = {}
        t += 1
        i = io.BytesIO()
        im.save(i, format='PNG')
        i = i.getvalue()
        temp['supported'] = 1        
        if is_rotten(i):
            temp['rotten'] = 1
            r += 1
        else:
            temp['rotten'] = 0
        status['fruit'].append(temp)

        if r > 0:
            sendi(r, t)

    return jsonify(status)


app.run(host='0.0.0.0')
