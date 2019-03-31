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

    status['success'] = 1
    content = request.files['file'].read()
    if is_fruit(content):
        status['supported'] = 1
        print("test rotten")
        if is_rotten(content):
            status['rotten'] = 1
        else:
            status['rotten'] = 0
    else:
        status['supported'] = 0
    if 'rotten' in status.keys():
        sendi(status['rotten'], 1)
    return jsonify(status)


app.run(host='0.0.0.0')
