from turtle import Screen
from table import Table
from tile import Tile
from winnerboard import WinnerBoard

WELCOMER = "Welcome the TIC-TAC-TOE: for start the game type START for learn to rules type RULES "

RULES = """
RULES:
1. The game is played on a grid that's 3x3
2. The game is for 2 players one of the player plays 'X' and the other one plays 'O'
    (in this case turtle represents X, circle represents O)
3. Players take turns putting their marks in empty squares
    (in this version players put their marks firstly with row "a/b/c" and then with their column "1/2/3" )
4. The first player to get 3 of they marks in a row (up,down,across or diagonally) is the winner
5. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie
"""

winner = ""

def main():
    first_time = False

    screen,winnerboard,tile = setup()

    
    if first_time:
        # start screen
        user_input = screen.textinput("WELCOMER", WELCOMER)
        while user_input.upper() not in ["START", "RULES"]:
            user_input = screen.textinput("WELCOMER", WELCOMER)

        if user_input.upper() == "RULES":
            screen.textinput("RULES",RULES)

        # first_time = False
        #     
    

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

        winner = check_game_over(tile)
        if winner != False:
            winnerboard.winscreen(winner) 
            game_over = True

        
        if game_over:
        # end screen
            screen.clear()
            winnerboard.winscreen(winner)

            
    screen.exitonclick()



def setup():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("TIC-TAC-TOE")
    screen.tracer(0)

    table = Table()

    winnerboard = WinnerBoard()

    tile = Tile()



    return screen, winnerboard, tile


def check_game_over(tile):
    if not tile.is_any_left() and not tile.check_win(): # TIE
        return "DRAW"
        
    if tile.check_win():
        if tile.return_turn() == "X": # O WON
            return "O"
        elif tile.return_turn() == "O": # X WON
            return "X"

    return False



#

main()