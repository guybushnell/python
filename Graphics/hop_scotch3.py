# Hit the flipped cells to un-flip them, as quick as you can!
# Step 3 - Detect hits by waiting for mouse-clicks in the right spot

import pygame
import random
import time

from hop_scotch1 import wait_for_user, draw_title, create_grid, draw_grid
from hop_scotch2 import flip_some_cells
        
def detect_hit(grid_map: list, point: (int, int)) -> list:
    """
    Find the cell containing the point. If it's lit, return the cell, otherwise return None.
    @returns (i,j) - cell coordinates or None
    """
    for y, row in enumerate(grid_map):
        for x, cell in enumerate(row):
            if cell[0].collidepoint(point) and cell[1]:
                return cell
            
    return None

            
# ==== Start Here ====
if __name__ == "__main__":

    # initialise pygame and set-up the gaming window
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("HopScotch3 - Hit the flipped cells!")

    # create the grid of rectangles - we'll use these to draw and test for hits!
    rect_grid = create_grid(screen=screen, nof_cols=5, nof_rows=5)
    
    total_flipped = 3
    
    flip_some_cells(rect_grid, total_flipped)
    draw_grid(screen, rect_grid)

    # now look for mouse presses
    while total_flipped > 0:        
        for event in pygame.event.get():
                
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                # was a flipped cell hit?
                x,y = pygame.mouse.get_pos()
                cell = detect_hit(grid_map=rect_grid, point=(x, y))
                
                if cell is not None:
                    # Yes. Unflip it and redraw
                    cell[1] = False
                    draw_grid(screen, rect_grid)
                    total_flipped = total_flipped - 1
                    
            elif event.type==pygame.QUIT: 
                exit()
        
        time.sleep(0.1)

    draw_title(screen=screen, text="Well Done!", colour=pygame.Color("white"))
    wait_for_user()