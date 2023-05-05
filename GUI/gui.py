from collections.abc import Callable, Iterable, Mapping
import tkinter as tk
import time
from typing import Any
from listener import *
from helper import *
import threading

def click(stringVar):
    stringVar.set("Hello, Another!")


class gui_c(threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.i = 0

        self.root = tk.Tk()
        self.currentItem = None

        self.string = tk.StringVar()
        self.string.set("Hello, World!")

        self.label = tk.Label(self.root, textvariable=self.string, font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click", command=lambda: click(self.string))
        self.button.pack()

        self.itemstr = tk.StringVar()
        self.itemstr.set("None")
        self.item = tk.Label(self.root, textvariable=self.itemstr, font=('Arial', 18))
        self.item.pack()

    def update(self):
        item = None
        self.i += 1
        self.string.set(self.i)
        current_item = buffer_pop(buffer)
        if current_item != None:
            self.itemstr.set((current_item))
        self.root.after(200, self.update)
        return
    
    def run(self):
        self.root.after(1, self.update)
        self.root.mainloop()