import pygame
import Box

from Resources import colors

class Button(Box.Box):
    
    def __init__(self, x_pos, y_pos, width, height, text, font_size, fill_color=colors.BLACK, border_color=colors.BLACK, border_thickness=0):
        super(Button, self).__init__(x_pos, y_pos, width, height, fill_color, border_color, border_thickness)
        
        self.font = pygame.font.Font('freesansbold.ttf', font_size)
        self.textSurface = self.font.render(text, True, colors.BLACK)

    def get_rect(self):
        return pygame.Rect(self._x_pos, self._y_pos, self._width, self._height)
    
    def Draw(self, screen):
        super(Button, self).Draw(screen)
        screen.blit(self.textSurface, (self._x_pos, self._y_pos))

    
        

