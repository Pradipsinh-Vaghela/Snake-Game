from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier",15,'normal')
GAME_FONT = ("Courier",25,'normal')

with open("data.txt",) as h_score:
    HIGH_SCORE = int(h_score.read())
    print(type(HIGH_SCORE))

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = HIGH_SCORE
        with open("data.txt", ) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.goto(0, 275)
        self.write(arg=f"Score is : {self.score} High Score : {self.high_score}", move = True, align = ALIGNMENT, font = SCORE_FONT)

    def update_score(self):
        self.score += 1

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                content = str(self.high_score)
                data.write(content)
        self.score = 0