import turtle
import fractals, config
import additional_features as features
#main file for running the program, could use this to contain the gui stuff as well
#also could maybe just throw everything into one file but it might get docked for poor organization or something

# note: if creating separate page for user to choose, maybe add a parameter (like int or char) for a case/switch branch statement
def draw(n):
    reset()
    '''
    Draws a specified fractal
    
    Parameters:
    n (int) - specifies the number of the fractal to be drawn
    '''
    if n == 1:
        fractals.Mandelbrot(True, 0, features.randomize_color())
    elif n == 2:
        fractals.KochSnowflake(False, features.randomize_color())
    elif n == 3:
        fractals.SierpinskiTriangle(False, features.randomize_color())
    elif n == 4:
        fractals.RandomFractal(False, features.randomize_color())

def reset():
    '''
    Resets the canvas
    '''
    config.stop = True
    turtle.clearscreen()
    setup()

def done():
    reset()
    turtle.Screen().bye()

def setup(n=0):
    '''
    Sets up all the buttons on the canvas

    Parameters:
    n (int) - specifies the number of the fractal to be drawn
    '''
    features.destroy_button()

    features.make_button(-350, -275, "Draw", lambda: draw(n))
    features.make_button(-250, -275, "Reset", reset)
    features.make_button(-150, -275, "Invert", features.invert)
    features.make_button(-350, -225, "Back", menu_setup)

def menu_setup():
    '''
    Sets up the main menu where the user can select which fractal they would like to view
    '''
    reset()
    features.destroy_button()

    features.make_button(-100, -100, "Mandelbrot Set", lambda: setup(1))
    features.make_button(-100, 100, "Koch Snowflake", lambda: setup(2))
    features.make_button(100, 100, "Sierpinski Triangle", lambda: setup(3))
    features.make_button(100, -100, "Random Fractal", lambda: setup(4))
    features.make_button(-25, 200, "Exit Program", done)

def main():
    config.init()
    screen = turtle.Screen()
    screen.setup(800, 600)
    menu_setup()
    turtle.mainloop()

if __name__ == '__main__':
    main()