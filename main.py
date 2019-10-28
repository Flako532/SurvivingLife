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

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            gameMode.control.mouse_button_down(event.button, event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            gameMode.control.mouse_button_up(event.button, event.pos)
        if event.type == pygame.MOUSEMOTION:
            gameMode.control.mouse_motion(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                gameMode.world.save_map()
            if event.key == pygame.K_a:
                gameMode.world.load_map()

    gameMode.world.update()
    # time.sleep(0.75)
    screen.blit(gameMode.world.get_surface(), (0, 0))
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
