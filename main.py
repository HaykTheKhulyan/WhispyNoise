import noise
import random
import pygame
import math
import time

MAP_WIDTH = 500
MAP_HEIGHT = 500

SCALE = 20

# 1 for perlin, 2 for simplex
NOISE_TYPE = 2

def get_noise(x_pos, y_pos, z_pos, x_off, y_off):
    if (NOISE_TYPE == 1):
        return noise.pnoise3(x_off + (x_pos / MAP_WIDTH * SCALE), y_off + (y_pos / MAP_HEIGHT * SCALE), z_pos) + 1
    elif (NOISE_TYPE == 2):
        return noise.snoise3(x_off + (x_pos / MAP_WIDTH * SCALE), y_off + (y_pos / MAP_HEIGHT * SCALE), z_pos) + 1

if __name__ == "__main__":
    pygame.display.init()
    
    # creates the screen
    screen = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
    
    # ensures that no two program runs use the same noise values
    rand_x_offset = random.randint(-100000, 100000)
    rand_y_offset = random.randint(-100000, 100000)

    # makes the "slice" of the noise map be taken at slightly different positions each loop
    z_off = 0
    
    # used to check if the program was closed
    running = True

    # tracks the delta time since the last loop
    delta_time = 0

    # records the beginning of the loop
    start = time.perf_counter()

    # records the end of the loop
    end = time.perf_counter()

    # outer loop steps through layers in the z direction
    while (running):
        # sets the amount of time since the last loop
        delta_time += end - start

        # records the time the loop started
        start = time.perf_counter()

        # checks the events and stops the program from running if the "X" was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # updates at most 20 times a second
        if (delta_time > 1 / 20):
            # generates a new slice of the noise map with the new z offset. In the future, maybe generate a 3 dimensional slice at the beginning for faster run times?
            noise_map = [[get_noise(i, j, z_off, rand_x_offset, rand_y_offset) for i in range(int(MAP_WIDTH / 10))] for j in range(int(MAP_HEIGHT / 10))]

            # clears the drawings of the previous frame
            screen.fill(pygame.Color('white'))

            # these loop through the grid and draw the vectors
            for col in range(int(MAP_WIDTH / 10)):
                for row in range(int(MAP_HEIGHT / 10)):
                    # calculates the endpoint of the line based on the noise value at that point
                    line_endpoint_x = row + math.cos(noise_map[row][col] * math.pi)
                    line_endpoint_y = col + math.sin(noise_map[row][col] * math.pi)

                    # draws the line on the screen, color black, starting at row/col and ending at the newly calculated endpoint
                    pygame.draw.line(screen, pygame.Color('black'), (10 * row, 10 * col), (10 * line_endpoint_x, 10 * line_endpoint_y))
                    pygame.draw.circle(screen, pygame.Color('red'), (10 * row, 10 * col), 1)

            # updates the display
            pygame.display.flip()
            
            # increases the z_off, meaning the next "slice" of the noisemap will be taken at a slightly different location
            z_off += 0.2

            # resets delta_time
            delta_time = 0

        #records the time the loop ended
        end = time.perf_counter()
