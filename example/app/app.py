# coding: utf8

import sys

from flask import *

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug="--debug" in sys.argv)
