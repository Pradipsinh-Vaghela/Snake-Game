from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier",15,'normal')
GAME_FONT = ("Courier",25,'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.goto(0, 275)
        self.write(arg=f"Score is : {self.score}", move = True, align = ALIGNMENT, font = SCORE_FONT)
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", move=True, align=ALIGNMENT, font=GAME_FONT)
