#!/usr/bin/python3
""" Starts a Flask Web App """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message at the root url """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Run Function """
    app.run(host='0.0.0.0', port=5000)
