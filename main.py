import fractals #not sure if this is how you import the code from the other files
import additional_features
#main file for running the program, could use this to contain the gui stuff as well
#also could maybe just throw everything into one file but it might get docked for poor organization or something

def main():
    fractals.Mandelbrot(True, 0, "#2848ac")

if __name__ == '__main__':
    main()