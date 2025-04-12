#file for adding extra features on top of the main fractal and gui stuff, could be random colors/shapes, maybe some extra user input stuff
#could rename the file later because its a bit too broad
import random
import tkinter as tk
import turtle

def randomizeColor():
    return "#{:06x}".format(random.randrange(0, 2 ** 24))

def makeButton(x, y, txt, cmd):
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text = txt, command = cmd)
    button.config(bd = 0, font="Courier", padx=5, pady=5)
    button.pack()
    canvas.create_window(x, y, window = button)

def destroyButton():
    canvas = turtle.getcanvas()

    for button in canvas.master.winfo_children():
        if isinstance(button, tk.Button):
            button.destroy()

def setBG(col):
    turtle.bgcolor(col)

inv = False
textOption = False
txt = ""

def setText(text):
    global textOption, txt
    textOption = True
    txt = text

def invert():
    global inv, textOption
    if inv:
        setBG("#FFFFFF")
        if textOption:
            write(inv)
        inv = False
    else:
        setBG("#000000")
        write(inv)
        inv = True

def write(inv = True, txt = ""):
    turtle.penup()
    turtle.setposition(0, 250)

    if inv:
        turtle.color("#000000")
    else:
        turtle.color("#FFFFFF")
    turtle.write(txt, align="center", font=('Arial', 12, 'bold'))
    turtle.hideturtle()