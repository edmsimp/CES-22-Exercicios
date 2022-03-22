"""
2) Change the traffic light program so that changes occur automatically, driven
by a timer.
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
    """
    The state machine change the color automatically with a timer
    """
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

    # Timer itself
    wn.ontimer(advance_state_machine, 1500)

# Initiate the timer
wn.ontimer(advance_state_machine, 1500)

wn.listen() # Listen for events
wn.mainloop()