from flask import Flask, request
from sms import sendi
from classify import is_apple, is_rotten

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/classify", methods=['POST'])
def classify():
    if is_apple(request.files['file']):
        if is_rotten(request.files['file']):
            return "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!"
    return "no u"


app.run(host='0.0.0.0')
