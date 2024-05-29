#!/usr/bin/env python3
"""task 3"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home():
    """home page"""
    title = _("home_title")
    header = _("home_header")
    return render_template("index.html", title=title, header=header)


if __name__ == "__main__":
    app.run(debug=True)
