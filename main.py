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

FPS = 30
TOP_LEFT_CORNER = (0, 0)

screen = pygame.display.set_mode(settings.SCREEN_SIZE)

gameMode = GameMode()
screen.blit(gameMode.world.get_surface(), TOP_LEFT_CORNER)
gameMode.startGame()

clock = pygame.time.Clock()

gameMode.running = True

while gameMode.running:
    # For every event
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            sys.exit()
            gameMode.quit()

        # Mouse Events
        gameMode.mouse_action(event)

        # Keyboard Event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                gameMode.save()
            if event.key == pygame.K_a:
                gameMode.load()

    # Update graphics
    gameMode.update_all()
    screen.blit(gameMode.get_game_screen(), (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
