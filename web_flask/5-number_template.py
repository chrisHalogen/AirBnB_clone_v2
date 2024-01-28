#!/usr/bin/python3
""" Starts a Flask Web App """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message at the root url """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints HBNB Message at /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints C <text> when /c is called """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """ Display Python <text> """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """ display “n is a number” if n is of int """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:num>', strict_slashes=False)
def numbers_and_templates(num):
    """ if n is an integer, display html """
    return render_template('5-number.html', num=num)

if __name__ == "__main__":
    """ Run Function """
    app.run(host='0.0.0.0', port=5000)
