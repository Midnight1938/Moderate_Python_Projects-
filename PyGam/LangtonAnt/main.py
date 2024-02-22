import pygame as pg
from collections import deque
from random import choice, randrange

"""
? We see that ants, from a (1,0) point
?   move (1,0)(0,1)(-1,0)(0,-1) clockwise, and reverse order in anticlockwise on the grid.
"""

class Ant:
    def __init__(self, app, pos, colour):
        self.app = app
        self.color = colour
        self.x, self.y = pos
        self.increment = deque([(1,0), (0,1), (-1,0), (0,-1)]) # deque is a list with fast appends and pops on either end
    
    def run(self): # ants rules
        value = self.app.grid[self.y][self.x]
        self.app.grid[self.y][self.x] = not value
        
        SIZE = self.app.CELL_SIZE
        
        # #* Coloured Circle Trail
        center = self.x * SIZE, self.y * SIZE
        if value:
            pg.draw.circle(self.app.screen, self.color, center, SIZE/2)
        
        #* White rectangle Trail
        # rect = self.x * SIZE, self.y * SIZE, SIZE -1, SIZE -1 # A rect to draw the ant
        # if value:
        #    pg.draw.rect(self.app.screen, pg.Color('white'), rect)
        # else:
        #    pg.draw.rect(self.app.screen, self.color, rect)
        
        
        self.increment.rotate(1) if value else self.increment.rotate(-1) # rotate deque by 1. ie next element
        dx, dy = self.increment[0] # get the next element
        self.x = (self.x + dx) % self.app.COLS # move the ant
        self.y = (self.y + dy) % self.app.ROWS # back into the grid boundaries
        

class App:
    def __init__(self, WIDTH=1920, HEIGHT=1080, CELL_SIZE=8):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        
        self.CELL_SIZE = CELL_SIZE
        self.ROWS, self.COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE # number of rows and columns
        self.grid = [[0 for col in range(self.COLS)] for row in range(self.ROWS)] # set all grid values to 0

        #* Colour Grouped
        # colors1 = [(50, 30, i) for i in range(256)] # GBA Blue style 
        colors2 = [(150, i, 120) for i in range(256)] # GBA Green Maroon style
        # ants1 = [Ant(self, [self.COLS // 3, self.ROWS // 2],
        #              choice(colors1)) for i in range(40)]
        # ants2 = [Ant(self, [self.COLS - self.COLS // 3, self.ROWS // 2],
        #              choice(colors2)) for i in range(40)]
        # self.ants = ants1 + ants2 # Group to display
        
        # self.ants = [Ant(self, [randrange(self.COLS), randrange(self.ROWS)], self.get_colour()) for i in range(500)] # Random Bunch
        self.ants = [Ant(self, [randrange(self.COLS), randrange(self.ROWS)], choice(colors2)) for i in range(500)] # Random Bunch
        self.ant = Ant(app=self, pos=[self.COLS // 2, self.ROWS // 2], colour=pg.Color('orange')) # initialize the ant, in orange colour
        
        
    @staticmethod
    def get_colour():
        channel = lambda: randrange(30, 220)
        return channel(), channel(), channel()
        
    def run(self):
        while True:
            [ant.run() for ant in self.ants]
#            self.ant.run() # run the ant around
            
            [exit() for eve in pg.event.get() if eve.type == pg.QUIT]
            pg.display.flip() # update the display
            self.clock.tick(60) # FPS
            # Show FPS
            fps = self.clock.get_fps()
            pg.display.set_caption(f"Langton's Ants | FPS: {int(fps)}")


if __name__ == "__main__":
    app = App()
    app.run()
