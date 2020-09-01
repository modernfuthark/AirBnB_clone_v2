#!/usr/bin/python3
""" 2-c_route: c route """
from flask import Flask

flap = Flask(__name__)


@flap.route("/", strict_slashes=False)
def hello():
    """ Returns 'Hello HBNB!' """
    return "Hello HBNB!"


@flap.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns 'HBNB' """
    return "HBNB"


@flap.route("/c/<txt>", strict_slashes=False)
def c(txt):
    """ Returns C followed by a string """
    return "C " + txt.replace("_", " ")

if __name__ == "__main__":
    flap.run(host="0.0.0.0", port="5000")
