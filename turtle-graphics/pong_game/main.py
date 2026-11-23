from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True


def quit_game():
    global game_is_on
    game_is_on = False


screen.onkey(quit_game, "Escape")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddles.
    if (
        ball.distance(right_paddle) < 50
        and ball.x_move > 0
        and ball.xcor() > 340
    ) or (
        ball.distance(left_paddle) < 50
        and ball.x_move < 0
        and ball.xcor() < -340
    ):
        ball.bounce_x()

    # Detect when the right paddle misses.
    if ball.xcor() > 390:
        ball.reset_pos()
        scoreboard.l_point()

    # Detect when the left paddle misses.
    if ball.xcor() < -390:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
