from turtle import Turtle
from scores import Scores
FONT = ("Courier", 12, "bold")


class WinnerBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.pu()


    def winscreen(self, winner, score_x, score_o):
        if winner != "DRAW":
            text = f"PLAYER {winner} HAS WON THE GAME\nCONGRATULATIONS MY PAL"
        else:
            text = "FRIENDSHIP HAS WON THE GAME"

        # self.write(text, align="center", font=FONT)
        self.write(f"{text}\nX: {score_x}\nO: {score_o}", align="center", font=FONT)

