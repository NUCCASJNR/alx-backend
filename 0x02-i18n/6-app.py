#!/usr/bin/env python3

"""
This module contains a user login system
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

users: Dict = {
    1:
        {"name": "Balou",
         "locale": "fr",
         "timezone": "Europe/Paris"},
    2:
        {"name": "Beyonce",
         "locale": "en",
         "timezone": "US/Central"},
    3:
        {"name": "Spock",
         "locale": "kg",
         "timezone": "Vulcan"},
    4:
        {"name": "Teletubby",
         "locale": None,
         "timezone": "Europe/London"},
}


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    Return a user dictionary or None if the id
    couldn't be found
    """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """"RUns Before request"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Translates to the best match language"""
    locale: str = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

    if 'locale' in g.user:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    header_locale: str = request.headers.get("locale")
    if header_locale:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Index route for the flask app
    Returns:
            The translated text
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
