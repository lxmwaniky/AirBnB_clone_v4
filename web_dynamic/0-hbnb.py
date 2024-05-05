#!/usr/bin/python3
""" Starts a Flask Web Application """
import uuid

from flask import Flask, render_template

from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(_):
    storage.close()


@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """
    Renders the '0-hbnb.html' template with the necessary data.

    Retrieves all states, amenities, and places from the storage.
    Sorts the states, amenities, and places alphabetically.
    Creates a list of states and their corresponding cities.
    Generates a cache_id using the uuid module.

    Returns:
        The rendered template '0-hbnb.html' with the following parameters:
        - states: A list of states and their corresponding cities.
        - amenities: A list of amenities.
        - places: A list of places.
        - cache_id: A unique identifier for caching purposes.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
