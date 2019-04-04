import pygame
from Resources import colors

class Box:
    def __init__(self, x_pos, y_pos, width, height):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self.width = width
        self.height = height

    def Draw(self, screen):
        pygame.draw.rect(
                screen,                                                     # the surface upon which to draw on
                colors.BLACK,                                               # the color of the rect
                (self._x_pos,                                               # the left border of the rect
                 self._y_pos,                                               # the top border of the rect
                 self.width,                                                # the width of the rect
                 self.height))                                              # the height of the rect
