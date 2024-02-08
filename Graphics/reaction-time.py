# Simple reaction time game. 
# Click on the green circles but not the red ones
# Be as quick as you can.

import pygame
import random
import time


def process_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            exit()
            
            
def wait_for_keypress():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN: 
                screen.fill((0, 0, 0))
                return
            elif event.type==pygame.QUIT: 
                exit()
                
                            
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
    
                
def draw_target() -> (bool, pygame.Rect):
    '''
    returns: true if the target is valid and the user should click!
    Also returns the bounding rectangle of the circle.
    '''
    # give the target a random position on screen
    x = random.random() * screen_width
    y = random.random() * screen_height

    # set the window background to black
    screen.fill(pygame.Color("black"))

    # Occasionally make an invalid target that the user shouldn't hit
    if random.random() >= 0.25:
        valid_target = True
        rect = pygame.draw.circle(surface=screen, color=pygame.Color("green"), center=[x, y], radius=target_radius)
    else:
        valid_target = False
        rect = pygame.draw.circle(surface=screen, color=pygame.Color("green"), center=[x, y], radius=target_radius, width=10)

    pygame.display.update()

    return (valid_target, rect)


pygame.init()

# Initialise the sound mixing module so we can play sounds
pygame.mixer.init()
good_sound = pygame.mixer.Sound("audio/correct.mp3")
bad_sound = pygame.mixer.Sound("audio/wrong-answer-buzzer.wav")

# Set screen size
screen_width = 500
screen_height = 500
target_radius = 30

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Time Test")

hits = 0
total_tests = 10
clock = pygame.time.Clock()

process_events()

# Show a some help about how to play
draw_title("Click the solid circles only!")

# a little pause for breath before we kick-off
time.sleep(2)

# Main loop - do a run of tests then stop
for test_number in range(0, total_tests):
    (valid_target, target_rect) = draw_target()

    start_time = time.time()
    button_pressed = False
    elapsed_time = 0

    # now wait for input from the user but only for a few seconds
    while not button_pressed and elapsed_time < 1:        
        # Check to see if windows has been closed
        for event in pygame.event.get():
            # check if a user wants to exit the game or not
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_pressed = True
                button_pos = pygame.mouse.get_pos()


        # How long have we been waiting for the user to press a button
        elapsed_time = time.time() - start_time

    # Logic table
    #   B V H
    #   F F F = T
    #   F F T -----X
    #   F T F = F
    #   F T T -----X
    #   T F F = F
    #   T F T = F
    #   T T F = F
    #   T T T = T

    if not button_pressed and not valid_target:
        success = True
    elif button_pressed and valid_target and target_rect.collidepoint(button_pos):
        success = True
    else:
        success = False
        
    if success:
        print("Reaction time: %.2f seconds" % elapsed_time)
        good_sound.play()
        hits = hits + 1
    else:
        # All other outcomes are bad
        bad_sound.play()

    screen.fill(pygame.Color("black"))
    pygame.display.update()


success_rate = 100 / total_tests * hits
draw_title("Hits: %d, Misses: %d - %d%% success rate" % (hits, total_tests-hits, success_rate))

wait_for_keypress()