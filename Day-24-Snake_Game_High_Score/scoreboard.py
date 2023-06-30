from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"[Score: {self.score}][High Score: {self.high_score}]", align=ALIGNMENT, font=FONT)

    def reset_(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def increase_bonus_score(self):
        self.score += 5
        self.update_scoreboard()
