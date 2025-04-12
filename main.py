import fractals
import additional_features as features
import turtle
#main file for running the program, could use this to contain the gui stuff as well
#also could maybe just throw everything into one file but it might get docked for poor organization or something

def draw():
    #fractals.Mandelbrot(True, 0, features.randomizeColor())
    fractals.KochSnowflake(features.randomizeColor(), 3)

def reset():
    fractals.stop = True
    turtle.clearscreen()
    setup()

def setup():
    features.destroyButton()

    features.makeButton(-350, -275, "Draw", draw)
    features.makeButton(-250, -275, "Reset", reset)
    features.makeButton(-150, -275, "Invert", features.invert)
    features.makeButton(-350, -225, "Exit", exit)

def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    setup()
    turtle.mainloop()

if __name__ == '__main__':
    main()