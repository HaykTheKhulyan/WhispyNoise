import pygame
from Resources import colors

class Box:
    def __init__(self, x_pos, y_pos, width, height, fill_color=colors.BLACK, border_color=colors.BLACK, border_thickness=0):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height

        self.fill_color = fill_color
        self.border_color = border_color
        self.border_thickness = border_thickness

    def Draw(self, screen):
        if (self.border_thickness > 0):
            # draws the "border" by drawing a bigger rectangle under the regular rectangle
            pygame.draw.rect(screen,                                                        # the surface upon which to draw on
                             self.border_color,                                             # the color of the border rect
                            (self._x_pos - self.border_thickness,                           # the x position of the top left corner of the border rect
                             self._y_pos - self.border_thickness,                           # the y position of the top left corner of the border rect
                             self._width + (2 * self.border_thickness),                     # the width of the border rect
                             self._height + (2 * self.border_thickness)))                   # the height of the border rect

        pygame.draw.rect(screen,                    # the surface upon which to draw on
                         self.fill_color,           # the color of the rect
                        (self._x_pos,               # the x position of the top left corner of the rect
                         self._y_pos,               # the y position of the top left corner of the rect
                         self._width,               # the width of the rect
                         self._height))             # the height of the rect
