from turtle import Turtle
from pathlib import Path

ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

HIGH_SCORE_FILE = Path(__file__).with_name("high_score.txt")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = self.load_high_score()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.message = Turtle()
        self.message.hideturtle()
        self.message.penup()
        self.message.color("white")

        self.update_scoreboard()

    def load_high_score(self):
        try:
            return int(HIGH_SCORE_FILE.read_text().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        HIGH_SCORE_FILE.write_text(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(
            f"Score: {self.score}    High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def increase_score(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.update_scoreboard()

    def game_over(self):
        self.message.goto(0, 0)
        self.message.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=("Arial", 24, "bold")
        )

    def reset_score(self):
        self.score = 0
        self.message.clear()
        self.update_scoreboard()
