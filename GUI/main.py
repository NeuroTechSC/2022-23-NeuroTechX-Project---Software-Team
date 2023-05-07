import tkinter as tk
import time
from listener import *
from gui import *
from helper import *
import threading


if __name__ == "__main__":
    # Start socket listener and gui thread
    listener_thread = socket_thread_c(1)
    gui_thread = gui_c(2)

    # Start GUI
    gui_thread.run()