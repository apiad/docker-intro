# coding: utf8

import sys
import pymongo

from flask import *


app = Flask(__name__)

client = pymongo.MongoClient("mongo", 27017)


@app.route("/")
def index():
    return str(client)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug="--debug" in sys.argv)
