import noise
import random
import pygame


MAP_WIDTH = 100
MAP_HEIGHT = 100



if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
    screen.fill(pygame.Color('white'))
    
    rand_x_offset = random.randint(-100000, 100000)
    rand_y_offset = random.randint(-100000, 100000)
    
    # creates a 2d list of noise values using list comprehension
    noise_map = [[noise.pnoise2(rand_x_offset + (i / MAP_WIDTH), rand_y_offset + (j / MAP_HEIGHT)) for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]
    
    for col in range(MAP_WIDTH):
        for row in range(MAP_HEIGHT):
            color_value = int(abs(255 * noise_map[row][col]))
            color = pygame.Color(color_value, color_value, color_value)
            pygame.draw.line(screen, color, (row, col), (row, col))
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
