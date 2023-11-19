from turtle import Turtle,Screen
from table import Table
from tile import Tile
import time
def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("TIC-TAC-TOE")
    screen.tracer(0)
    
    
    table = Table()
    tile = Tile()

    screen.listen()

    screen.onkey(tile.highlight_row_1, "a")
    screen.onkey(tile.highlight_row_2, "b")
    screen.onkey(tile.highlight_row_3, "c")

    screen.onkey(tile.col_1, "1")
    screen.onkey(tile.col_2, "2")
    screen.onkey(tile.col_3, "3")
    

    game_over = False
    while not game_over:

        screen.update()
        time.sleep(0.001)

        # check situations

    screen.exitonclick()

main()