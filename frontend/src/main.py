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
    app.run(debug = True, host = '0.0.0.0', port = 5001)