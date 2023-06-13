from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 10, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!\nScore: 0{self.score}", align="center", font=("Courier", 30 , "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
