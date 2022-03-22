"""
1) Add some new key bindings to the first sample program:
Pressing keys R, G or B should change tess' color to Red, Green or Blue.
Pressing keys + or - should increase or decrease the width of tess' pen.
Ensure that the pen size stays between 1 and 20 (inclusive).
Handle some other keys to change some attributes of tess, or attributes of the
window, or to give her new behaviour that can be controlled from the keyboard.
"""
import turtle
# Initializing the traffic light and the window
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("tl becomes a traffic light!")
wn.bgcolor("lightgreen")
tl = turtle.Turtle()

def draw_housing():
    """
    Draw a nice housing to hold the traffic lights.
    """
    tl.pensize(3)
    tl.color("black", "darkgrey")
    tl.begin_fill()
    tl.forward(80)
    tl.left(90)
    tl.forward(200)
    tl.circle(40, 180)
    tl.forward(200)
    tl.left(90)
    tl.end_fill()

draw_housing()

# Position tl onto the place where the green light should be
tl.penup()
tl.forward(40)
tl.left(90)
tl.forward(50)

# Turn tl into a big green circle
tl.shape("circle")
tl.shapesize(3)
tl.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tl' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tl.forward(70)
        tl.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tl.forward(70)
        tl.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tl.back(140)
        tl.fillcolor("green")
        state_num = 0

# First part of the question
def change_color_blue():
    """
    Pressing key B should change tl color to blue.
    """
    tl.fillcolor("blue")
    
def change_color_red():
    """
    Pressing key R should change tl color to red.
    """
    tl.fillcolor("red")  

def change_color_green():
    """
    Pressing key G should change tl color to green.
    """
    tl.fillcolor("green")

# Second part of the question
def increase_pen():
    """
    Pressing key + should increase tl pen size.
    """
    if tl.pensize() <= 19:
        tl.pensize(tl.pensize() + 1)

def reduce_pen():
    """
    Pressing key - should reduce tl pen size.
    """
    if tl.pensize() >= 2:
        tl.pensize(tl.pensize() - 1)

# Third part of the question, adding some functions to change the pen's color
def pen_color_purple():
    """
    Pressing key p should reduce tl pen color.
    """
    tl.pencolor("purple")

def pen_color_white():
    """
    Pressing key w should reduce tl pen color.
    """
    tl.pencolor("white")

def pen_color_yellow():
    """
    Pressing key y should reduce tl pen color.
    """
    tl.pencolor("yellow")

# Bind the event handler to the space key
wn.onkey(advance_state_machine, "space")

# Bind the event handler to the B key
wn.onkey(change_color_blue, "b")

# Bind the event handler to the R key
wn.onkey(change_color_red, "r")

# Bind the event handler to the G key
wn.onkey(change_color_green, "g")

# Bind the event handler to the plus key
# OBS: in case there are "=" and "+" in the same key on your keyboard, please
#   use "shift" + "+" for this to work
wn.onkey(increase_pen, "plus")

# Bind the event handler to the minus key
wn.onkey(reduce_pen, "minus")

# Bind the event handler to the P key
wn.onkey(pen_color_purple, "p")

# Bind the event handler to the P key
wn.onkey(pen_color_white, "w")

# Bind the event handler to the P key
wn.onkey(pen_color_yellow, "y")

wn.listen() # Listen for events
wn.mainloop()