from Resources import colors

# width/height of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# the color of the background
BG_COLOR = colors.WHITE

# how zoomed into the noise map to be (20 works well for simplex, 30 for perlin)
SCALE = 20

# 1 for perlin, 2 for simplex
NOISE_TYPE = 2

# how many particles to render 
NUM_PARTICLES = 1000

# whether the vectors should be drawn
DRAW_VECTORS = False

# whether the particles should be drawn
DRAW_PARTICLES = True

# affects how the particle move. 0.55 for choppy movements (like on a circuit board), 0.85 for smooth curvy flowing
VELOCITY_MULTIPLIER = 0.85

# changes the line thickness
LINE_THICKNESS = 1

# the color of the path drawn by the particle
PATH_COLOR = colors.BLACK

# whether the origin circle should be drawn
DRAW_ORIGIN_CIRCLE = False
# the radius of the origin circle
ORIGIN_CIRCLE_RADIUS = 4
# the color of the origin circle
ORIGIN_CIRCLE_COLOR = colors.BLACK

# whether the origin rectangle should be drawn
DRAW_ORIGIN_RECTANGLE = False
# the width of the origin rectangle
ORIGIN_RECTANGLE_WIDTH = 6
# the color of the origin rectangle
ORIGIN_RECTANGLE_COLOR = colors.BLACK

# changes the increment between consecutive noise layers in the z-axis (0 for no change, 0.001 for a nice and gradual change)
Z_INCREMENT = 0.001

# multiplier for the acceleration values for the particles (think of it like the strength of the wind)
MAGNITUDE = 1