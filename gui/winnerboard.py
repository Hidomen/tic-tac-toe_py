from turtle import Turtle

FONT = ("Courier", 12, "bold")


class WinnerBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.pu()

        self.score_x = 0
        self.score_o = 0


    def score_up(self,winner):
        if winner == "X":
            self.score_x += 1

        elif winner == "O":
            self.score_o += 1


    def winscreen(self, winner):
        if winner != "DRAW":
            text = f"PLAYER {winner} HAS WON THE GAME\nCONGRATULATIONS MY PAL"
            self.score_up(winner)
        else:
            text = "FRIENDSHIP HAS WON THE GAME"

        self.write(text, align="center", font=FONT)
        # self.write(f"{text}\nX: {self.score_x}\nO: {self.score_o}", align="center", font=FONT)