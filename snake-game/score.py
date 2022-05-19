from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score_board()

    def score_board(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    def calculate_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
