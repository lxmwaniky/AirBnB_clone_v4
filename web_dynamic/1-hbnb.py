#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
import uuid
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/1-hbnb')
def display_hbnb():
    """
    Display the HBNB page with states, amenities, places, and a cache ID.

    Returns:
        The rendered template '1-hbnb.html' with the following variables:
        - states: All the states
        - amenities: All the amenities
        - places: All the places
        - cache_id: A unique cache ID generated using uuid.uuid4()
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('1-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
