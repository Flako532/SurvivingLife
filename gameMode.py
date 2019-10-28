"""
This module controls the game and has all attributes refered to the game.

Lorem Ipsum.
"""
import pygame
import settings
import random
from gameObjects import Worker


class GameMode():
    """Class manages game rules and flow."""

    def __init__(self):
        """Docstring."""
        self.world = Mapper()

    def startGame(self):
        """Docs."""
        self.world.load_map()
        worker = Worker()
        self.world.spawn_object(
            worker,
            (settings.TABLE_SIZE[0]-5, settings.TABLE_SIZE[1]-15))
