import fractals
import additional_features as features
import turtle
#main file for running the program, could use this to contain the gui stuff as well
#also could maybe just throw everything into one file but it might get docked for poor organization or something

def reset():
    turtle.clearscreen()
    main()

def main():
    features.makeButton(-350, -275, "Reset", reset)

    fractals.Mandelbrot(True, 0, features.randomizeColor())
    #fractals.KochSnowflake(features.randomizeColor(), 3)

if __name__ == '__main__':
    main()