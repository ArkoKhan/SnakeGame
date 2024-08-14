from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
