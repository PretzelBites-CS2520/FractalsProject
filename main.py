import fractals
import additional_features as features
#main file for running the program, could use this to contain the gui stuff as well
#also could maybe just throw everything into one file but it might get docked for poor organization or something

def main():
    #fractals.Mandelbrot(True, 0, features.randomizeColor())
    fractals.KochSnowflake(features.randomizeColor())

if __name__ == '__main__':
    main()