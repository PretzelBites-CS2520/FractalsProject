import turtle
import math
import additional_features as features

stop = False

def variables(default, min, max):
    '''
    (probably temporary) Method of getting user input for number of iterations

    Parameters:
    default: default value
    min: min value
    max: max value
    '''
    global stop
    screen = turtle.Screen()
    iterations = screen.numinput("Iterations", f"Number of recursive iterations:\n({min} - {max})", default, min, max)
    if iterations is None:
        stop = True
        return None
    return int(iterations)

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
    global stop
    stop = False

    # Setup of the canvas
    turtle.tracer(spd, 50)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Mandelbrot Set")
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()

    # Writes text if parameter boolean is true. Title of fractal and formula
    if textOption:
        text = "Mandelbrot Set\nFormula: Z_n+1 = (Z_n)^2 + C"
        features.write(text)
        features.setText(text)

    iterations = variables(20, 15, 500)
    if stop or iterations is None:
        return

    # Uses helper function and draws the fractal
    for x1 in range(-400, 300, 2):
        if stop:
            return
        for y1 in range(-400, 300, 2):
            if stop:
                return
            x2, y2 = x1 * 0.005, y1 * 0.005
            m  = MandelbrotHelper(0, 1j * y2 + x2, iterations)
            if not math.isnan(m.real):
                # Cursor color
                t.color("#000000")
                # Fractal color
                t.dot(2.4, color)
                t.goto(x1, y1)
        turtle.update()

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

def KochSnowflake(color = "black", iterations = 3):
    '''
    Creates a Koch Snowflake fractal

    Parameters:
    color (string): Changes the color of the lines in the fractal
    iterations (int): number of recursions that the fractal will go through
    '''
    global stop
    stop = False

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
    
    # (TEMPORARY) Ideally find a place in additional_features or interactive GUI for iterations
    iterations = variables(3, 2, 7)
    if stop or iterations is None:
        return

    for _ in range(3):
        if stop:
            return
        KochCurve(t, 300, iterations)
        t.right(120)

    t.goto(-150, 100)
    t.setheading(0)

    t.hideturtle()
    turtle.update()

def SierpinskiTriangle():
    print() #temp