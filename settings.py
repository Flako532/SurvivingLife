"""
Settings.

My Settings.
"""

SCREEN_SIZE = (1921, 1081)
TABLE_SIZE = (27, 18)

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'bg-gray': (120, 120, 120),
    'rock-gray': (70, 65, 65),
    'water-blue': (43, 43, 215),
    'grass-green': (8, 125, 0),
    'pink': (219, 40, 210),
    'brown': (165, 42, 42),
    'green-ish': (17, 233, 161)
}

GROUND_TYPE = {
    'rock': COLORS['rock-gray'],
    'water': COLORS['water-blue'],
    'grass': COLORS['grass-green']
}

GROUND_PERCENTAGE = {
    'rock': 0.3,
    'water': 0.2,
    'grass': 0.5
}

TURN_TIME = 1.5
