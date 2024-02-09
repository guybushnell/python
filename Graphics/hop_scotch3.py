# Hit the flipped cells to un-flip them, as quick as you can!
# Step 3 - Detect hits by waiting for mouse-clicks in the right spot

import pygame
import random
import time

from hop_scotch1 import wait_for_user, draw_title, create_grid, draw_grid
from hop_scotch2 import flip_some_cells
        
        
def detect_hit(grid_map: list, point: tuple[int, int]) -> list:
    """
    Find the cell containing the point. If it's flipped, return the cell, otherwise return None.
    @returns the cell or None
    """
    for row in grid_map:
        for cell in row:
            # use the built-in method in Rect for testing a point (cell[0] is a pygame.Rect)
            if cell[0].collidepoint(point) and cell[1]:
                return cell
            
    return None

            
# ==== Start Here ====
if __name__ == "__main__":

    # initialise pygame and set-up the gaming window
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("HopScotch3 - Hit the flipped cells!")

    # Initialise sounds and load some ready to play
    pygame.mixer.init()
    hit_sound = pygame.mixer.Sound("audio/hit.mp3")
    miss_sound = pygame.mixer.Sound("audio/miss.wav")
    complete_sound = pygame.mixer.Sound("audio/complete.wav")

    # create the grid of rectangles - we'll use these to draw and test for hits!
    rect_grid = create_grid(screen=screen, nof_cols=5, nof_rows=5)
    
    total_flipped = 3
    flip_some_cells(rect_grid, total_flipped)
    draw_grid(screen, rect_grid)

    draw_title(screen=screen, text="Hit The Lit Cells!", colour=pygame.Color("white"))
    time.sleep(2)

    # loop until all the flipped cells have been un-flipped
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
                    hit_sound.play()
                else:
                    miss_sound.play()
                    
            elif event.type==pygame.QUIT: 
                exit()
        
        time.sleep(0.1)

    complete_sound.play()
    draw_title(screen=screen, text="Well Done!", colour=pygame.Color("white"))
    wait_for_user()