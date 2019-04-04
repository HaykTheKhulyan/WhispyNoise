import pygame
import pygame_textinput

import Box
from Resources import settings, colors

class TextBox(Box.Box):
    
    def __init__(self, x_pos, y_pos, width, height):
        super(TextBox, self).__init__(x_pos, y_pos, width, height)
        self.input_box = pygame_textinput.TextInput(text_color=colors.WHITE)
    
    def Update(self, events):
        self.input_box.update(events)

    def Draw(self, screen):
        super(TextBox, self).Draw(screen)                                           # the height of the rect
        screen.blit(self.input_box.get_surface(), (self._x_pos, self._y_pos))





