# Simple bouncing ball
# Add sounds to the bounce and the effect of gravity
import pygame
from bouncing_ball1 import process_events, draw_title


# ==== Start Here ====
if __name__ == "__main__":

    # Start pygame and create the game window
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("bouncing-ball1 - Simple Bouncing Ball")
    
    pygame.mixer.init()
    bounce_sound = pygame.mixer.Sound("audio/boing.wav")
    
    # we will use the clock to make the animation look smooth
    clock = pygame.time.Clock()

    # initial velocity of the ball
    vx, vy = 17, 13

    # the centre of the ball
    x, y = 0, 0  

    # Main loop - goes forever
    while True:
        
        # Check to see if windows has been closed
        process_events()
    
        # Move the ball a little
        x += vx
        y += vy
        
        # Now draw the ball at its new position
        screen.fill(0)
        pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(x,y), radius=30)
        pygame.display.update()
        
        # Do we need to bounce?
        if x < 0 or x > screen.get_width():
            vx = -vx
            bounce_sound.play()
            
        if y < 0 or y > screen.get_height():
            vy = -vy
            bounce_sound.play()

        # simulate the effect of gravity
        vy = vy + 0.9
        
        clock.tick(30)
        
