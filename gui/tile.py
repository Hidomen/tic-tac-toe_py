from turtle import Turtle


X_SYMBOL = "turtle"
O_SYMBOL = "circle"

POSITIONS = [(-200,200), (0,200), (200,200), (-200,0), (0,0), (200,0), (-200,-200), (0,-200), (200,-200)]


class Tile(Turtle):
    def __init__(self):
        super().__init__()
        self.tiles = []

        self.turn = "X"
        self.unturn = "O" 

        # t = 200
        for pos in POSITIONS:
            self.create_tile(pos)


    def create_tile(self,position):
        """creates tile in the beginning of the game"""
        new_tile = Turtle("square")

        new_tile.pu()
        new_tile.color("white")
        new_tile.goto(position)

        self.tiles.append(new_tile)


    def highlight_row(self,count):
        """highlights the row that given"""
        for tile in self.tiles:
            tile.color("white")

        if count == 1:
            line = 0
        elif count == 2:
            line = 3
        elif count == 3:
            line = 6

        self.tiles[line].color("yellow")
        self.tiles[line + 1].color("yellow")
        self.tiles[line + 2].color("yellow")

# get rid of copy-paste here too
    def highlight_row_1(self):
        """uses highlight_row function to highlight the row #1"""
        self.highlight_row(1)

    
    def highlight_row_2(self):
        """uses highlight_row function to highlight the row #2"""
        self.highlight_row(2)


    def highlight_row_3(self):
        """uses highlight_row function to highlight the row #3"""
        self.highlight_row(3)

# get rid of copy-paste thing
    def col_1(self):
        """checks for highlighted row and if there is any and intersection tile of column #1 and highlighted row is not given to any player changes to it"""
        for i in [0,3,6]:
            if self.return_color(self.tiles[i]) == "yellow":
                if self.tiles[i].shape() == "square":
                    self.change_tile(i)
    

    def col_2(self):
        """checks for highlighted row and if there is any and intersection tile of column #2 and highlighted row is not given to any player changes to it"""
        for i in [1,4,7]:
            if self.return_color(self.tiles[i]) == "yellow":    
                if self.tiles[i].shape() == "square":
                    self.change_tile(i)

    
    def col_3(self):
        """checks for highlighted row and if there is any and intersection tile of column #3 and highlighted row is not given to any player changes to it"""
        for i in [2,5,8]:
            if self.return_color(self.tiles[i]) == "yellow":
                if self.tiles[i].shape() == "square":
                    self.change_tile(i)
#

    def return_color(self,tile):
        """returns tile's color"""
        return tile.color()[0]
    

    def change_tile(self,index):
        """changes tile's shape based on x or o's symbol and turns over"""
        if self.turn == "X":
            self.tiles[index].shape(X_SYMBOL)

            # if self.is_any_left or self.check_win == False: !!!!!!!# should be turn over only if game is not over
            self.turn_over()
            # else:
            #     print("game over")

        else:
            self.tiles[index].shape(O_SYMBOL)

            # if self.is_any_left or self.check_win == False: 
            self.turn_over()
            # else:
            #     print("game over")

    def turn_over(self):
        """changes the turn"""
        self.turn, self.unturn = self.unturn, self.turn


    def return_turn(self):
        """returns turn"""
        return self.turn

# check situations
    def is_any_left(self):
        """checks are there any tile left and return True/False"""
        for tile in self.tiles:
            if tile.shape() == "square":
                return True
        return False


    def check_win(self):
            """checks for win situations and returns True/False"""
            # row check
            for i in [0,3,6]:
                if self.tiles[i].shape() == self.tiles[i+1].shape() == self.tiles[i+2].shape() and self.tiles[i].shape() != "square":
                    return True
            # column check
            for i in [0,1,2]:
                if self.tiles[i].shape() == self.tiles[i+3].shape() == self.tiles[i+6].shape() and self.tiles[i].shape() != "square":
                    return True

            # diagonal checks  
            if self.tiles[0].shape() == self.tiles[4].shape() ==  self.tiles[8].shape() and self.tiles[0].shape() != "square":
                return True

            
            if self.tiles[2].shape() == self.tiles[4].shape() == self.tiles[6].shape() and self.tiles[2].shape() != "square":
                return True
            
            return False
    

    def reset(self):
        self.tiles.clear()
        self.__init__()

            
