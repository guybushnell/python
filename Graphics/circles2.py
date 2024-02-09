# display random sizes circles randomly
# and then remove them from the screen - so you need to remember where each one is!
import pygame
import random
import time

from circles1 import screen, process_events, draw_circle


def erase_circle(posx, posy, radius):
    fill_col = pygame.Color("black")
    
    # filled part
    pygame.draw.circle(surface=screen, color=fill_col, center=[posx, posy], radius=radius)
    pygame.display.update()


# ==== Start Here ====
if __name__ == "__main__":
    # a list of circle coordinates and radius
    circles = []

    pygame.display.set_caption("Circles2")
        
    while True:
        process_events()
                
        x = random.random() * screen.get_width()
        y = random.random() * screen.get_height()
        r = random.random() * 25 + 10
        
        # add this circle to our list so we can rub it out later
        circles.append((x, y, r))
        
        draw_circle(x, y, r)
        time.sleep(0.125)
        
        if len(circles) > 10:
            circle = circles[0]
            erase_circle(circle[0], circle[1], circle[2])
            del circles[0]
    
