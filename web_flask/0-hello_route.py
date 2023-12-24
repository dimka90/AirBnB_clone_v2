#!/usr/bin/python3
"""
This module implements a simple Flask web application.
"""
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)
app.url_map.strict_slashes = False

# Decorate the entry point route
@app.route("/")
def entry() -> str:
    """
    Handle requests to the root URL ("/").

    Returns:
    - str: A greeting message, "Hello HBNB!"
    """

    return 'Hello HBNB!'

if __name__ == "__main__":
    # Run the Flask application on host "0.0.0.0" and port 5000
    app.run(host="0.0.0.0", port='5000')
