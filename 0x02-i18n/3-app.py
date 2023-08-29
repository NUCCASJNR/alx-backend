#!/usr/bin/env python3

"""Contains a flask app and a babel class"""

from flask import Flask, render_template
from flask_babel import Babel, gettext


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Index route for the flask app
    Returns:
            The translated text
    """
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    return render_template('3-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
