#!/usr/bin/python3
""" 0-hello_route: Main route """
from flask import Flask

flap = Flask(__name__)


@flap.route("/", strict_slashes=False)
def hello():
    """ Returns 'Hello HBNB!' """
    return "Hello HBNB!"

if __name__ == "__main__":
    flap.run(host="0.0.0.0", port="5000")
