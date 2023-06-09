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
screen_width = 1200
screen_height = 800

# setting the player height.
player_height = 100
player_width = 60

# setting up the enemy height.
enemy_height = 70
enemy_width = 90


# setting up the player sprite.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/PLAYER_IRONMAN.png")
        self.surf = pygame.transform.scale(self.surf, (player_width, player_height))
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
        self.surf = pygame.image.load("images/ENEMY_ALIEN.png")
        self.surf = pygame.transform.scale(self.surf, (enemy_width, enemy_height))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# sets up the dimensions of the screen based on the screen_width and screen_height variables.
screen = pygame.display.set_mode((screen_width, screen_height))

# create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# player is an instance of the Player class created above.
player = Player()

# creating two sprite groups,
# one for the enemy.
# and the other one for the player.
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# setting the background image.
background_image = pygame.image.load("images/BACKGROUND_WALLPAPER.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# creating a custom event for handling the scorecard for the game.
UPDATESCORE = pygame.USEREVENT + 2
pygame.time.set_timer(UPDATESCORE, 900)

# variable for maintaining the score
score = 0

# lives that the player has, originally the player will have 3 lives, but with every collision the lives decrement
# by 1.
player_lives = 3

# counter for the infinite moving background image.
counter = 0

# setting up the key event handlers with the game loop.
running = True

while running:
    # setting up the display text for the game.
    font = pygame.font.Font("freesansbold.ttf", 30)
    text = font.render(f"your score : is {score} points", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (screen_width - text.get_width() / 2, 0 + text.get_height() / 2)

    # setting up the lives card for the player in the game.
    lives_card = pygame.font.Font("freesansbold.ttf", 30)
    lives_text = font.render(f"lives remaining : {player_lives}", True, (255, 255, 255), (0, 0, 0))
    lives_rect = lives_text.get_rect()
    lives_rect.center = (0 + lives_text.get_width()/2, 0 + lives_text.get_height()/2)

    screen.fill((0, 0, 0))
    screen.blit(background_image, (counter, 0))
    screen.blit(background_image, (screen_width + counter, 0))
    if counter == -screen_width:
        screen.blit(background_image, (screen_width + counter, 0))
        counter = 0
    counter -= 1
    screen.blit(text, text_rect)
    screen.blit(lives_text, lives_rect)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        # add the new enemy event handler.
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # deals with the UPDATESCORE event.
        elif event.type == UPDATESCORE:
            score += 1

    # collision detection for the sprite and the enemies.
    # basically if the player collides with any of the member sprites of the enemies group, the player is
    # killed and the loop is broken.
    if pygame.sprite.spritecollide(player, enemies, True):
        player_lives -= 1

    elif player_lives == 0:
        player.kill()
        running = False
    # return a dictionary of all the keys pressed.
    pressed_keys = pygame.key.get_pressed()

    # update the enemies' position.
    enemies.update()

    # update the frame every time in order to move the player, based on the key pressed.
    player.update(pressed_keys)

    # creating or drawing something on the screen using the Surface. The main screen is a surface since all the other
    # sprites for the player will be a Surface sprite.
    # screen.fill((255, 255, 255))

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

    # setting the frame rate for the game.
    clock = pygame.time.Clock()
    clock.tick(700)

    # updates the contents of the screen throughout the loop.
    pygame.display.flip()
