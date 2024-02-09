# Multiple balls all bouncing at once!

import pygame
import random

# import functions from the previous example
from bouncing_ball1 import process_events, draw_title


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
        ball = [x, y, vx, vy]
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
            ball[0] += ball[2]
            ball[1] += ball[3]
                        
            # Now draw the ball at its new position
            pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(ball[0], ball[1]), radius=30)
            
            # Do we need to bounce?
            if ball[0] < 0 or ball[0] > screen.get_width():
                ball[2] = -ball[2]
                
                # stop balls getting stuck beneath or above window
                ball[0] = max(0, ball[0])
                ball[0] = min(ball[0], screen.get_width())
                
            if ball[1] < 0 or ball[1] > screen.get_height():
                ball[3] = -ball[3]
                
                # stop balls getting stuck beneath or above window
                ball[1] = max(0, ball[1])
                ball[1] = min(ball[1], screen.get_height())

            # simulate the effect of gravity
            ball[3] = ball[3] + 1.5
        
        pygame.display.update()

        # Check to see if windows has been closed
        process_events()

        clock.tick(30)
        
