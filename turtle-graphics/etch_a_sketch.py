from turtle import Turtle, Screen

# Create turtle and screen objects
tim = Turtle()
screen = Screen()


# Bind keyboard keys to functions
def bind_key(func, key):
    screen.onkey(func, key.lower())
    screen.onkey(func, key.upper())


# Move the turtle forward
def move_forwards():
    tim.forward(20)


# Move the turtle backward
def move_backwards():
    tim.backward(20)


# Turn left and move forward
def counterclockwise():
    tim.lt(10)
    move_forwards()
    tim.tilt(20)


# Turn right and move forward
def clockwise():
    tim.rt(10)
    move_forwards()
    tim.tilt(20)


# Clear the drawing and reset the turtle
def clear_drawing():
    tim.reset()


# Listen for keyboard events
screen.listen()

# Keyboard controls
bind_key(move_forwards, "w")       # W - Forward
bind_key(move_backwards, "s")      # S - Backward
bind_key(counterclockwise, "a")    # A - Left
bind_key(clockwise, "d")           # D - Right
bind_key(clear_drawing, "c")       # C - Clear drawing


# Keep the window open
screen.exitonclick()
