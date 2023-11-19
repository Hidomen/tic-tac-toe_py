# learn pygame to make it with gui



board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def main() :
    # find them better name
    pturn = "X"
    other = "O"
    a = True
    while a == True :
        table(pturn)
        move(pturn)

        # gamecheck
        for i in [ 0, 3, 6 ] :
            if board[i] == board[i + 1] == board[i + 2] != 0 :
                end(pturn)
                a = False
            # horizontal
        for i in [ 0, 1, 2 ] :
            if board[i] == board[i + 3] == board[i + 6] != 0 :
                end(pturn)
                a = False
            # vertical
        if board[0] == board[4] == board[8] != 0 :
            end(pturn)
            a = False
            # diagonal
        if board[2] ==board[4] == board[6] != 0 :
            end(pturn)
            a = False
            # diagonal
        
        # draw
        if 0 not in board :
            table(pturn)
            print("IT'S DRAW")
            break

        # turn switch
        pturn, other = other, pturn
            

def table(pturn) :
    # could be better in this
    print(f"|     |     |     |       #-| PLAYER {pturn}'S TURN |-#")
    for i in range(len(board)) :
        print(f"|  {board[i]}  ", end = "")
        if i == 8 :
            print("|", end= "")
        if i in [2,5] :
            print("|")
            print("|     |     |     |")
            print("|-----|-----|-----|")
            print("|     |     |     |")
    print("\n|     |     |     | ")


def move(pturn) :
    print("to make a move type a number between [1-9]")

    while True :
        try : 
            pmove = int(input("> "))
            if pmove >= 1 and pmove <= 9 :
                if board[pmove - 1] == 0 :
                    # success
                    board[pmove - 1] = pturn
                    # endturn
                    break
                else :
                    print("full")
            else :
                print("[1-9] please")
        except ValueError:
            print("type a number please")


def end(pturn) :
    table(pturn)
    print(f"{pturn} WON")


main()