import flask

from app import app

user = {"username": "Aboba"}


@app.route('/')
def index():
    return flask.render_template("index.html")
