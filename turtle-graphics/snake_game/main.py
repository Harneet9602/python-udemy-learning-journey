
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard


class SnakeGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        self.game_is_on = True
        self.is_paused = False

        self.create_pause_label()
        self.setup_controls()

        self.game_loop()
        self.screen.mainloop()

    def create_pause_label(self):
        self.pause_label = Turtle()
        self.pause_label.hideturtle()
        self.pause_label.penup()
        self.pause_label.color("white")
        self.pause_label.goto(-250, 260)
        self.update_pause_label()

    def update_pause_label(self):
        self.pause_label.clear()

        label = "RESUME" if self.is_paused else "PAUSE"

        self.pause_label.write(
            label,
            align="center",
            font=("Arial", 12, "bold")
        )

    def setup_controls(self):
        self.screen.listen()

        self.screen.onkeypress(self.snake.up, "Up")
        self.screen.onkeypress(self.snake.down, "Down")
        self.screen.onkeypress(self.snake.left, "Left")
        self.screen.onkeypress(self.snake.right, "Right")

        self.screen.onclick(self.handle_screen_click)

    def handle_screen_click(self, x, y):
        if not self.game_is_on:
            self.restart_game()
            return

        if -290 <= x <= -210 and 245 <= y <= 280:
            self.toggle_pause()

        self.screen.listen()

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        self.update_pause_label()

    def game_loop(self):
        if self.game_is_on and not self.is_paused:
            self.snake.move()

            if self.snake.head.distance(self.food) < 15:
                self.food.refresh(self.snake.positions())
                self.snake.extend()
                self.scoreboard.increase_score()

            if (
                self.snake.head.xcor() > 280
                or self.snake.head.xcor() < -280
                or self.snake.head.ycor() > 280
                or self.snake.head.ycor() < -280
            ):
                self.end_game()

            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.end_game()
                    break

        self.screen.update()
        self.screen.ontimer(self.game_loop, 100)

    def end_game(self):
        if self.game_is_on:
            self.game_is_on = False
            self.scoreboard.game_over()

    def restart_game(self):
        answer = self.screen.textinput(
            "Game Over",
            "Would you like to play again? (yes/no)"
        )

        if answer and answer.strip().lower() in ("yes", "y"):
            self.snake.reset()
            self.food.refresh(self.snake.positions())
            self.scoreboard.reset_score()

            self.game_is_on = True
            self.is_paused = False
            self.update_pause_label()
            self.screen.listen()
        else:
            self.screen.bye()


game = SnakeGame()
