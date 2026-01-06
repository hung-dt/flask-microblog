from flask import render_template
from app import flask_app


@flask_app.route("/")
@flask_app.route("/index")
def index():
    user = {"username": "Hung"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
        {"author": {"username": "BSB"}, "body": "Show me the meaning of being lonely!"},
        {"author": {"username": "Avril Lavigne"}, "body": "My Happy Ending!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
