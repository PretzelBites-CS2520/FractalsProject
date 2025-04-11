#file for adding extra features on top of the main fractal and gui stuff, could be random colors/shapes, maybe some extra user input stuff
#could rename the file later because its a bit too broad
import random
import tkinter as tk
from turtle import Screen

def randomizeColor():
    return "#{:06x}".format(random.randrange(0, 2 ** 24))

def makeButton(x, y, txt, cmd):
    screen = Screen()
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text = txt, command = cmd)
    button.config(bd = 0, font="Courier", padx=5, pady=5)
    button.pack()
    canvas.create_window(x, y, window = button)