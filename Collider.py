import pygame

class Collider:

    def Collide(self, mouse_pos, rect):
        return rect.collidepoint(mouse_pos)