# importing any initialising the pygame.
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# initialising pygame.
pygame.init()

# setting up the screen.
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# setting up the key event handlers with the game loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    # creating or drawing something on the screen using the Surface.
    screen.fill((255, 255, 255))

    # now creating a Surface
    surface = pygame.Surface((50, 50))
    surface.fill((0, 0, 0))

    # creating its underlying rectangle
    rectangle = surface.get_rect()

    # finding the exact center of the surface to align it both horizontally and vertically in the center.
    surface_center = (
        (screen_width - surface.get_width())/2,
        (screen_height - surface.get_height())/2
    )

    # copying the contents from the surface to the screen.
    screen.blit(surface, surface_center)
    pygame.display.flip()