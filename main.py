import turtle
import fractals, config
import additional_features as features

def draw():
    reset()
    '''
    Draws a specified fractal
    
    Parameters:
    n (int) - specifies the number of the fractal to be drawn
    '''
    if config.n == 1:
        fractals.Mandelbrot(True, 0, features.choose_color())
    elif config.n == 2:
        fractals.KochSnowflake(False, features.choose_color())
    elif config.n == 3:
        fractals.SierpinskiTriangle(False, features.choose_color())
    elif config.n == 4:
        fractals.RandomFractal(False, features.choose_color())
    elif config.n == 5:
        fractals.BasicSnowflake(False, features.choose_color())

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

    Parameters:
    n (int) - specifies the number of the fractal to be drawn
    '''
    turtle.clearscreen()
    features.destroy_button()
    
    features.make_button(-350, -275, "Draw", lambda: draw())
    features.make_button(-250, -275, "Reset", reset)
    features.make_button(-150, -275, "Invert", features.invert)
    features.make_button(-350, -225, "Back", menu_setup)

def setup_helper(val):
    '''
    Helper method to set global variable and call setup method

    Parameters:
    val (int): Value from 1-4 correlating to which fractal the user chose
    '''
    config.n = val
    setup()

def menu_setup():
    '''
    Sets up the main menu where the user can select which fractal they would like to view
    '''
    reset()
    config.n = 0
    features.destroy_button()

    # Sets up the images
    from pathlib import Path #importing this library to deal with issues in operating systems
    features.draw_image(-330, -220, Path("images/mandelbrot.png"))
    features.draw_image(180, -220, Path("images/koch.png"))
    features.draw_image(-330, -30, Path("images/sierpinski.png"))
    features.draw_image(180, -30, Path("images/random.png"))
    features.draw_image(-55, -30, Path("images/basicsnowflake.png"))

    # Sets up the buttons
    features.make_button(-250, -100, "Mandelbrot Set", lambda: setup_helper(1))
    features.make_button(250, -100, "Koch Snowflake", lambda: setup_helper(2))
    features.make_button(-250, 100, "Sierpinski Triangle", lambda: setup_helper(3))
    features.make_button(250, 100, "Random Fractal (EXP)", lambda: setup_helper(4))
    features.make_button(0, 100, "Basic Snowflake", lambda: setup_helper(5))
    features.make_button(0, 200, "Exit Program", done)

def main():
    config.init()
    screen = turtle.Screen()
    screen.setup(800, 600)
    menu_setup()
    turtle.mainloop()

if __name__ == '__main__':
    main()