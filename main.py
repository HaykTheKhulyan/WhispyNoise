import noise
import random
import pygame
import math
import time

MAP_WIDTH = 500
MAP_HEIGHT = 500

SCALE = 100

# 1 for perlin, 2 for simplex
NOISE_TYPE = 2

def get_noise(x_pos, y_pos, z_pos, x_off, y_off):
    if (NOISE_TYPE == 1):
        return noise.pnoise3(x_off + (x_pos / MAP_WIDTH * SCALE), y_off + (y_pos / MAP_HEIGHT * SCALE), z_pos)
    elif (NOISE_TYPE == 2):
        return noise.snoise3(x_off + (x_pos / MAP_WIDTH * SCALE), y_off + (y_pos / MAP_HEIGHT * SCALE), z_pos)

if __name__ == "__main__":
    pygame.init()
    
    # creates the screen
    screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
    
    # ensures that no two program runs use the same noise values
    rand_x_offset = random.randint(-100000, 100000)
    rand_y_offset = random.randint(-100000, 100000)
    
    # outer loop steps through layers in the z direction
    for z_off in range (0, 10):
        # clears the screen 
        screen.fill(pygame.Color('white'))

        # generates a new slice of the noise map with the new z offset. In the future, maybe generate a 3 dimensional slice at the beginning for faster run times?
        noise_map = [[get_noise(i, j, z_off / 5, rand_x_offset, rand_y_offset) for i in range(int(MAP_WIDTH / 10))] for j in range(int(MAP_HEIGHT / 10))]

        # these loop through the grid and draw the vectors
        for col in range(int(MAP_WIDTH / 10)):
            for row in range(int(MAP_HEIGHT / 10)):
                # calculates the endpoint of the line based on the noise value at that point
                line_endpoint_x = row + math.cos(noise_map[row][col])
                line_endpoint_y = col + math.sin(noise_map[row][col])

                # draws the line on the screen, color black, starting at row/col and ending at the newly calculated endpoint
                pygame.draw.line(screen, pygame.Color('black'), (10 * row, 10 * col), (10 * line_endpoint_x, 10 * line_endpoint_y))

        # updates the display
        pygame.display.flip()
        
        # small pause, will probably delete for real thing
        time.sleep(0.5)

    # for testing, to know when the program finished updating
    print("Done")
   
    # if the program is exited, we exit
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
