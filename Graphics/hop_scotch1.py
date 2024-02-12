# Hit the flipped cells to un-flip them, as quick as you can!
# Step 1 - Create and draw a grid of shapes ready for hitting

import pygame
import random
import time


def wait_for_user() -> None:
    """
    Wait for a mouse-click or keypress then return.
    If user closes windows, then quite the program.
    """
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN: 
                return
            elif event.type==pygame.MOUSEBUTTONDOWN:
                return
            elif event.type==pygame.QUIT: 
                exit()
                

def draw_title(screen, text: str, colour) -> None:
    '''
    Place the given text in the centre of the screen
    '''
    font = pygame.font.SysFont(None, 36)
    img = font.render(text, True, colour)
    img_size = img.get_size()
    
    centre_x = (screen.get_width() - img.get_width()) / 2
    centre_y = (screen.get_height() - img.get_height()) / 2
    screen.blit(img, (centre_x, centre_y))
    pygame.display.update()
    

def create_grid(screen: pygame.Surface, nof_cols:int, nof_rows:int) -> list:
    """
    Creates a grid of rects that fill the screen.
    For example, a 2x2 grid would be returned as
    [
        [rect1 rect2] 
        [rect3 rect4]
    ] 
    Accessing rect2 would be - grid[0][1]
    
    @returns the grid as a list of lists. 
    """
    
    # work out the width of each cell
    cell_width = screen.get_width() / nof_cols
    cell_height = screen.get_height() / nof_rows
    
    # keep track of the current row position
    y = 0
    grid = []
    
    # foreach row we need to build...
    for row in range(0, nof_rows):
        
        # keep track of current column position
        x = 0
        row = []

        # for each column/cell in that row...
        for column in range(0, nof_cols):
            rect = pygame.Rect((x,y), (cell_width, cell_height))
            
            # move-on ready to make the next one
            x = x + cell_width

            # each cell is a list of [rectangle, status]
            # we will use the status to indicate if the cell is flipped/lit
            row.append([rect, False])
            
        # add this new row of cells to the list of rows
        grid.append(row)
        
        # move to the next row position
        y = y + cell_height
        
    return grid
    
    
def draw_grid(screen: pygame.Surface, grid: list) -> None:
    """
    Draw each rectangle in the grid.
    """
    unlit = pygame.Color("dark blue")
    lit = pygame.Color("light blue")
    background = pygame.Color("black")
    
    # for every row in grid...
    for row in grid:
        
        # for every cell in row...
        for rect, flipped in row:
            
            if flipped:
                pygame.draw.rect(surface=screen, color=lit, rect=rect)
            else:
                pygame.draw.rect(surface=screen, color=unlit, rect=rect)
            
            # draw a border around each to separate them a little bit
            pygame.draw.rect(surface=screen, color=background, rect=rect, width=4)
            
    pygame.display.update()
            
    
# ==== Start Here ====
if __name__ == "__main__":

    # initialise pygame and set-up the gaming window
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("HopScotch1 - Create & Draw")

    # create the grid of rectangles - we'll use these to draw and test for hits!
    rect_grid = create_grid(screen=screen, nof_cols=6, nof_rows=6)
    draw_grid(screen, rect_grid)

    # Now wait until the use closes the window
    wait_for_user()
                
