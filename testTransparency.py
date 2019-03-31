import pygame 
from math import pi

pygame.init()

size = [600, 600] 
screen = pygame.display.set_mode(size)
vertical_line = pygame.Surface((600, 600), pygame.SRCALPHA)

running = True

while (running):



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    #vertical_line.fill((0, 255, 0, 50)) # You can change the 100 depending on what transparency it is.
    pygame.draw.circle(vertical_line, pygame.Color(0, 0, 0, 50), (300, 300), 50)
    screen.blit(vertical_line, (0, 0))

    pygame.display.flip()

pygame.quit()