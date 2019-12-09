# coding=utf-8
"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import pygame
import sys
import time
import settings
from gameMode import GameMode
from gameObjects import GameObject


pygame.init()

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(settings.SCREEN_SIZE)

gameMode = GameMode()
screen.blit(gameMode.world.get_surface(), (0, 0))
gameMode.startGame()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                gameMode.world.save_map()
            if event.key == pygame.K_a:
                gameMode.world.load_map()

    gameMode.world.update()
    # time.sleep(0.75)
    screen.blit(gameMode.world.get_surface(), (0, 0))
    pygame.display.flip()
