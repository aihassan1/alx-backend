#!/usr/bin/env python3
"""
    Contains a basic flask app displaying 'Welcome to Holberton' on
    a single route '/'
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """configuration for babel"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """this method checks the URL parameter for locale variable
    and force the Locale of the app"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """this route renders 0-index.html template"""

    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
