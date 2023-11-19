from turtle import Turtle

class WinnerBoard(Turtle):
    def __init__(self,winner):
        super().__init__()

        self.hideturtle()
        self.pu()

        if winner != "DRAW":
            text = f"PLAYER {winner} HAS WON THE GAME\nCONGRATULATIONS MY PAL"
        else:
            text = "FRIENDSHIP HAS WON THE GAME\nHOOORRRAYY!!!"

        self.write(text, align="center", font=("Courier", 12, "bold"))