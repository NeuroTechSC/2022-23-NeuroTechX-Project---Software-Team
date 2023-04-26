from flask import Flask 
import requests
import pymongo
from pymongo import MongoClient
from io import BytesIO
from flask import Flask, send_file
#import requests
#import pymongo
#from pymongo import MongoClient
import csv

app = Flask(__name__)
client = MongoClient('mongodb://root:example@mongo:27017')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/')
def hello_world():
    return 'Hello Flafdsdk!!d'

@app.route('/export')
def export_data():
    # Grabbing the data from MongoDB
    data = collection.find({})
     #Writing to a CSV File
    with open("data.csv", "w") as f:
        csvwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in data:
            print(item)
            csvwriter.writerow([item['name'], item['_id']])
    #Close CSV file to user
    return send_file('data.csv', as_attachment=True)


if __name__ == '__main__':
    print(client.list_database_names())
    print("\n\n\n")
    db = client["mydatabase"]
    coll = db["mycollection"]
    post1 = {"name": "hello"}
    coll.insert_one(post1)
    results = coll.find({})
    print("found results:\n")
    for r in results:
        print(r)
    print("\n end results")
    app.run(debug = True, host = '0.0.0.0', port = 5001)