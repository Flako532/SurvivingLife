"""
Docs.

DOcs.
"""
import pygame
import settings

TILE_WIDTH = int((settings.SCREEN_SIZE[0]-1)/settings.TABLE_SIZE[0])
TILE_HEIGHT = int((settings.SCREEN_SIZE[1]-1)/settings.TABLE_SIZE[1])


class GameObject():
    """Docs."""

    def __init__(self, name='', size=(1, 1)):
        """docs."""
        tileSize = (
            size[0]*TILE_WIDTH,
            size[1]*TILE_HEIGHT)
        self.name = ''
        self.surface = pygame.Surface(tileSize, pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()


class Worker(GameObject):
    """Docs."""

    def __init__(self):
        """docs."""
        super(Worker, self).__init__('worker')
        center = (int(TILE_HEIGHT/2), int(TILE_WIDTH/2))
        radius = int((TILE_WIDTH/2)-TILE_WIDTH*0.15)
        pygame.draw.circle(
            self.surface,
            settings.COLORS['pink'],
            center,
            radius)


class BaseBuilding(GameObject):
    """Docs."""

    def __init__(self, size=(2, 2), name='BaseBuilding'):
        """Docs."""
        super(BaseBuilding, self).__init__(name, size)
        self.name = name
        self.size = size
        self.health = 100
        self.color = color
        self.pos = None  # Tuple
