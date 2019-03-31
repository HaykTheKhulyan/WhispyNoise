import math
import pygame

from Resources import colors, settings

class Particle:
    
    def __init__(self, x_pos, y_pos, screen):
        self._x_pos = x_pos
        self._y_pos = y_pos
        
        self._prev_x_pos = x_pos
        self._prev_y_pos = y_pos

        self._x_vel = 0
        self._y_vel = 0

        self._x_accel = 0
        self._y_accel = 0
        
        #pygame.draw.circle(screen, colors.VERY_LIGHT_BLUE, (self._x_pos, self._y_pos), 5)

    
    def Update(self, noise_map):
        if (self._x_pos > 0 and self._y_pos > 0 and self._x_pos < settings.WINDOW_WIDTH and self._y_pos < settings.WINDOW_HEIGHT):
            self._x_accel = math.cos(noise_map[int(self._x_pos / 10)][int(self._y_pos / 10)] * math.pi)
            self._y_accel = math.sin(noise_map[int(self._x_pos / 10)][int(self._y_pos / 10)] * math.pi)
        
        self._x_vel += self._x_accel
        self._y_vel += self._y_accel
        
        self._prev_x_pos = self._x_pos
        self._prev_y_pos = self._y_pos

        self._x_pos += int(self._x_vel)
        self._y_pos += int(self._y_vel)

        self._x_vel *= 0.55
        self._y_vel *= 0.55

    def Draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0, 100), (self._x_pos, self._y_pos), (self._prev_x_pos, self._prev_y_pos), 2)



