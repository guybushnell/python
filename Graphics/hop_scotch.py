# Hit the flipped cells to un-flip them, as quick as you can!

import pygame
import time


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

            row.append(rect)
            
        # add this new row of cells to the list of rows
        grid.append(row)
        
        # move to the next row position
        y = y + cell_height
        
    return grid
    

# Start Here
if __name__ == "__main__":

    # initialise pygame and set-up the gaming window
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Whack-a-circle!")

    # create the coordinate grid of rectangle - we'll use these to draw and test for hits!
    grid_map = create_grid(screen=screen, width=3, height=3)
    
    while True:
        # flip some cells in the grid so the user can try to hit them
        num_flipped = flip_some_cells(screen, grid_map)
        
        # monitor the users input for a set time only, detecting hits
        score = process_events(timeout_secs=2)
        
        if score < num_lit:
            draw_title(screem, "Game Over Man!")
            time.sleep(2)
            break
        else:
            draw_title(screen, "Well Done! Next level!")
            time.sleep(2)