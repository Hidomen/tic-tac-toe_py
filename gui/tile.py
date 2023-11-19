from turtle import Turtle

class Tile(Turtle):
    def __init__(self):
        super().__init__()
        self.tiles = []
        

        positions = [(-200,200), (0,200), (200,200), (-200,0), (0,0), (200,0), (-200,-200), (0,-200), (200,-200)]
        # t = 200
        for pos in positions:
            self.create_tile(pos)


    def create_tile(self,position):
        new_tile = Turtle("square")

        new_tile.pu()
        new_tile.color("white")
        new_tile.goto(position)
        # new_tile.team() = "none"

        self.tiles.append(new_tile)


    def highlight_row(self,count):
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

    
    def highlight_row_1(self):
        self.highlight_row(1)

    
    def highlight_row_2(self):
        self.highlight_row(2)


    def highlight_row_3(self):
        self.highlight_row(3)


    def col_1(self):
        for i in [0,3,6]:
            if self.return_color(self.tiles[i])[0] == "yellow":
                print(i)
    
    def col_2(self):
        
        for i in [1,4,7]:
            if self.return_color(self.tiles[i])[0] == "yellow":    
                print(i)

    
    def col_3(self):
        
        for i in [2,5,8]:
            if self.return_color(self.tiles[i])[0] == "yellow":
                print(i)


    def return_color(self,tile):
        return tile.color()