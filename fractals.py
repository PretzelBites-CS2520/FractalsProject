import turtle
import math

def MandelbrotHelper(z, c, n = 20):
    '''
    Recursive function to create Mandelbrot set

    Formula: Z_n+1 = (Z_n)^2 + C

    Parameters:
    z: complex number used in the formula
    c: complex number used in the formula
    n: number of times the recursive function occurs (higher -> more accurate)
    '''
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return MandelbrotHelper(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

def Mandelbrot(textOption = True, spd = 0, color = "black"):
    '''
    Creates a Mandelbrot set fractal

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    spd (int): An integer from 1-10 (or 0) for the drawing speed of the turtle
    color (string): Changes the color of the lines in the fractal
    '''
    # Setup of the canvas
    turtle.tracer(spd, 50)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Mandelbrot Set")
    t = turtle.Turtle()
    t.penup()

    # Writes text if parameter boolean is true. Title of fractal and formula
    if textOption:
        t.setposition(0, 250)
        t.write("Mandelbrot Set\nFormula: Z_n+1 = (Z_n)^2 + C", align = "center", font = ('Arial', 12, 'bold'))
    
    # Uses helper function and draws the fractal
    for x1 in range(-400, 300, 2):
        for y1 in range(-400, 300, 2):
            x2, y2 = x1 * 0.005, y1 * 0.005
            m  = MandelbrotHelper(0, 1j * y2 + x2)
            if not math.isnan(m.real):
                # Cursor color
                t.color("#000000")
                # Fractal color
                t.dot(2.4, color)
                t.goto(x1, y1)
        turtle.update()
    # Note, takes a while after finishing before this happens, most likely slow load
    turtle.exitonclick()

def KochCurve(turtle, l, n = 7):
    '''
    Recursive function for drawing Koch Curves

    Formula: make a koch curve on each of the sides of an equilateral triangle

    Parameters:
    turtle - turtle drawing operator
    l - length of koch curve being drawn
    n - number of times iterating, default is 7
    '''
    #basic idea for koch snowflake - start with equilateral triangle, remove the inner side and draw another equilateral triangle
    #draw a koch curve for each part of the triangle
    #in the recursive function p2 will some distance be above the midpoint of the line 
    if n == 0:
        turtle.forward(l)
    else:
        KochCurve(turtle, l / 3, n - 1)
        turtle.left(60)
        KochCurve(turtle, l / 3, n - 1)
        turtle.right(120)
        KochCurve(turtle, l / 3, n - 1)
        turtle.left(60)
        KochCurve(turtle, l / 3, n - 1)

def KochSnowflake(color = "black"):
    '''
    Creates a Koch Snowflake fractal

    Parameters:
    color (string): Changes the color of the lines in the fractal
    '''
    
    # Setup of the canvas
    turtle.tracer(0, 50)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Koch Snowflake")

    t = turtle.Turtle()
    t.color(color)
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()

    for _ in range(3):
        KochCurve(t, 300, 5)
        t.right(120)

    t.hideturtle()
    turtle.exitonclick()