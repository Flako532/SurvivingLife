"""
This module controls the game and has all attributes refered to the game.

Lorem Ipsum.
"""
import pygame
import settings
import random

TILE_WIDTH = (settings.SCREEN_SIZE[0]-1)/settings.TABLE_SIZE[0]
TILE_HEIGHT = (settings.SCREEN_SIZE[1]-1)/settings.TABLE_SIZE[1]
NUMBER_OF_TILES = settings.TABLE_SIZE[0]*settings.TABLE_SIZE[1]


class Tile():
    """Represents a tile in the map."""

    def __init__(self, gt=None):
        """Docsstring."""
        size = (
            TILE_WIDTH,
            TILE_HEIGHT)
        self.surface = pygame.Surface(size)
        self.groundType = gt
        self.surface.fill(settings.GROUND_TYPE[gt])
        self.gameObject = None
        self.speedMod = None

    def get_tile_size(self):
        """Docstring."""
        return size


class Mapper():
    """Builds the entire map."""

    def __init__(self, size=settings.SCREEN_SIZE):
        """Docsstring."""
        self.background = pygame.Surface(size)
        self._drawBgLines()
        self.slots = []
        for slot in range(0, NUMBER_OF_TILES):
            self.slots.append(Tile(random.choice(['grass', 'rock', 'water'])))

    def _coord_to_pixels(self, x, y):
        """Docs."""
        x_pixels = x * TILE_WIDTH
        y_pixels = y * TILE_HEIGHT
        return (x_pixels, y_pixels)

    def _drawBgLines(self):
        """Draw the lines to make visual tile slots."""
        for x in range(0, 108):
            if not x > 72:
                pygame.draw.line(
                    self.background,
                    pygame.Color(
                        settings.COLORS['bg-gray'][0],
                        settings.COLORS['bg-gray'][1],
                        settings.COLORS['bg-gray'][2]),
                    (0, 10*x),
                    (1080, 10*x))
            pygame.draw.line(
                self.background,
                pygame.Color(
                    settings.COLORS['bg-gray'][0],
                    settings.COLORS['bg-gray'][1],
                    settings.COLORS['bg-gray'][2]),
                (10*x, 0),
                (10*x, 720))
        pygame.draw.lines(
            self.background,
            pygame.Color(
                settings.COLORS['bg-gray'][0],
                settings.COLORS['bg-gray'][1],
                settings.COLORS['bg-gray'][2]),
            False,
            ((0, 720), (1080, 720), (1080, 0)))

    def _draw_tiles(self):
        """Docs."""
        for index in range(0, len(self.slots)):
            coords = self._coord_to_pixels(
                index % settings.TABLE_SIZE[0],
                int(index / settings.TABLE_SIZE[0]))
            self.background.blit(
                self.slots[index].surface,
                (coords[0], coords[1]))

    def get_surface(self):
        """Get surface."""
        return self.background

    def update(self):
        """Docs."""
        self.background.fill(settings.COLORS['black'])
        self._draw_tiles()
        self._drawBgLines()


class GameMode():
    """Class manages game rules and flow."""

    def __init__(self):
        """Docstring."""
        self.world = Mapper()
