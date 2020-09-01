#!/usr/bin/python3
""" 4-number_route: number route """
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


@flap.route("/python", strict_slashes=False)
@flap.route("/python/<txt>", strict_slashes=False)
def python(txt="is cool"):
    """ Returns Python followed by a string """
    return "Python " + txt.replace("_", " ")


@flap.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Returns 'n is a number' """
    return "{} is a number".format(n)

if __name__ == "__main__":
    flap.run(host="0.0.0.0", port="5000")
