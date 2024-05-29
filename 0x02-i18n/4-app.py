#!/usr/bin/env python3
"""
    Contains a basic flask app displaying 'Welcome to Holberton' on
    a single route '/'
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration class for Flask application.

    Attributes:
        LANGUAGES (list): The languages supported by the application.
        BABEL_DEFAULT_LOCALE (str): The default language locale.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for user's accepted languages.

    Returns:
        str: The best language match from accepted languages.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """
    Render the home page.

    Returns:
        str: HTML of the home page.
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
