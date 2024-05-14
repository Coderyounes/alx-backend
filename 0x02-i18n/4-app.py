#!/usr/bin/env python3
""" Force locale with URL parameter """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the application.

    Attributes:
        LANGUAGES (list): List of supported languages for the application.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get the best matching language for the user based on their request headers.

    Returns:
        str: The best matching language code.
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """
    This function returns the rendered template '3-index.html'.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
