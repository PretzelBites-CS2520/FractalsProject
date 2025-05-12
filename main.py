import turtle
import fractals, config
import additional_features as features

def draw():
    reset()
    '''
    Draws a specified fractal
    '''

    match config.n:
        # Mandelbrot
        case 1:
            config.user_input = features.get_input("Parameters", 20, 15, 100)
            if config.user_input is not None:
                config.text_option = config.user_input['text_option']
                fractals.Mandelbrot(config.text_option, config.user_input['color'])

        # Koch Snowflake
        case 2:
            config.user_input = features.get_input("Parameters", 3, 2, 7)
            if config.user_input is not None:
                config.text_option = config.user_input['text_option']
                fractals.KochSnowflake(config.text_option, config.user_input['color'])

        # Sierpinski Triangle
        case 3:
            config.user_input = features.get_input("Parameters", 5, 1, 6)
            if config.user_input is not None:
                config.text_option = config.user_input['text_option']
                fractals.SierpinskiTriangle(config.text_option, config.user_input['color'])

        # Random Fractal
        case 4:
            config.user_input = features.get_input("Parameters", 25000, 10000, 100000)
            if config.user_input is not None:
                config.text_option = config.user_input['text_option']
                fractals.RandomFractal(config.text_option, config.user_input['color'])

        # Snowflake
        case 5:
            config.user_input = features.get_input("Parameters", 5, 1, 10)
            if config.user_input is not None:
                config.text_option = config.user_input['text_option']
                fractals.BasicSnowflake(config.text_option, config.user_input['color'])

        # Tree Fractal
        case 6:
            config.user_input = features.get_input("Parameters", 10, 1, 15)
            if config.user_input is not None:
                config.text_option = config.user_input['text_option']
                fractals.TreeFractal(config.text_option, config.user_input['color'])

def reset():
    '''
    Resets the canvas
    '''
    config.stop = True
    turtle.clearscreen()
    setup()

def done():
    '''
    Exits the program entirely
    '''
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
    val (int): Value from 1-6 correlating to which fractal the user chose
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
    features.draw_image(-60, -220, Path("images/treefractal.png"))

    # Sets up the buttons
    features.make_button(-250, -100, "Mandelbrot Set", lambda: setup_helper(1))
    features.make_button(250, -100, "Koch Snowflake", lambda: setup_helper(2))
    features.make_button(-250, 100, "Sierpinski Triangle", lambda: setup_helper(3))
    features.make_button(250, 100, "Random Fractal (EXP)", lambda: setup_helper(4))
    features.make_button(0, 100, "Basic Snowflake", lambda: setup_helper(5))
    features.make_button(0, -100, "Tree Fractal", lambda: setup_helper(6))
    features.make_button(0, 200, "Exit Program", done)

def main():
    config.init()
    screen = turtle.Screen()
    screen.setup(800, 600)
    menu_setup()
    turtle.mainloop()

if __name__ == '__main__':
    main()