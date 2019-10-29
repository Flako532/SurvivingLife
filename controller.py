"""
Docs.

Docs
"""

import pygame
import settings

ZERO_POS = {
    'x': 0,
    'y': 0
}


class Controller():
    """docstring for ClassName."""

    def __init__(self):
        """Docs."""
        self.selectedTile = None
        self.selectedObjects = []
        self.mouseOptions = {
           'position': {
               'x': 0,
               'y': 0
           },
           'offset': {
               'x': 0,
               'y': 0
           },
           'button1': False,
           'button2': False,
        }

    def remove_selection(self, world):
        """Docs."""
        self.selectedObjects.clear()
        self.selectedTile = None
        world.clear_selection()

    def mouse_button_down(self, world, button, pos):
        """Docs."""
        if button == 1:
            # Save parameters
            self.mouseOptions['button1'] = True
            self.mouseOptions['position']['x'],
            self.mouseOptions['position']['y'] = pos
            # Check tile
            new_tile = world.get_tile_by_pixels(pos)
            if self.selectedTile == new_tile:
                world.change_tile_selection(new_tile)
            else:
                # Deselect
                self.remove_selection(world)

    def mouse_button_up(self, world, button, pos):
        """Docs."""
        if button == 1:
            self.mouseOptions['button1'] = False
            new_tile = world.get_tile_by_pixels(pos)
            if self.selectedTile is not new_tile:
                self.selectedTile = new_tile
                world.select_tile(self.selectedTile)

    def mouse_motion(self, world, button, pos, rel):
        """Docs."""
        pass
