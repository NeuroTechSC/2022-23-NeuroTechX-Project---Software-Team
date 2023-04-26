import json

import gevent.monkey  # async alt to quart
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

from config import Config

# fix ssl inf recursion error
gevent.monkey.patch_all()


def create_app():
    print("init app...", end="", flush=True)
    app = Flask(__name__)
    app.config.from_object(Config)
    print("done")
    return app


app = create_app()


def register_blueprints(app):
    print("register blueprints...", end="", flush=True)
    from . import errors
    from .blueprints.home import home

    app.register_blueprint(home)
    print("done")


with app.app_context():
    print("add extensions...", end="", flush=True)
    CORS(app)

    client = MongoClient("mongodb://root:example@mongo:27017")
    print(client.list_database_names())
    print("\n\n\n")
    db = client["testdb"]
    coll = db["testcoll"]
    post1 = {"name": "hello"}
    coll.insert_one(post1)
    results = coll.find({})
    print("found results:\n")
    for r in results:
        print(r)
    print("\n end results")

    print("done")

    register_blueprints(app)
