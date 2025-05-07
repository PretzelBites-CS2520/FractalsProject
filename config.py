# File to contain global variables to be used in other files

def init():
    # Global flag to stop process and wait for button press
    global stop
    stop = False

    # Check for invert
    global inv
    inv = False

    # Global variable for selecting fractal from main menu
    global n
    n = 0

    # Global variables for the text to show
    global txt
    txt = ""

    # Variable to check whether or not to show text
    global text_option
    text_option = False

    # Dictionary for user input from the popup window
    global user_input
    user_input = {}