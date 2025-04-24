import turtle
import math, random
import additional_features as features

# Global flag to stop process and wait for button press
stop = False

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

    # Writes text if parameter boolean is true. Title of fractal (and formula in this case)
    features.text(textOption, "Mandelbrot Set\nFormula: Z_n+1 = (Z_n)^2 + C")

    iterations = features.variables(20, 15, 500)
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
    #basic idea for koch snowflake - start with equilateral triangle, then draw a koch curve for each part of the triangle and so on
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

    features.text(textOption, "Koch Snowflake")

    t = turtle.Turtle()
    t.color(color)
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()
    
    # (TEMPORARY) Ideally find a place in additional_features or interactive GUI for iterations
    iterations = features.variables(3, 2, 7)
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

def SierpinskiTriangle(textOption = True, color = "black"):
    '''
    Generates an equilateral triangle Sierpinski fractal

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
    turtle.title("Sierpinski Triangle")

    features.text(textOption, "Sierpinski Triangle")

    iterations = features.variables(5, 1, 6)
    if stop or iterations is None:
        return

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
    RemoveInner(t, vert1, vert2, vert3, iterations)

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
        angle = random.uniform(-angle_range, angle_range)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        scale_x = random.uniform(*scale_range)
        scale_y = random.uniform(*scale_range)
        shear = random.uniform(*shear_range)

        a = scale_x * cos_a
        b = -scale_x * sin_a + shear * cos_a
        c = scale_y * sin_a
        d = scale_y * cos_a + shear * sin_a
        e = random.uniform(*trans_range)
        f = random.uniform(*trans_range)
        
        transform.append((a, b, c, d, e, f))
    
    return transform

def RandomFractal(textOption = True, color = "black"):
    '''
    Random fractal generation using IFS (Iterated Function System) and chaos game
    '''
    global stop
    stop = False
    transform = RandomFractalHelper()

    # Setting up canvas
    turtle.tracer(0, 0)
    turtle.setup(800, 600)
    turtle.bgcolor("#FFFFFF")
    turtle.title("Random IFS Fractal")

    features.text(textOption, "Mandelbrot Set\nFormula: Z_n+1 = (Z_n)^2 + C")

    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.speed(0)
    t.color(color)

    if textOption:
        text = "Random IFS Fractal\n(Chaos Game)"
        features.write(txt = text)
        features.setText(text)

    # Set number of iterations (or points) used to create the fractal
    iterations = features.variables(25000, 10000, 100000)
    if stop or iterations is None:
        return

    x, y = random.uniform(-1, 1), random.uniform(-1, 1)

    indices = list(range(len(transform)))

    update_interval = 500

    for i in range(iterations):
        if stop:
            return

        a, b, c, d, e, f = transform[random.choice(indices)]
        x, y = (a * x) + (b * y) + e, (c * x) + (d * y) + f

        t.goto(x, y)
        t.dot(1)

        if i % update_interval == 0:
            turtle.update()
    turtle.update()