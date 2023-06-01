
import tkinter as tk
import random


class checkPhoneme():

#get a generate_random_object from test

   

    def check(self,current_item):

        user = random.randrange(0, 5)

        if(current_item["phoneme"] == user):
                print("correct")
                print(user)
                self.itemstr.set("correct")

        else:
                print("incorrect")
                print (user)
                self.itemstr.set("incorrect")

        if current_item == None:
            print ("nothing")

    


