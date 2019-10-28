"""
Docs.

Docs.
"""

import pygame
import settings

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
        self.select = {
            'tile': False,
            'object': False
        }
        self.surface = pygame.Surface(size)
        self.groundType = gt
        self.surface.fill(settings.GROUND_TYPE[self.groundType])
        self.gameObject = None
        self.speedMod = None

    def get_tile_size(self):
        """Docstring."""
        return size

    def update(self):
        """Docs."""
        self.surface.fill(settings.GROUND_TYPE[self.groundType])
        if self.gameObject is not None:
            self.surface.blit(self.gameObject.surface, (0, 0))
        if self.select['tile']:
            selection_surface = pygame.Surface(
                self.surface.get_size(),
                pygame.SRCALPHA,
                32)
            self.surface = self.surface.convert_alpha()
            pygame.draw.lines(
                selection_surface,
                settings.COLORS['black'],
                True,
                [(1, 1),
                 (1, selection_surface.get_size()[1]-1),
                 (selection_surface.get_size()[0]-1,
                    selection_surface.get_size()[1]-1),
                 (selection_surface.get_size()[0]-1, 1)])
            self.surface.blit(selection_surface, (0, 0))

    def select_tile(self):
        """Docs."""
        self.select['tile'] = True

    def deselect_tile(self):
        """Docs."""
        self.select['tile'] = False

    def change_color(self):
        """Docstring."""
        if self.groundType == 'rock':
            self.groundType = 'water'
        elif self.groundType == 'water':
            self.groundType = 'grass'
        elif self.groundType == 'grass':
            self.groundType = 'rock'

    def force_color(self, gt):
        """Docs."""
        self.groundType = gt

    def receive_object(self, obj):
        """Docs."""
        self.gameObject = obj


class Mapper():
    """Builds the entire map."""

    def __init__(self, size=settings.SCREEN_SIZE):
        """Docsstring."""
        self.background = pygame.Surface(size)
        self._drawBgLines()
        self.slots = []
        for slot in range(0, NUMBER_OF_TILES):
            self.slots.append(Tile('grass'))

    def _coordinates_to_index(self, coordinates):
        return coordinates[0] + coordinates[1] * settings.TABLE_SIZE[0]

    def _pixels_to_index(self, pos):
        """DOCS."""
        x_coordinate = int(pos[0] / TILE_WIDTH)
        y_coordinate = int(pos[1] / TILE_HEIGHT)
        index = self._coordinates_to_index((x_coordinate, y_coordinate))
        return index

    def _coordinates_to_pixels(self, x, y):
        """Docs."""
        x_pixels = x * TILE_WIDTH
        y_pixels = y * TILE_HEIGHT
        return (x_pixels, y_pixels)

    def _drawBgLines(self):
        """Draw the lines to make visual tile slots."""
        for x in range(0, settings.TABLE_SIZE[0]):
            if not x > settings.TABLE_SIZE[1]:
                pygame.draw.line(
                    self.background,
                    pygame.Color(
                        settings.COLORS['bg-gray'][0],
                        settings.COLORS['bg-gray'][1],
                        settings.COLORS['bg-gray'][2]),
                    (0, TILE_HEIGHT*x),
                    (settings.SCREEN_SIZE[0] - 1, TILE_HEIGHT*x))
            pygame.draw.line(
                self.background,
                pygame.Color(
                    settings.COLORS['bg-gray'][0],
                    settings.COLORS['bg-gray'][1],
                    settings.COLORS['bg-gray'][2]),
                (TILE_WIDTH*x, 0),
                (TILE_WIDTH*x, settings.SCREEN_SIZE[1]))
        pygame.draw.lines(
            self.background,
            pygame.Color(
                settings.COLORS['bg-gray'][0],
                settings.COLORS['bg-gray'][1],
                settings.COLORS['bg-gray'][2]),
            False,
            ((0, settings.SCREEN_SIZE[1] - 1),
                (settings.SCREEN_SIZE[0] - 1, settings.SCREEN_SIZE[1] - 1),
                (settings.SCREEN_SIZE[0] - 1, 0)))

    def _draw_tiles(self):
        """Docs."""
        for index in range(0, len(self.slots)):
            coordinates = self._coordinates_to_pixels(
                index % settings.TABLE_SIZE[0],
                int(index / settings.TABLE_SIZE[0]))
            self.background.blit(
                self.slots[index].surface,
                (coordinates[0], coordinates[1]))

    def get_tile_by_pixels(self, mousePos):
        """Docs."""
        index = self._pixels_to_index(mousePos)
        return self.slots[index]

    def select_tile(self, tile):
        """Docs."""
        index = self.slots.index(tile)
        self.slots[index].select_tile()

    def deselect_tile(self, tile):
        """Docs."""
        index = self.slots.index(tile)
        self.slots[index].deselect_tile()

    def get_surface(self):
        """Get surface."""
        return self.background

    def change_tile_color(self, pos):
        """DOCS."""
        # ex pos. (425, 129)
        index = self._pixels_to_index(pos)
        self.slots[index].change_color()

    def spawn_object(self, obj, coordinates):
        """Docs."""
        index = self._coordinates_to_index(coordinates)
        self.slots[index].receive_object(obj)

    def update(self):
        """Docs."""
        self.background.fill(settings.COLORS['black'])
        for slot in self.slots:
            slot.update()
        self._draw_tiles()
        self._drawBgLines()

    def save_map(self):
        """Docs."""
        import json
        saveFile = open('maps/testmap.json', 'w')
        data = {}
        for index in range(0, len(self.slots)):
            data[str(index)] = self.slots[index].groundType
        json_data = json.dumps(data)
        saveFile.write(json_data)
        saveFile.close()
        print('File Saved')

    def load_map(self):
        """Docs."""
        import json
        with open('maps/testmap.json', 'r') as mapFile:
            json_data = json.loads(mapFile.read())
            for index in json_data:
                self.slots[int(index)].force_color(json_data[index])
