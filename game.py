# This program is an equivalent to any hello world program in any other programming language.

# Importing and initialising the pygame library.
import pygame

# setting the screen size parameters.
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# setting up the game loop.
running = True
while running :
    # event for if the user clicked the window close button.
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        # filling the background color with white
        screen.fill((255, 255, 255))

        # draws a solid circle on the screen.
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50)

        # updates the contents of the screen.
        pygame.display.flip()

# Quits the game, happens only when the loop finishes.
pygame.quit()
