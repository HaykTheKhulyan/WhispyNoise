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
        
        if settings.DRAW_ORIGIN_CIRCLE:
            pygame.draw.circle(
                screen,                                                     # the surface upon which to draw on
                settings.ORIGIN_CIRCLE_COLOR,                               # the color of the circle
                (self._x_pos, self._y_pos),                                 # the center of the circle
                settings.ORIGIN_CIRCLE_RADIUS)                              # the radius of the circle
        elif settings.DRAW_ORIGIN_RECTANGLE:
            pygame.draw.rect(
                screen,                                                     # the surface upon which to draw on
                settings.ORIGIN_RECTANGLE_COLOR,                            # the color of the rect
                (self._x_pos - settings.ORIGIN_RECTANGLE_WIDTH / 2,         # the left border of the rect
                self._y_pos - settings.ORIGIN_RECTANGLE_WIDTH / 2,          # the top border of the rect
                settings.ORIGIN_RECTANGLE_WIDTH,                            # the width of the rect
                settings.ORIGIN_RECTANGLE_WIDTH))                           # the height of the rect 
                                                                            #
                                                                            # - Note that since we are drawing squares and 
                                                                            #   not rectangles, the height and width are equal

    
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

        self._x_vel *= settings.VELOCITY_MULTIPLIER
        self._y_vel *= settings.VELOCITY_MULTIPLIER

    def Draw(self, screen):
        pygame.draw.line(
            screen,                                                         # the surface upon which to draw on
            settings.PATH_COLOR,                                            # the color of the path
            (self._x_pos, self._y_pos),                                     # the current position of the particle
            (self._prev_x_pos, self._prev_y_pos),                           # the previous position of the particle
            settings.LINE_THICKNESS)                                        # the thiqueness of the path



