import noise
import random
import pygame
import math
import time

from Particle import Particle
from Resources import colors, settings
RAND_X_OFFSET = random.randint(-100000, 100000)
RAND_Y_OFFSET = random.randint(-100000, 100000)

def get_noise(x_pos, y_pos, z_pos):
    if (settings.NOISE_TYPE == 1):
        return noise.pnoise3(RAND_X_OFFSET + (x_pos / settings.WINDOW_WIDTH * settings.SCALE), RAND_Y_OFFSET + (y_pos / settings.WINDOW_HEIGHT * settings.SCALE), z_pos) + 1
    elif (settings.NOISE_TYPE == 2):
        return noise.snoise3(RAND_X_OFFSET + (x_pos / settings.WINDOW_WIDTH * settings.SCALE), RAND_Y_OFFSET + (y_pos / settings.WINDOW_HEIGHT * settings.SCALE), z_pos) + 1

if __name__ == "__main__":
    pygame.display.init()
    
    # creates the screen
    screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT), pygame.SRCALPHA, 32)

    surface1 = pygame.Surface((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
    surface1.set_colorkey(colors.BLACK)
    surface1.set_alpha(100)
    
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

    particle_list = []


    screen.fill(colors.DARK_BLUE)
    surface1.fill(colors.BLACK)
    
    screen.blit(surface1, (0, 0))
    pygame.display.update()

    
    for i in range(settings.NUM_PARTICLES):
        particle_list.append(Particle.Particle(random.randint(0, settings.WINDOW_WIDTH), random.randint(0, settings.WINDOW_HEIGHT), screen))

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
        if (delta_time > 1 / 100):
            # generates a new slice of the noise map with the new z offset. In the future, maybe generate a 3 dimensional slice at the beginning for faster run times?
            noise_map = [[get_noise(x, y, z_off) for x in range(int(settings.WINDOW_WIDTH / 10))] for y in range(int(settings.WINDOW_HEIGHT / 10))]

            # clears the drawings of the previous frame
            #screen.fill(pygame.Color('white'))

            for part in particle_list:
                part.Update(noise_map)
                part.Draw(screen)

                

            # these loop through the grid and draw the vectors
            #for col in range(int(WINDOW_WIDTH / 10)):
                #for row in range(int(WINDOW_HEIGHT / 10)):
                    # calculates the endpoint of the line based on the noise value at that point
                    #line_endpoint_x = row + math.cos(noise_map[row][col] * math.pi)
                    #line_endpoint_y = col + math.sin(noise_map[row][col] * math.pi)

                    # draws the line on the screen, color black, starting at row/col and ending at the newly calculated endpoint
                    #pygame.draw.line(screen, pygame.Color('black'), (10 * row, 10 * col), (10 * line_endpoint_x, 10 * line_endpoint_y))
                    #pygame.draw.circle(screen, pygame.Color('red'), (10 * row, 10 * col), 1)


            # updates the display
            pygame.display.update()            
            
            # increases the z_off, meaning the next "slice" of the noise map will be taken at a slightly different location
            z_off += 0.0

            # resets delta_time
            delta_time = 0

        #records the time the loop ended
        end = time.perf_counter()

    pygame.quit()