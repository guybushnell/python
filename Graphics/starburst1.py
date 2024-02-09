# draw a simple fan or star-burst
import pygame
import math
import sys
import time

screen = pygame.display.set_mode((500, 500))


def process_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            exit()
            
            
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
    

def draw_line(x, y, radius, angle):
    
    # convert angle in degrees to radians
    radians = math.radians(angle)
    
    end_x = x + math.sin(radians)*radius
    end_y = y + math.cos(radians)*radius
    
    # draw line from x,y -> end_x,end_y
    pygame.draw.line(surface=screen, color=pygame.Color("yellow"), 
                    start_pos=(x, y), end_pos=(end_x, end_y),
                    width=1)
    
    pygame.display.update()
    
    # only needed for starburst2.py
    return (end_x, end_y)


def simple_starburst():
    # Draw simple fan or starburst
    for angle in range(0, 360, 5): 
        process_events()
        draw_line(screen.get_width() / 2, screen.get_height()/2, 200, angle)
        time.sleep(0.05)


def reducing_starburst():
    # Starburst with reducing radius
    angle = 0
    radius = 200

    while radius >= 50:
        process_events()
                
        draw_line(screen.get_width() / 2, screen.get_height()/2, radius, angle)
        
        angle = angle + 17
        radius = radius - 1
        
        time.sleep(0.05)

    
# ==== Start Here
if __name__ == "__main__":
    pygame.display.set_caption("Simple Starburst")
    simple_starburst()
    wait_for_user()

    screen.fill(0)

    pygame.display.set_caption("Reducing Starburst")
    reducing_starburst()    
    wait_for_user()