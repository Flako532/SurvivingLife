"""
Docs.

Docs
"""

import pygame
import settings
import selectionRect

ZERO_POS = {
    'x': 0,
    'y': 0
}


class Controller():
    """docstring for ClassName."""

    def __init__(self):
        """Docs."""
        self.selectedTile = None
        self.selectionBox = None
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
            self.mouseOptions['position']['x'] = pos[0]
            self.mouseOptions['position']['y'] = pos[1]
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
            self.mouseOptions['position']['x'] = pos[0]
            self.mouseOptions['position']['y'] = pos[1]
            self.mouseOptions['offset'] = ZERO_POS

            self.selectionBox.updateRect(pos)
            self.selectionBox.hide(world.get_surface())

            new_tile = world.get_tile_by_pixels(pos)
            if self.selectedTile is not new_tile:
                self.selectedTile = new_tile
                world.select_tile(self.selectedTile)

    def mouse_motion(self, world, buttons, pos, rel):
        """Docs."""
        if buttons == (1, 0, 0):
            self.mouseOptions['offset']['x'] = pos[0] - self.mouseOptions['position']['x']
            self.mouseOptions['offset']['y'] = pos[1] - self.mouseOptions['position']['y']
            startPos = (
                self.mouseOptions['position']['x'],
                self.mouseOptions['position']['y'])
            size = (
                self.mouseOptions['offset']['x'],
                self.mouseOptions['offset']['y'])
