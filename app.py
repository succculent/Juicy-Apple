from flask import Flask, request, jsonify
from sms import sendi
from classify import is_rotten, is_apple
import io


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
    with io.open(request.files['file'].stream) as img:
        content = img.read()
        if is_apple(content):
            status['apple'] = 1
            print("test rotten")
            if is_rotten(content):
                status['rotten'] = 1
            else:
                status['rotten'] = 0
        else:
            status['apple'] = 0
        return jsonify(status)


app.run(host='0.0.0.0')
