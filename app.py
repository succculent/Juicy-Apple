from flask import Flask, request
from sms import sendi
from classify import is_apple, is_rotten
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/classify", methods=['POST'])
def classify():
    status = {}
    if is_apple(request.files['file']):
        status['apple'] = 1
        if is_rotten(request.files['file']):
            status['rotten'] = 1
        else:
            status['rotten'] = 0
    else:
        status['apple'] = 0
    return json.dumps(status)


app.run(host='0.0.0.0')
