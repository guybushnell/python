# Hit the flipped cells to un-flip them, as quick as you can!
# Step 2 - Randomly flip a number of cells, ready for hitting

import pygame
import random
import time

from hop_scotch1 import wait_for_user, draw_title, create_grid, draw_grid

    
def flip_some_cells(grid_map: list, flip_count: int) -> None:
    """
    Randomly change the status of a <flip_count> cells to 'flipped'
    Doesn't draw anything, just changes the status.
    """

    # first make sure all the cells are reset (unflipped)
    for row in grid_map:
        for cell in row:
            cell[1] = False
    
    nof_rows = len(grid_map)
    nof_cols = len(grid_map[0])
    
    # now flip some
    for i in range(0, flip_count):
        
        while True:
            row = int(random.random() * nof_rows)
            col = int(random.random() * nof_cols)
            
            cell = grid_map[row][col]

            # if not flipped, then flip it!
            if not cell[1]:
                cell[1] = True
                break
        

# ==== Start Here ====
if __name__ == "__main__":

    # initialise pygame and set-up the gaming window
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("HopScotch2 - Flip cells")

    # create the grid of rectangles - we'll use these to draw and test for hits!
    rect_grid = create_grid(screen=screen, nof_cols=3, nof_rows=3)
    
    # Now wait until the use closes the window
    while True:
        flip_some_cells(rect_grid, 3)
        draw_grid(screen, rect_grid)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                exit()
                
        time.sleep(1)
