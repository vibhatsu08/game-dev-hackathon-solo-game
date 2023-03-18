# This program is an equivalent to any hello world program in any other programming language.

# Importing and initialising the pygame library. Along with the keystrokes.
import pygame

# importing pygame.locals for easier access to the keystrokes.
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# iniitalise the game.
pygame.init()

# creating the canvas to be able to draw something on it.
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# setting the game loop and checking for any kind of key events.
# checking for loop ending events.
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
