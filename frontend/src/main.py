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
    data = collection.find()
     #Writing to a CSV File
    display = BytesIO()
    writer  = csv.writer(display)
    for text in data:
        writer.writerow([text['_id'], text['name']])
    with open("data.csv", "wb") as f:
        f.write(display.getbuffer())
    #Close CSV file to user
    display.seek(0)
    return send_file('data.csv', as_attachment=True)


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