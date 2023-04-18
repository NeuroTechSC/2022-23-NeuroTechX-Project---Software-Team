from flask import Flask 
import requests
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://root:example@mongo:27017')

@app.route('/')
def hello_world():
    return 'Hello Flafdsdk!!d'

if __name__ == '__main__':
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
    app.run(debug = True, host = '0.0.0.0', port = 5001)