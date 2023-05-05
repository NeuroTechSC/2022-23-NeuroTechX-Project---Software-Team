import tkinter as tk
from time import sleep
from listener import *

def click(stringVar):
    stringVar.set("Hello, Another!")

def funcionally_create_items(gui):
    gui.button=tk.Button(gui.root, text="click2")
    gui.button.pack()

class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.buffer = []
        self.currentItem = None

        # Start socket server
        
        self.string = tk.StringVar()
        self.string.set("Hello, World!")

        self.label = tk.Label(self.root, textvariable=self.string, font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click", command=lambda: click(self.string))
        self.button.pack()
        funcionally_create_items(self)

        # Start GUI
        self.root.mainloop()

    # Get HTTP input
    def input(self) -> None:
        pass

    # Update items that are rendered on the GUI
    def update(self) -> None:
        pass

gui1 = GUI()