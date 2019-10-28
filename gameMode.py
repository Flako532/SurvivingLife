"""
This module controls the game and has all attributes refered to the game.

Lorem Ipsum.
"""
import pygame
import settings
import random
from gameObjects import Worker
from mapper import Mapper
from controller import Controller


class GameMode():
    """Class manages game rules and flow."""

    def __init__(self):
        """Docstring."""
        self.world = Mapper()
        self.controller = Controller()
        self.running = False

    def startGame(self):
        """Docs."""
        self.world.load_map()
        worker = Worker()
        self.world.spawn_object(
            worker,
            (settings.TABLE_SIZE[0]-5, settings.TABLE_SIZE[1]-15))

    def update_all(self):
        """Docs."""
        self.world.update()

    def quit(self):
        """Docs."""
        self.running = False

    def mouse_action(self, event):
        """Docs."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.controller.mouse_button_down(
                self.world,
                event.button,
                event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            self.controller.mouse_button_up(
                self.world,
                event.button,
                event.pos)
        if event.type == pygame.MOUSEMOTION:
            self.controller.mouse_motion(
                self.world,
                event.buttons,
                event.pos,
                event.rel)