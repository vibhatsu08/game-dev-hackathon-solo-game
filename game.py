# This program is an equivalent to any hello world program in any other programming language.

# Importing and initializing the game library.
import pygame
pygame.init()

# setting up the screen's width and height parameters.
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# flag for the game loop, the game will run as long as the loop is True.
running = True

while running :
    # event to check when the game window is closed.
    for event in pygame.event.get() :
        # checks if the game window is closed.
        if event.type == pygame.QUIT :
            running = False

    # setting the screen's/display's color.
    screen.fill((0, 0, 0))

    # drawing out the circle on the screen, with it's other parameters such as it's size, color, coordinates, radius.
    pygame.draw.circle(screen, (255, 255, 0), (250, 250), 50)

    # updates the content of the screen.
    pygame.display.flip()

# quits the game when the loop is done running, or when the loop finishes.
pygame.quit()