from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER'
                   f'\n'
                   f'Final score: {self.level}', align='center', font=FONT)
