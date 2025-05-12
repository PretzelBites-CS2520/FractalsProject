import turtle
import math, random
import additional_features as features
import config

def MandelbrotHelper(z, c, n = 20):
    '''
    Recursive function to create Mandelbrot set

    Formula: Z_n+1 = (Z_n)^2 + C

    Parameters:
    z: complex number used in the formula
    c: complex number used in the formula
    n (int): number of times the recursive function occurs (higher -> more accurate)
    '''
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return MandelbrotHelper(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

def Mandelbrot(textOption = True, color = "black"):
    '''
    Creates a Mandelbrot set fractal

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    spd (int): An integer from 1-10 (or 0) for the drawing speed of the turtle
    color (string): Changes the color of the lines in the fractal
    '''
    config.stop = False

    # Setup of the canvas
    turtle.tracer(0, 0)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Mandelbrot Set")
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()

    # Writes text if parameter boolean is true. Title of fractal (and formula in this case)
    features.text(textOption, "Mandelbrot Set\nFormula: Z_n+1 = (Z_n)^2 + C")

    # Uses helper function and draws the fractal
    for x1 in range(-400, 300, 2):
        if config.stop:
            return
        for y1 in range(-400, 300, 2):
            if config.stop:
                return
            x2, y2 = x1 * 0.005, y1 * 0.005
            m  = MandelbrotHelper(0, 1j * y2 + x2, config.user_input['iterations'])
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

def KochSnowflake(textOption = True, color = "black"):
    '''
    Creates a Koch Snowflake fractal

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    color (string): Changes the color of the lines in the fractal
    '''
    config.stop = False

    # Setup of the canvas
    turtle.tracer(0, 50)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Koch Snowflake")

    features.text(textOption, "Koch Snowflake")

    t = turtle.Turtle()
    t.color(color)
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()

    for _ in range(3):
        if config.stop:
            return
        KochCurve(t, 300, config.user_input['iterations'])
        t.right(120)

    t.goto(-150, 100)
    t.setheading(0)

    t.hideturtle()
    turtle.update()

def SierpinskiTriangle(textOption = True, color = "black"):
    '''
    Generates an equilateral triangle Sierpinski fractal

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    color (string): Changes the color of the lines in the fractal
    '''
    config.stop = False
    
    # Setup of the canvas
    turtle.tracer(0, 50)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Sierpinski Triangle")

    features.text(textOption, "Sierpinski Triangle")

    #creating initial triangle
    t = turtle.Turtle()
    t.color(color)
    t.fillcolor(color)
    t.speed(0)
    t.penup()
    t.setheading(0)
    t.goto(250, -250) #trying to start at the bottom left point of the triangle
    vert1 = t.pos() #storing initial vertex
    t.pendown()
    t.begin_fill()
    t.left(120)
    t.forward(500)
    vert2 = t.pos()
    t.left(120)
    t.forward(500)
    vert3 = t.pos()
    t.left(120)
    t.forward(500)
    t.end_fill()

    #now starting the recursive process for removing the inner parts of the triangle
    RemoveInner(t, vert1, vert2, vert3, config.user_input['iterations'])

def RemoveInner(turtle, p1, p2, p3, n):
    '''
    Recursive function that removes the Inner part of a triangle for Sierpinski Fractal

    Parameters:
    turtle - turtle drawing operator
    p1, p2, p3 (tuple): the x and y coordinates of the vertices of the triangle
    n (int) - number of times iterating
    '''
    turtle.color("white") #can change to different colors, just doing white for now
    turtle.fillcolor("white")
    #have to calculate the midpoints of each vertex on the triangle to draw the "removed" triangle
    m1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    m2 = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)
    m3 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
    turtle.penup()
    turtle.goto(m1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(m2)
    turtle.goto(m3)
    turtle.goto(m1)
    turtle.end_fill()

    if n == 0:
        turtle.penup() #do nothing to end the process
    else:
        RemoveInner(turtle, p1, m1, m2, n - 1) #have to run three times since three triangles are created
        RemoveInner(turtle, m1, p2, m3, n - 1)
        RemoveInner(turtle, m2, m3, p3, n - 1)

def RandomFractalHelper():
    '''
    Helper method for RandomFractal to generate transformation matrix
    '''
    num_transform = random.randint(3, 5)
    transform = []

    # Set the canvas ranges of the fractal
    angle_range = math.pi
    scale_range = (0.2, 0.7)
    shear_range = (-0.3, 0.3)
    trans_range = (-200, 150)

    # Creates a transformation matrix to be used when creating points
    for _ in range(num_transform):
        # Creates random angles for the points / shapes
        angle = random.uniform(-angle_range, angle_range)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        # Randomizes scale of the shapes
        scale_x = random.uniform(*scale_range)
        scale_y = random.uniform(*scale_range)
        shear = random.uniform(*shear_range)

        a = scale_x * cos_a
        b = -scale_x * sin_a + shear * cos_a
        c = scale_y * sin_a
        d = scale_y * cos_a + shear * sin_a
        e = random.uniform(*trans_range)
        f = random.uniform(*trans_range)
        
        # Adds all parameters to the return value
        transform.append((a, b, c, d, e, f))
    
    return transform

def RandomFractal(textOption = True, color = "black"):
    '''
    Random fractal generation using IFS (Iterated Function System) and chaos game

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    color (string): Changes the color of the lines in the fractal
    '''
    config.stop = False
    transform = RandomFractalHelper()

    # Setting up canvas
    turtle.tracer(0, 0)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Random IFS Fractal")

    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.color(color)

    if textOption:
        text = "Random IFS Fractal\n(Chaos Game)"
        features.write(txt = text)
        features.set_text(text)

    # Starting values, including how often to update screen
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    indices = list(range(len(transform)))
    update_interval = 500

    for i in range(config.user_input['iterations']):
        if config.stop:
            return

        # Draws dot at the x, y coordinates
        a, b, c, d, e, f = transform[random.choice(indices)]
        x, y = (a * x) + (b * y) + e, (c * x) + (d * y) + f

        t.goto(x, y)
        t.dot(1)

        if i % update_interval == 0:
            turtle.update()
    turtle.update()

def BasicSnowflake(textOption = True, color = "black"):
    """
    Draws a basic fractal pattern that looks like a snowflake

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    color (string): Changes the color of the lines in the fractal
    """
    # Setting up canvas
    turtle.tracer(0, 0)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Basic Snowflake")

    t = turtle.Turtle()
    t.color(color)

    features.text(textOption, "Basic Snowflake")

    drawBasicSnowflake(t, 190, config.user_input['iterations'])

def drawBasicSnowflake(t, length, iterations):
    """
    Function for drawing the basic snowflake
    this code is taken from a stack overflow post showing how to create a simple snowflake
    link: https://stackoverflow.com/questions/32303391/drawing-a-snowflake-using-recursion

    Parameters:
    t - turtle drawing object
    length - the length of the line to be drawn
    iterations - the number of times the iterable will be run
    """
    if iterations > 0:
        for _ in range(6):
            t.forward(length)
            drawBasicSnowflake(t, length // 3, iterations - 1)
            t.backward(length)
            t.left(60)

def TreeFractal(textOption = True, color = "brown", leafColor = "green"):
    """
    Draws a basic fractal pattern that looks like a tree

    Parameters:
    textOption (bool): Decides whether or not to put text in the drawing
    color (string): Changes the color of the base lines in the fractal
    leafColor (string): Changes the color of the edge lines in the fractal
    """
    # Setting up canvas
    turtle.tracer(0, 0)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Tree Fractal")

    t = turtle.Turtle()
    t.color(color)

    #Drawing initial stump
    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()
    t.forward(400)

    drawBranch(t, 400 * 0.9, 20, leafColor, config.user_input["iterations"])

    features.text(textOption, "Tree Fractal")

def drawBranch(t, length, angle, color, iterations):
    """
    Draws a branch of the tree fractal
    """
    if iterations > 0:
        t.color(color)
        t.forward(length)
        t.left(angle)
        drawBranch(t, length * 0.9, angle, color, iterations - 1)
        t.right(angle)
        t.right(angle)
        drawBranch(t, length * 0.9, angle, color, iterations - 1)
        t.left(angle)

