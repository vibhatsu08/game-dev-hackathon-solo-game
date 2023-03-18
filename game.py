# importing any initialising the pygame.
import pygame

# importing the random library for the enemies.
import random

# importing the keystrokes from the pygame.locals.
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


# setting up the player sprite.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()

    # comes into action when the keys mentioned above are registered in the returned pressed_keys dictionary below.
    def update(self, pressed_keys):
        # the corresponding action is taken care of based on the key pressed.
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # to avoid the player sprite from moving off-screen, by doing this the player stays in the limits of the screen.
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


# setting up the enemy sprite.
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )
        self.speed = random.randint(1, 4)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# sets up the dimensions of the screen based on the screen_width and screen_height variables.
screen = pygame.display.set_mode((screen_width, screen_height))

# player is an instance of the Player class created above.
player = Player()

# creating two sprite groups,
# one for the enemy.
# and the other one for the player.
enemy = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# setting up the key event handlers with the game loop.
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # return a dictionary of all the keys pressed.
    pressed_keys = pygame.key.get_pressed()

    # update the frame every time in order to move the player, based on the key pressed.
    player.update(pressed_keys)

    # creating or drawing something on the screen using the Surface. The main screen is a surface since all the other
    # sprites for the player will be a Surface sprite.
    screen.fill((255, 255, 255))

    # now creating a Surface
    surf = pygame.Surface((50, 50))
    # surf Surface has the color of black.
    surf.fill((0, 0, 0))

    # creating its underlying rectangle
    rect = surf.get_rect()

    # finding the exact center of the surface to align it both horizontally and vertically in the center.
    surface_center = (
        (screen_width - surf.get_width()) / 2,
        (screen_height - surf.get_height()) / 2
    )

    # copying the contents from the surface to the screen.
    # screen.blit(surf, surface_center)
    # screen.blit(player.surf, (screen_width / 2, screen_height / 2))

    # instead of calling .blit on just the player, you can iterate over all the sprites in the all_sprites group.
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
