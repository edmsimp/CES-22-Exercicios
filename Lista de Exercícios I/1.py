"""
1 ) Write a program to draw this. Assume the innermost square is 20 units
per side, and each successive square is 20 units bigger, per side, than
the one inside it.
"""

# Drawing constants
bgcolor = "light green"
pencolor = "pink"
number_of_squares = 5
first_side_lenght = 20
growing_rate = 20
square_angle = 90
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

# Drawing loop
for i in range(number_of_squares):
    # Updating the square side size
    side_lenght = first_side_lenght +i*growing_rate
    # Drawing the squares
    pen.pendown() 
    pen.forward(side_lenght)
    pen.left(square_angle)
    pen.forward(side_lenght)
    pen.left(square_angle)
    pen.forward(side_lenght)
    pen.left(square_angle)
    pen.forward(side_lenght)
    pen.left(square_angle)
    # Updating the pen's position
    pen.penup()
    pen.goto(-side_lenght/2, -side_lenght/2) 

# Uncomment this last line in case you want to see the drawing instead of
# closing the screen right after it gets done
# window.exitonclick()
