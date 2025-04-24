import turtle
import fractals, config
import additional_features as features
#main file for running the program, could use this to contain the gui stuff as well
#also could maybe just throw everything into one file but it might get docked for poor organization or something

# note: if creating separate page for user to choose, maybe add a parameter (like int or char) for a case/switch branch statement
def draw():
    reset()
    '''
    Draws a specified fractal
    '''
    fractals.Mandelbrot(True, 0, features.randomize_color())
    #fractals.KochSnowflake(False, features.randomize_color())
    #fractals.SierpinskiTriangle(False, features.randomize_color())
    #fractals.RandomFractal(False, features.randomize_color())

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

def setup():
    '''
    Sets up all the buttons on the canvas
    '''
    features.destroy_button()

    features.make_button(-350, -275, "Draw", draw)
    features.make_button(-250, -275, "Reset", reset)
    features.make_button(-150, -275, "Invert", features.invert)
    features.make_button(-350, -225, "Exit", done)

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    setup()
    turtle.mainloop()

if __name__ == '__main__':
    main()