#!/usr/bin/python3
""" 9-states: Lists states, if given a state id, give cities too """

from flask import Flask, render_template
from models import storage
from models.state import State

flap = Flask(__name__)


@flap.route("/states")
@flap.route("/states/<int:id>")
def states(id=None):
    """ returns rendered html listing states """
    states = storage.all(State)
    return render_template("9-states.html", states=states, id=id)


@flap.teardown_appcontext
def teardown(arg=None):
    """ teardown """
    storage.close()

if __name__ == "__main__":
    flap.url_map.strict_slashes = False
    flap.run(host="0.0.0.0", port="5000")
