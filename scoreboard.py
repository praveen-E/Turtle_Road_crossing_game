from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 260)
        self.update_score(0)
        self.hideturtle()

    def update_score(self, level):
        self.clear()
        self.write(f"level : {level}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)