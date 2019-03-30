from flask import Flask, request, jsonify
from sms import sendi
from classify import is_rotten, is_apple


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
    if is_apple(request.files['file']):
        status['apple'] = 1
        print("test rotten")
        if is_rotten(request.files['file']):
            status['rotten'] = 1
        else:
            status['rotten'] = 0
    else:
        status['apple'] = 0
    return type(request.files['file'])


app.run(host='0.0.0.0')
