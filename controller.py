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
        self.selection = []
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
        for item in self.selection:
            self.selection.remove(item)
            world.deselect_tile(item)

    def mouse_button_down(self, world, button, pos):
        """Docs."""
        if button == 1:
            self.remove_selection(world)
            self.mouseOptions['button1'] = True
            self.mouseOptions['position']['x'],
            self.mouseOptions['position']['y'] = pos
            self.selection.append(world.get_tile_by_pixels(
                pos))

    def mouse_button_up(self, world, button, pos):
        """Docs."""
        if button == 1:
            self.mouseOptions['button1'] = False
            if self.mouseOptions['offset'] == ZERO_POS:
                for item in self.selection:
                    world.select_tile(item)

    def mouse_motion(self, world, button, pos, rel):
        """Docs."""
        pass
