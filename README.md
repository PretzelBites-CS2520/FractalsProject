# FractalsProject
Turtle Drawing Fractals Project for CS2520
***
### Roadmap
- Generate different types of fractals using turtle
  - <ins>examples</ins>: ~~Mandelbrot set, Koch Snowflake,~~ Sierpinski Triangle, Tree fractal, ...
  - could also add this snowflake fractal found on stackOverflow (link: https://stackoverflow.com/questions/32303391/drawing-a-snowflake-using-recursion)
  - <ins>optional</ins>: Randomly generated fractals (look into Chaos Game?)
- User customization
  - GUI for user to select the type of fractal
    - maybe through a separate "page" (optionally with images of fractals)
  - ~~Color~~, size, scale, ~~(?)background, # of iterations~~
- messages / text
- maybe: change invert button to user keyboard input (if not possible, remove this)
***
### Known Issues
- ~~Invert button multiple times makes fractal generation noticeably slower for Mandelbrot (may not be fixable? given nature of generating)~~ Likely not fixable for now
- ~~May be difficult to make interactive GUI with just Turtle. Look into Tkinter~~
- Turn off invert button for random fractal (will impact performance too much)