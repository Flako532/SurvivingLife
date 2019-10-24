# coding=utf-8
"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import pygame
import sys
import settings


pygame.init()

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(settings.SCREEN_SIZE)

ball = pygame.Surface((70, 70))
pygame.draw.circle(ball, pygame.Color(125, 125, 125), (35, 35), 35)
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > settings.SCREEN_SIZE[0]:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > settings.SCREEN_SIZE[1]:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
