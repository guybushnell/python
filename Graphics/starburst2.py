# draw a simple fan or star-burst
import pygame
import time

from starburst1 import screen, process_events, draw_line, wait_for_user


def recursive_starburst(x, y, radius, depth):
    # Draw a starburst with mini starbursts on the end of each line!
    
    for angle in range(0, 360, 30):                 
        (x2, y2) = draw_line(x, y, radius, angle)
        
        if depth < 2:
            recursive_starburst(x2, y2, radius * 0.35, depth+1)

    pygame.display.update()
    process_events() 
    time.sleep(0.125)
    
    
# ==== Start Here
if __name__ == "__main__":
    pygame.display.set_caption("Recursive Starburst")
    
    recursive_starburst(x=screen.get_width() / 2, y=screen.get_height()/2, radius=160, depth=0)
    
    wait_for_user()