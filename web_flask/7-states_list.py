#!/usr/bin/python3
""" Starts a Flask Web App """
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display Pages listed in alphabetical order """
    data = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def teardown_db(exception):
    """ on teardown, close storage """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')