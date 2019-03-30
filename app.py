from flask import Flask
from sms import sendi
from classify import is_apple, is_rotten

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


app.run(host='0.0.0.0')
