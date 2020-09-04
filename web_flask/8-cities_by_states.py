#!/usr/bin/python3
""" 8-cities_by_states: Lists cities by states """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

flap = Flask(__name__)


@flap.route("/cities_by_states")
def cities_by_states():
    """ returns template html with cities listed by states """
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@flap.teardown_appcontext
def teardown(arg=None):
    """ teardown """
    storage.close()

if __name__ == "__main__":
    flap.url_map.strict_slashes = False
    flap.run(host="0.0.0.0", port="5000")
