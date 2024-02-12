# paint circles at the current mouse position and then 
# remove them one by one if they have been on-screen for more than 2 seconds.
import pygame
import random
import time

from dataclasses import dataclass

from circles1 import screen, draw_circle
from circles2 import erase_circle


@dataclass
class Circle:
    """ Describes a circle with centre (x,y), radius r
        time marks when the circle was drawn.
    """
    x: float
    y: float
    r: float
    time: float
    
    
# ==== Start Here ====
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
                circles.append(Circle(x, y, r, time.time()))    

        time.sleep(0.025)
        
        if len(circles) > 0:
            circle = circles[0]
    
            age = time.time() - circle.time
            if (age > 2):
                erase_circle(circle.x, circle.y, circle.r)
                del circles[0]
