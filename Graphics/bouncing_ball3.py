# Multiple balls all bouncing at once!

import pygame
import random

from dataclasses import dataclass

# import functions from the previous example
from bouncing_ball1 import process_events, draw_title

@dataclass
class Ball:
    """ Describes a ball's centre point (x,y) and velocity (vx, vy) """
    x: float
    vx: float

    y: float
    vy: float
    
    
def create_balls(screen: pygame.Surface, nof_balls: int) -> list:
    '''
    Creates a list of balls, all with different start points and different velocities
    @returns a list of balls - [ [x, y, vx, vy] ... ]
    '''
    # our empty list of balls
    balls = []
    
    for i in range(0, nof_balls):
        x = random.random() * screen.get_width()
        y = random.random() * screen.get_height()
        vx = (20*random.random()) - 10
        vy = (20*random.random()) - 10
        
        # create then add this new ball to the list
        # make sure parameter are in same order as Class - or name then to be safe
        ball = Ball(x, vx, y, vy)
        balls.append(ball)   
        
    return balls
    
    
# ==== Start Here ====
if __name__ == "__main__":

    # Start pygame and create the game window
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("bouncing-ball2 - Multiple Bouncing Balls")
    
    # we will use the clock to make the animation look smooth
    clock = pygame.time.Clock()

    balls = create_balls(screen=screen, nof_balls=15)

    # Main loop - goes forever
    while True:
        screen.fill(0)

        for ball in balls:
            # Move the ball a little
            ball.x += ball.vx
            ball.y += ball.vy
                        
            # Now draw the ball at its new position
            pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(ball.x, ball.y), radius=30)
            
            # Do we need to bounce?
            if ball.x < 0 or ball.x > screen.get_width():
                ball.vx = -ball.vx
                
                # stop balls getting stuck beneath or above window
                ball.x = max(0, ball.x)
                ball.x = min(ball.x, screen.get_width())
                
            if ball.y < 0 or ball.y > screen.get_height():
                ball.vy = -ball.vy
                
                # stop balls getting stuck beneath or above window
                ball.y = max(0, ball.y)
                ball.y = min(ball.y, screen.get_height())

            # simulate the effect of gravity
            ball.vy = ball.vy + 1.5
        
        pygame.display.update()

        # Check to see if windows has been closed
        process_events()

        clock.tick(30)
        
