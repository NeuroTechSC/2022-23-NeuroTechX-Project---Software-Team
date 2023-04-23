#Neuro-Tech Software 2022 - 2023
import pymongo
import csv

#Connecting to the MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['mydatabase']
collection = db['mycollection']
documents = collection.find()

with open('mycollection.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['_id', 'field1', 'field2'])
    # I need to replace 'field1', 'field2' with the names of the fields in the documents from the data
    for document in documents:
        writer.writerow([document['_id'], document['field1'], document['field2']])
        #  Again I need to replace 'field1', 'field2' with the names of the fields in the documents from the data
        









        



