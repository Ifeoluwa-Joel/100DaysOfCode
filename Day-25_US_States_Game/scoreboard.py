from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(300, 250)
        self.score = 0
        self.write(f"{self.score}/50", align='right', font=("Courier", 15, "bold"))

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.increase_score()
        self.write(f"{self.score}/50", align='right', font=("Courier", 15, "bold"))