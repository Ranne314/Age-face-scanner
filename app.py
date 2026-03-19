from flask import Flask # this model loading in flask dont work so dont use this

with open('index.html', 'r') as f:
    content = f.read()

app = Flask(__name__)

@app.route("/")
def home():
    return content