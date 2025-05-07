import random, turtle
import tkinter as tk
from tkinter import colorchooser
import config

class MultiInputApp:
    '''
    Class for user input for various options including color, iterations, and text option
    '''
    def __init__(self, root, title, default, min, max):
        '''
        Initializes all labels and values

        Parameters:
        root: The root window as tk.Toplevel() to avoid clashing with the other windows
        title (str): Title of the popup window
        default (int): Default value for iterations
        min (int): Minimum value for iterations
        max (int): Maximum value for iterations
        '''

        # Sets up the popup window
        self.root = root
        if hasattr(self.root, 'title'):
            self.root.title(title)
        self.result = None

        self.min = min
        self.max = max
        
        # Color section
        tk.Label(root, text = "Color:").grid(row = 0, column = 0, padx = 5, pady = 5)
        self.color_var = tk.StringVar(value = "#000000")
        self.color_entry = tk.Entry(root, textvariable = self.color_var, width = 10)
        self.color_entry.grid(row = 0, column=1, padx=5, pady=5)
        
        # Buttons for color wheel and randomizing color
        tk.Button(root, text="Choose", command = self.choose_color).grid(row = 0, column = 2, padx = 5, pady = 5)
        tk.Button(root, text="Random", command = self.random_color).grid(row = 0, column = 3, padx = 5, pady = 5)
        
        # Iterations section
        tk.Label(root, text = f"Iterations ({min} - {max}):").grid(row = 1, column = 0, padx = 5, pady = 5)
        self.iter_var = tk.StringVar(value = str(default))

        # Setting up validation
        vcmd = (root.register(self.validate_digits), '%P')
        self.iter_entry = tk.Entry(root, textvariable = self.iter_var, validate = 'key', validatecommand = vcmd)
        self.iter_entry.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5, sticky = 'ew')

        # Text section
        tk.Label(root, text = "Show Text:").grid(row = 2, column = 0, padx = 5, pady = 5)

        # Default value and options to choose from
        self.bool_var = tk.StringVar(value = "True")
        options = ["True", "False"]
        self.bool_dropdown = tk.OptionMenu(root, self.bool_var, *options)
        self.bool_dropdown.grid(row = 2, column = 1, padx = 5, pady = 5)

        # Bottom Buttons
        tk.Button(root, text = "Confirm", command=self.confirm).grid(row = 3, column = 1, padx = 5, pady = 5)
        tk.Button(root, text = "Cancel", command=self.cancel).grid(row = 3, column = 2, padx = 5, pady = 5)
        
        # Code to keep window up until the user confirms or cancels
        self.root.protocol("WM_DELETE_WINDOW", self.cancel)
        self.root.wait_window()
    
    # Ensures the iterations is a number
    def validate_digits(self, new):
        return new.isdigit() or new == ""
    
    # Methods to pick color or randomize
    def choose_color(self):
        color = colorchooser.askcolor(title="Choose color")[1]
        if color:
            self.color_var.set(color)
    
    def random_color(self):
        self.color_var.set(self.randomize_color())
    
    @staticmethod
    def randomize_color():
        return "#{:06x}".format(random.randrange(0, 2 ** 24))

    # Method for when confirm is pressed
    def confirm(self):
        # Check for valid number of iterations
        try:
            value = int(self.iter_var.get())
            if not (self.min <= value <= self.max):
                tk.messagebox.showerror("Invalid Input", f"Iterations must be between {self.min} and {self.max}.")
                return
            self.result = {
                'color': self.color_var.get(),
                'iterations': value,
                'text_option': self.bool_var.get() == "True"
            }
        except ValueError:
            tk.messagebox.showerror("Invalid Input", "Please enter a valid integer for iterations.")
            return

        self.root.destroy()

    # Method for when cancel is pressed
    def cancel(self):
        # Clears dictionary and closes window
        self.result = None
        self.root.destroy()

def get_input(title, default, min, max):
    '''
    Popup menu for user input

    Parameters:
    default (int): Default value for iterations
    min (int): Minimum value for iterations
    max (int): Maximum value for iterations
    '''
    root = tk.Toplevel()
    app = MultiInputApp(root, title, default, min, max)
    return app.result

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

def set_text(text):
    '''
    Enables formula text to be shown on the canvas

    Parameter:
    text (string): The string to set the text to be shown
    '''
    config.text_option = True
    config.txt = text

def invert():
    '''
    Inverts the background (and text if necessary)
    '''
    if config.inv:
        set_bg("#FFFFFF")
        if config.text_option:
            write(config.inv, config.txt)
        config.inv = False
    else:
        set_bg("#000000")
        write(config.inv, config.txt)
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

def text(textOpt, text):
    '''
    Sets text value based on the message given

    Parameters:
    textOpt (bool): Chooses whether to show text message or not
    text (string): The text string value to output
    '''

    # If textOpt is false, the text will not show
    if not textOpt:
        config.txt = ""
        return
    write(txt = text)
    set_text(text)

def draw_image(x, y, path):
    '''
    Draws an image at the selected x and y value

    Parameters:
    x (int): x-coordinate to output image, based on the north-west starting position
    y (int): y-coordinate to output image, based on the north-west starting position
    path (str): path to the image file
    '''
    screen = turtle.Screen()
    canvas = screen.getcanvas()
    
    img = tk.PhotoImage(file = path)
    canvas.create_image(x, y, anchor = tk.NW, image = img)
    
    # Checks if canvas list was already created (if canvas already has an image attribute), if not create then append
    if not hasattr(canvas, 'images'):
        canvas.images = []
    canvas.images.append(img)