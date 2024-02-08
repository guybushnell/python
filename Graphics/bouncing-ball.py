from time import sleep
import pygame
import sys
import random

def throw_ball():
    global vx, vy, ball_rect, energy_loss, still_moving

    # initial velocity of the ball
    vx = (20 * random.random()) - 10
    vy = (20 * random.random()) - 10
    
    # Draw a ball and get back the rectangle surrounding it
    ball_rect = pygame.draw.circle(surface=screen, color=red, center=[scr_width/2, ball_radius*2], radius=ball_radius)

    # Make the ball lose a little energy after each bounce
    energy_loss = 0.95
    still_moving = True


def draw_title(text: str):
    '''
    Place the given text in the centre of the screen
    '''
    font = pygame.font.SysFont(None, 36)
    img = font.render(text, True, pygame.Color("darkorange"))
    img_size = img.get_size()
    
    centre_x = (screen.get_width() - img.get_width()) / 2
    centre_y = (screen.get_height() - img.get_height()) / 2
    screen.blit(img, (centre_x, centre_y))
    pygame.display.update()

    pygame.init()

# Set screen size
scr_width = 500
scr_height = 500
ball_radius = 30

#  Some colours
red = (255, 0, 0)
black = (0, 0, 0)

# Initialise the sound mixing module so we can play sounds
pygame.mixer.init()
boing_sound = pygame.mixer.Sound("audio/boing.wav")

screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Bouncing Ball Test")

# gravity will affect the behavior of the y velocity
gravity = 0.7
    
# Set up the ball's initial velocity and position
throw_ball()

# Main loop - goes forever
while True:
    
    # Check to see if windows has been closed
    for event in pygame.event.get():
        # check if a user wants to exit the game or not
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            throw_ball()
 
    if still_moving:
        # fill black color on screen
        screen.fill(black)
        
        # Move the ball a little
        ball_rect = ball_rect.move(vx, vy)
        
        # Gravity is always pulling down by increasing y velocity towards the bottom of the window
        vy = vy + gravity
            
        x_bounce = False
        y_bounce = False
        
        # Check to see if the ball has hit left or right side of window
        if ball_rect.left <= 0:
            ball_rect.left = 0
            x_bounce = True
        elif ball_rect.right >= scr_width:
            ball_rect.right = scr_width
            x_bounce = True

        if x_bounce:    
            vx = -vx # yes, so reverse x-velocity
            
        # Check to see if the ball has hit top or bottom of window
        if ball_rect.top <= 0:
            ball_rect.top = 0
            y_bounce = True
        elif ball_rect.bottom >= scr_height:
            ball_rect.bottom = scr_height
            y_bounce = True
            
        if y_bounce:
            vy = -vy # yes, so reverse y-velocity
            
        # Now draw the ball at its new position
        pygame.draw.circle(surface=screen, color=red, center=ball_rect.center, radius=ball_radius)
        
        # Finally, update the screen so we can see what's changed!
        pygame.display.update()
        
        if x_bounce or y_bounce:
            boing_sound.play()
            vy = vy * energy_loss
            vx = vx * energy_loss
            energy_loss = energy_loss / 1.03
            
            # Should we quite if we've practically stopped?
            if abs(vx) < 0.2 and abs(vy) < 0.2:
                still_moving = False   
                draw_title("Press Mouse Button To Restart")            
                 
    sleep(0.025)
    
