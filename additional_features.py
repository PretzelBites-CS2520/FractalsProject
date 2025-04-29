import random, turtle
import tkinter as tk
import config

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
textOption = False
txt = ""

def set_text(text):
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
    global textOption
    if config.inv:
        set_bg("#FFFFFF")
        if textOption:
            write(config.inv, txt)
        config.inv = False
    else:
        set_bg("#000000")
        write(config.inv, txt)
        config.inv = True

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
    screen = turtle.Screen()
    iterations = screen.numinput("Iterations", f"Number of recursive iterations:\n({min} - {max})", default, min, max)
    if iterations is None:
        config.stop = True
        return None
    return int(iterations)

def text(textOpt, text):
    if not textOpt:
        global txt
        txt = ""
        return
    write(txt = text)
    set_text(text)

def draw_image(x, y, path):
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    
    img = tk.PhotoImage(file = path)
    canvas.create_image(x, y, anchor = tk.NW, image = img)
    
    # Checks if canvas list was already created (if canvas already has an image attribute), if not create then append
    if not hasattr(canvas, 'images'):
        canvas.images = []
    canvas.images.append(img)