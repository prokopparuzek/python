#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import sys

root = Tk()

label = ttk.Label(root, text='Hello World!')
but = ttk.Button(root, text='Konec', command= lambda: sys.exit(0))

label.pack()
but.pack()

root.mainloop()
