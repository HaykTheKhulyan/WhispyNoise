import noise
import random
import pygame


MAP_WIDTH = 500
MAP_HEIGHT = 500

SCALE = 7

# 1 for perlin, 2 for simplex
NOISE_TYPE = 1

def get_noise(x_pos, y_pos, z_pos, x_off, y_off):
    if (NOISE_TYPE == 1):
        return (noise.pnoise3(x_off + (x_pos / MAP_WIDTH * SCALE), y_off + (y_pos / MAP_HEIGHT * SCALE), z_pos) + 1) / 2
    elif (NOISE_TYPE == 2):
        return (noise.snoise3(x_off + (x_pos / MAP_WIDTH * SCALE), y_off + (y_pos / MAP_HEIGHT * SCALE), z_pos) + 1) / 2

if __name__ == "__main__":
    pygame.init()
    
    screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
    screen.fill(pygame.Color('white'))
    
    rand_x_offset = random.randint(-100000, 100000)
    rand_y_offset = random.randint(-100000, 100000)
    
    # creates a 2d list of noise values using list comprehension
    #noise_map = [[get_noise(i, j, rand_x_offset, rand_y_offset) for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]
    
    for z_off in range (0, 10):
        noise_map = [[get_noise(i, j, z_off / 5, rand_x_offset, rand_y_offset) for i in range(MAP_WIDTH)] for j in range(MAP_HEIGHT)]
        for col in range(MAP_WIDTH):
            for row in range(MAP_HEIGHT):
                color_value = int(abs(255 * noise_map[row][col]))
                color = pygame.Color(color_value, color_value, color_value)
                pygame.draw.line(screen, color, (row, col), (row, col))
        pygame.display.flip()
    print("Done")
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
