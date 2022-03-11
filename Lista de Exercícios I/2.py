"""
2) Write a void function draw_poly(t, n, sz) which makes a turtle draw
a regular polygon. When called with draw_poly(tess, 8, 50), it will
draw a shape like this:
"""

def draw_poly(t, n, sz):
    """
    Makes a turtle draw a regular polygon given the number of sides and
    it's size.
    """

    # Drawing loop
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

# Drawing constants
bgcolor = "light green"
pencolor = "pink"
number_of_sides = 8
side_lenght = 50
pen_size = 3 # The pen size was chosen by test, to fit better compared to the
             # given picture

# Importing libraries
import turtle

# Initializing the Screen and Turtle objects
window = turtle.Screen()
window.bgcolor(bgcolor)
pen = turtle.Turtle()
pen.color(pencolor)
pen.pensize(pen_size)

# Drawing the required polygon
draw_poly(pen, number_of_sides, side_lenght)

# Uncomment this last line in case you want to see the drawing instead of
# closing the screen right after it gets done
# window.exitonclick()
