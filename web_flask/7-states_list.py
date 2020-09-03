#!/usr/bin/python3
""" 7-states_list: Lists states """

from flask import Flask, render_template
from models import storage
from models.state import State

flap = Flask(__name__)


@flap.route("/states_list")
def states_list():
    """ returns template html with states listed """
    states = storage.all(State)
    _sorted = sorted(states.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=_sorted)


@flap.teardown_appcontext
def teardown(arg=None):
    """ teardown """
    storage.close()

if __name__ == "__main__":
    flap.url_map.strict_slashes = False
    flap.run(host="0.0.0.0", port="5000")
