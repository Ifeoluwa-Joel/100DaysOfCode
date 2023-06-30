from turtle import Turtle

FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=270)
        self.write(f"Level: {self.level}", align='left', font=FONT)


    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        if self.level == 1:
            self.write(f"GAME OVER!\nYou completed 0 levels\nThink about your life", align='center', font=("Poppins", 20, "bold"))

        elif self.level == 2:
            self.write(f"GAME OVER!\nYou completed {self.level - 1} level\nYou suck", align='center', font=("Poppins", 20, "bold"))

        elif self.level == 3:
            self.write(f"GAME OVER!\nYou completed {self.level - 1} levels\nStop disgracing your ancestors", align='center', font=("Poppins", 20, "bold"))

        elif self.level == 4:
            self.write(f"GAME OVER!\nYou completed {self.level - 1} levels\nYou can do better", align='center', font=("Poppins", 20, "bold"))

        elif self.level == 5:
            self.write(f"GAME OVER!\nYou completed {self.level - 1} levels\nYou deserve some accolades", align='center', font=("Poppins", 20, "bold"))

        elif self.level == 6:
            self.write(f"GAME OVER!\nYou completed {self.level - 1} levels\nNa your papa born you", align='center', font=("Poppins", 20, "bold"))

        elif self.level == 7:
            self.write(f"GAME OVER!\nYou completed {self.level - 1} levels\nYou need to relass and be taken kiaruf", align='center', font=("Poppins", 20, "bold"))

        else:
            self.write(f"GAME OVER!\nYou completed {self.level} levels\nYou mastered this game", align='center', font=("Poppins", 20, "bold"))