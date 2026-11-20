from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make your bet',
          prompt='Which turtle will win the race, enter a color(red,pink,purple,blue,green,yellow):'
          )

colors= ['red','blue','green','yellow','purple','pink']
y_positions = [i*40-100 for i in range(6)]
all_turtles=[]

for turtle_index in range(0,6):
      new_turtle = Turtle(shape='turtle')
      new_turtle.color(colors[turtle_index])
      new_turtle.penup()
      new_turtle.goto(x=-240, y= y_positions[turtle_index])
      all_turtles.append(new_turtle)


is_race_on = False
if user_bet:
      is_race_on = True


while is_race_on:

    for t in all_turtles:
        t.speed(0)
        rand_dist=random.randint(0,30)
        t.forward(rand_dist)
        if t.xcor()> 230:
            is_race_on = False
            winning_color = t.pencolor()
            break
if winning_color == user_bet.lower():
    result = f"WINNER IS {winning_color.upper()}!!!\nYOU WON! 🎉"
else:
    result = f"WINNER IS {winning_color.upper()}!!!\nBETTER LUCK NEXT TIME!"

result_turtle = Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 0)
result_turtle.color(winning_color)
result_turtle.write(
    result,
    align="center",
    font=("Calibri", 18, "bold")
)

screen.exitonclick()
