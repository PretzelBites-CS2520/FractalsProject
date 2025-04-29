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