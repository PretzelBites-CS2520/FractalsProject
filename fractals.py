import turtle
import math
#this file could be used for containing each of the fractal drawings, could maybe make each one have their own file if needed
piX = (2.0 - (-2.0)) / 800
piY = (2.0 - (-1.0)) / 600

def MandelbrotHelper(z, c, n = 20):
    '''
    Recursive function to create Mandelbrot set
    '''
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return MandelbrotHelper(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

# some parameters are currently filler (textOption), implement later
def Mandelbrot(textOption = True, spd = 0, color = "black"):
    '''
    Creates a Mandelbrot set fractal
    
    (temp) Formula: Z(n + 1) = (Z(n))^2 + C

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    spd (int): An integer from 1-10 (or 0) for the drawing speed of the turtle
    color (string): Changes the color of the lines in the fractal
    '''
    turtle.tracer(spd, 50)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Mandelbrot Set")
    t = turtle.Turtle()
    t.penup()
    for x1 in range(-400, 300, 2):
        for y1 in range(-400, 300, 2):
            x2, y2 = x1 * piX, y1 * piY
            m  = MandelbrotHelper(0, x2 + 1j * y2, 20)
            if not math.isnan(m.real):
                # Cursor color
                t.color("#000000")
                # Fractal color
                t.dot(2.4, color)
                t.goto(x1, y1)
        turtle.update()
    # Note, takes a while after finishing before this happens, most likely slow load
    turtle.exitonclick()