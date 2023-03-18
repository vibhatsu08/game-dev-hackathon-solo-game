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


# setting up the class for the player sprite.
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75, 25))
#         self.surf.fill((255, 0, 255))
#         self.rect = self.surf.get_rect()
#

class Player (pygame.sprite.Sprite) :
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()


screen = pygame.display.set_mode((screen_width, screen_height))

player = Player()

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
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))

    # creating its underlying rectangle
    rectangle = surf.get_rect()

    # finding the exact center of the surface to align it both horizontally and vertically in the center.
    surface_center = (
        (screen_width - surf.get_width()) / 2,
        (screen_height - surf.get_height()) / 2
    )

    # copying the contents from the surface to the screen.

    screen.blit(surf, surface_center)
    screen.blit(player.surf, (screen_width/2, screen_height/2))
    pygame.display.flip()
