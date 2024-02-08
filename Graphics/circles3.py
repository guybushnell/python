# display random sizes circles randomly
# and then remove them from the screen - so you need to remember where each one is!
import pygame
import random
import time

from circles1 import screen, draw_circle
from circles2 import erase_circle


# Start Here
if __name__ == "__main__":
    pygame.display.set_caption("Circles3")

    # a list of circle coordinates
    circles = []   
        
    while True:
        
        for event in pygame.event.get():
            # check if a user wants to exit the game or not
            if event.type == pygame.QUIT:
                exit()
            
            # has mouse been moved?
            elif event.type == pygame.MOUSEMOTION:
                x,y = pygame.mouse.get_pos()
                r =  30
        
                draw_circle(x, y, r)

                # add this circle to our list so we can rub it out later
                circles.append((x, y, r, time.time()))    

        time.sleep(0.025)
        
        if len(circles) > 0:
            circle = circles[0]
    
            age = time.time() - circle[3]
            if (age > 2):
                erase_circle(circle[0], circle[1], circle[2])
                del circles[0]
