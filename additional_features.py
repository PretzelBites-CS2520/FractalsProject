#file for adding extra features on top of the main fractal and gui stuff, could be random colors/shapes, maybe some extra user input stuff
#could rename the file later because its a bit too broad
import random
import tkinter as tk
import turtle

def randomize_color():
    '''
    Simple generator for random hex colors

    Returns a random hex-code color string
    '''
    return "#{:06x}".format(random.randrange(0, 2 ** 24))

def make_button(x, y, txt, cmd):
    '''
    Creates a button

    Parameters:
    x (int): X-coordinate location of button
    y (int): Y-coordinate location of button
    txt (string): Text displayed on the button
    cmd: Function of the button
    '''
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    button = tk.Button(canvas.master, text = txt, command = cmd)
    button.config(bd = 0, font="Courier", padx=5, pady=5)
    button.pack()
    canvas.create_window(x, y, window = button)

def destroy_button():
    '''
    Destroys all buttons in the canvas
    '''
    canvas = turtle.getcanvas()

    for button in canvas.master.winfo_children():
        if isinstance(button, tk.Button):
            button.destroy()

def set_bg(col):
    '''
    Sets the background of the canvas

    Parameter:
    col (string): Color to change the background to
    '''
    turtle.bgcolor(col)

# Global variables to help with method functions
inv = False
textOption = False
txt = ""

def setText(text):
    '''
    Enables formula text to be shown on the canvas

    Parameter:
    text: The string to set the text to be shown
    '''
    global textOption, txt
    textOption = True
    txt = text

def invert():
    '''
    Inverts the background (and text if necessary)
    '''
    global inv, textOption
    if inv:
        set_bg("#FFFFFF")
        if textOption:
            write(inv, txt)
        inv = False
    else:
        set_bg("#000000")
        write(inv, txt)
        inv = True

def write(inv = True, txt = ""):
    '''
    Helper method to write the text on the canvas

    Parameters:
    inv (boolean): Checks if text color needs to be changed based on if the background is inverted
    txt (string): The string to set the text to
    '''
    turtle.penup()
    turtle.setposition(0, 250)

    # Changes text color based on if the background is inverted
    if inv:
        turtle.color("#000000")
    else:
        turtle.color("#FFFFFF")
    
    # Writes text on the canvas based on parameter txt
    turtle.write(txt, align="center", font=('Arial', 12, 'bold'))
    turtle.hideturtle()

def variables(default, min, max):
    '''
    Method of getting user input for number of iterations

    Parameters:
    default: default value
    min: min value
    max: max value
    '''
    global stop
    screen = turtle.Screen()
    iterations = screen.numinput("Iterations", f"Number of recursive iterations:\n({min} - {max})", default, min, max)
    if iterations is None:
        stop = True
        return None
    return int(iterations)

def text(textOpt, text):
    if not textOpt:
        return
    write(txt = text)
    setText(text)