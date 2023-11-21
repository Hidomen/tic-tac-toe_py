from turtle import Turtle

TABLE_SIZE = 600

class Lines(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        # self.speed(9)
        self.pensize(3)
        self.color("white")

        x = int(TABLE_SIZE/6)
        y = int(TABLE_SIZE/2)

        for i in range(1,-2,-2):
            self.pu()
            self.goto(i*x,y)
            self.pd()
            self.setheading(270)
            self.forward(TABLE_SIZE)

            self.pu()
            self.goto(y,i*x)
            self.pd()
            self.setheading(180)
            self.forward(TABLE_SIZE)