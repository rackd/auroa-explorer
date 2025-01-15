import tkinter as tk
from tkinter import *

class Gui:
    def __init__(self, title, w, h, bg_color):
        self.root = tk.Tk()
        self.root.title(title)
        self.canvas = tk.Canvas(self.root, width=w, height=h, bg=bg_color, bd=0, highlightthickness=0)
        self._createNavigationBar()
        self.canvas.pack()
    def run(self):
        self.root.mainloop()
    def _createNavigationBar(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open")
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit")
        menubar.add_cascade(label="File")

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index")
        helpmenu.add_command(label="About...")
        menubar.add_cascade(label="Help")

        self.root.config(menu=menubar)
    def donothing(self):
        x=3