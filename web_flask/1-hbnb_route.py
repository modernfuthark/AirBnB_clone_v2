#!/usr/bin/python3
""" 1-hbnb_route: hbnb route """
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

if __name__ == "__main__":
    flap.run(host="0.0.0.0", port="5000")
