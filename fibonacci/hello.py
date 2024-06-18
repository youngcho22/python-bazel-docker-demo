from fibonacci import rainbow_fibonacci
from colorama import init
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    init()
    out = rainbow_fibonacci(20)
    return f'<p>Hello, {out} World!</p>'