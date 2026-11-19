
import turtle as t
import random


# Create turtle object
tim = t.Turtle()
tim.speed(0)
tim.pensize(2)

# Available colours
colors = ["red", "green", "blue", "purple", "pink", "brown", "yellow"]

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen"
]

directions = [0, 90, 180, 270]
step_size = [i + 10 for i in range(0, 100)]


# Generate random RGB colours
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# CHALLENGE 1: Draw a square
def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


# CHALLENGE 2: Draw a dashed line
def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


# CHALLENGE 2: Draw a dashed square
def draw_dashed_square():
    for _ in range(4):
        draw_dashed_line()
        tim.left(90)


# CHALLENGE 3: Draw shapes from triangle to decagon
def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)


def draw_polygons():
    for shape_side in range(3, 11):
        tim.color(random.choice(colors))
        draw_shape(shape_side)


# CHALLENGE 4: Random walk with named colours
def random_walk(steps):
    tim.pensize(10)

    for _ in range(steps):
        tim.color(random.choice(colours))
        tim.forward(random.choice(step_size))
        tim.setheading(random.choice(directions))


# CHALLENGE 4: Random walk with random RGB colours
def random_walk_rgb(steps):
    tim.pensize(10)

    for _ in range(steps):
        tim.color(random_color())
        tim.forward(random.choice(step_size))
        tim.setheading(random.choice(directions))


# CHALLENGE 5: Create a spirograph
def spirograph(size_of_gap):
    tim.speed(0)

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


# SELECT THE CHALLENGE YOU WANT TO RUN
# Options:
# "square"
# "dashed_line"
# "dashed_square"
# "polygons"
# "random_walk"
# "random_walk_rgb"
# "spirograph"

CHALLENGE = "spirograph"


# Execute selected challenge
if CHALLENGE == "square":
    draw_square()

elif CHALLENGE == "dashed_line":
    draw_dashed_line()

elif CHALLENGE == "dashed_square":
    draw_dashed_square()

elif CHALLENGE == "polygons":
    draw_polygons()

elif CHALLENGE == "random_walk":
    random_walk(1000)

elif CHALLENGE == "random_walk_rgb":
    random_walk_rgb(1000)

elif CHALLENGE == "spirograph":
    spirograph(2)

else:
    print("Invalid challenge selected!")


# Keep the window open
screen = t.Screen()
screen.exitonclick()
