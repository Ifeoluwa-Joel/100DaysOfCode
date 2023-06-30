from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(position)
        self.write(self.score, font=('Consolas', 60, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()

    def update_score(self):
        self.increase_score()
        self.write(self.score, font=('Consolas', 60, 'bold'))


