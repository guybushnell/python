# display random sizes circles randomly
import pygame
import random
import time


screen = pygame.display.set_mode((500, 500))
    
    
def draw_circle(posx, posy, radius):
    fill_col = pygame.Color("light blue")
    line_col = pygame.Color("black")
    
    # filled part
    pygame.draw.circle(surface=screen, color=fill_col, center=[posx, posy], radius=radius)
    # outline
    pygame.draw.circle(surface=screen, color=line_col, center=[posx, posy], radius=radius, width=1)
    
    pygame.display.update()


def process_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            exit()
            
            
# ==== Start Here ====
if __name__ == "__main__":
    pygame.display.set_caption("Circles1")

    # Main loop - goes forever
    while True:
        
        # Quit if the user closes the main window
        process_events()
                
        x = random.random() * screen.get_width()
        y = random.random() * screen.get_height()
        r = random.random() * 25 + 10
        
        draw_circle(x, y, r)
        
        time.sleep(0.125)