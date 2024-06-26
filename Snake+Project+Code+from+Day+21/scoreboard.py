from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGHSCORE = 0

with open('highscore.txt', mode='r') as file:
    saved_score = file.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(saved_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            HIGHSCORE = self.highscore
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

with open('highscore.txt', mode='w') as file:
    file.write(str(HIGHSCORE))
