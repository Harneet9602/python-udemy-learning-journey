from turtle import Turtle, Screen
import random


# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)


# Ask the user to place a bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color (red, pink, purple, blue, green, yellow):"
)

# List of turtle colours and their starting positions
colors = ["red", "blue", "green", "yellow", "purple", "pink"]
y_positions = [i * 40 - 100 for i in range(6)]

all_turtles = []


# Create six turtle objects
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])

    all_turtles.append(new_turtle)


# Start the race if the user enters a bet
is_race_on = bool(user_bet)

if is_race_on:

    for turtle in all_turtles:
        turtle.speed(0)

    while is_race_on:

        for turtle in all_turtles:

            # Move each turtle by a random distance
            rand_dist = random.randint(0, 30)
            turtle.forward(rand_dist)

            # Check whether a turtle has crossed the finish line
            if turtle.xcor() > 230:
                is_race_on = False

                winning_color = turtle.pencolor()
                print(f"The winner is {winning_color}")

                # Check whether the user's bet was correct
                if winning_color == user_bet.lower():
                    print("Congratulations! You won your bet.")
                else:
                    print("Better luck next time, you lost this one.")

                break


# Close the window when clicked
screen.exitonclick()
