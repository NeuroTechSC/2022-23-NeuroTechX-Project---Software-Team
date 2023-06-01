from collections.abc import Callable, Iterable, Mapping
import tkinter as tk
import time
from typing import Any
from listener import *
from helper import *
import threading
from component import checkPhoneme

def click(stringVar):
    stringVar.set("Hello, Another!")


class gui_c(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.status = 'stopped'

        self.root = tk.Tk()
        self.components = []

        # YOUR CODE BELOW
        
        # Start/Stop Button
        self.buttonStr = tk.StringVar(self.root, 'Start')
        self.startStopButton = tk.Button(self.root, 
                                         textvariable=self.buttonStr,
                                         command = lambda: startStopButtonFunc(self, self.buttonStr)
                                        )
        self.startStopButton.pack()

        self.itemstr = tk.StringVar()
        self.itemstr.set("None")
        self.item = tk.Label(self.root, textvariable=self.itemstr, font=('Arial', 18))
        self.item.pack()

    def update(self):
        # Get current item
        current_item = buffer_pop(buffer)

        # Set status
        # if self.buttonStr.get() == 'Start':
        #     self.status = 'stopped'
        # else:
        #     self.status = 'running'
        print(self.status)
        if current_item != None:

            # Update all components
            self.itemstr.set(current_item)
            checkPhoneme.check(self,current_item)




        # Keep this last
        self.root.after(500, self.update)
        return
    
    def run(self):
        self.root.after(1, self.update)
        self.root.mainloop()


def startStopButtonFunc(obj, stringvar) -> str:
    if stringvar.get() == 'Start':
        stringvar.set('Stop')
        obj.status = 'running'
        return 'running'
    else:
        stringvar.set('Start')
        obj.status = 'stopped'
        return 'stopped'
