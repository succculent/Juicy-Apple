API_KEY="AIzaSyB1g5SVzfrZqzNQc_7HzJEJFzrnFG_kJEo"

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
