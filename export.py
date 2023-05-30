from collections.abc import Callable, Iterable, Mapping
import tkinter as tk
import threading
import pymongo
import csv

class SubvocalPhonemeGUI(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

        #Creating the main window of the application 
        self.root = tk.Tk()

         #Setting up GUI elements 
        self.label = tk.Label(self.root, text="Hello, World!", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click", command=lambda: self.export_data())
        self.button.pack()

        self.button = tk.Button(self.root, text="Export Data", command=self.export_data)
        self.button.pack()

        #Connecting to the MongoDB 
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["subvocal_database"]
        self.collection = self.db["subvocal_collection"]

    def export_data(self):
      self.status_label.config(text="Exporting Data...")

      #Query the data from the MongoDB
      #Limiting the data amount 50 lines
      data = self.collection.find({}).limit(50)

      #Write the data to a CSV file 
      with open('data_export.csv', 'w') as f:
        csvwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #write each row of data
        for item in data:
          csvwriter.writerow([item['name'], item['_id']])
      #return send_file('data.csv', as_attachment=True)

      self.status_label.config(text="Data Exported Successfully")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    gui = SubvocalPhonemeGUI(1)
    gui.start()
    gui.join()
