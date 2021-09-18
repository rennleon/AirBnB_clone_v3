#!/usr/bin/python3
"""This module starts a flask app"""
from os import getenv
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Handle teardown"""
    storage.close()


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns a text when / route is requested"""
    return 'Hello HBNB!'


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    return jsonify({"error": "Not found"})


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port)
