
import turtle as t
import random
import colorgram


# OPTIONAL: Extract RGB colours from an image
# Uncomment and run this function if you want to
# extract a new colour palette from another image.

def extract_colors(image_path, number_of_colors=30):
    rgb_colors = []
    colors = colorgram.extract(image_path, number_of_colors)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors


# RGB colour palette extracted from the reference image
color_list = [
    (246, 242, 244), (202, 164, 110), (240, 245, 241),
    (236, 239, 243), (149, 75, 50), (222, 201, 136),
    (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86),
    (73, 43, 35), (145, 178, 149), (14, 98, 70),
    (232, 176, 165), (160, 142, 158), (54, 45, 50),
    (101, 75, 77), (183, 205, 171), (36, 60, 74),
    (19, 86, 89), (82, 148, 129), (147, 17, 19),
    (27, 68, 102), (12, 70, 64), (107, 127, 153),
    (176, 192, 208), (168, 99, 102)
]


# Create turtle object
tim = t.Turtle()
tim.speed(0)
tim.hideturtle()

# Set RGB colour mode
t.colormode(255)


# Create a grid of colourful dots
def make_dots(num_rows, num_columns):
    dot_size = 20
    spacing = 50

    start_x = -((num_columns - 1) * spacing) / 2
    start_y = ((num_rows - 1) * spacing) / 2

    tim.penup()

    for row in range(num_rows):
        for column in range(num_columns):
            tim.goto(
                start_x + column * spacing,
                start_y - row * spacing
            )

            tim.dot(dot_size, random.choice(color_list))


# CHALLENGE: Create a Hirst-inspired dot painting
make_dots(10, 10)


# Display the drawing
screen = t.Screen()
screen.exitonclick()
