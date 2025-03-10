from debug import *

#--- Global constants ---
try:
    import pygame
    from pygame.locals import *
except:
    print("No PyGame installation found!")

# scales
SPRITE_SCALE = 2
LIVES_SPRITE_SCALE = 3

# screen scale
NEW_SCREEN_SIZE = True

# cell size
'''
the w x h of the robot sprite is 8 x 11. 
the w x h of the cell appear to be twice that, 16 x 22. (same size)
'''
if NEW_SCREEN_SIZE == True:
    CELL_WIDTH  = 16
    CELL_HEIGHT = 22
else:
    CELL_WIDTH  = 16 - 4
    CELL_HEIGHT = 22 - 4    

# grid size
GRID_WIDTH  = 8 * 5       # 40
GRID_HEIGHT = 7 * 3 + 1   # 22

# screen/maze object dimensions
BORDERTHICKNESS = 20
WALLTHICKNESS = 8
MAZE_WIDTH  = GRID_WIDTH  * CELL_WIDTH   # original: 640
MAZE_HEIGHT = GRID_HEIGHT * CELL_HEIGHT  # original: 480
MAZE_XMIN = BORDERTHICKNESS + WALLTHICKNESS
MAZE_YMIN = BORDERTHICKNESS + WALLTHICKNESS
MAZE_XMAX = MAZE_XMIN + MAZE_WIDTH
MAZE_YMAX = MAZE_YMIN + MAZE_HEIGHT
BORDER_XMIN = BORDERTHICKNESS
BORDER_YMIN = BORDERTHICKNESS
BORDER_XMAX = BORDER_XMIN + WALLTHICKNESS + MAZE_WIDTH
BORDER_YMAX = BORDER_YMIN + WALLTHICKNESS + MAZE_HEIGHT
BORDER_HSEGMENT = int(MAZE_WIDTH/5)
BORDER_VSEGMENT = int(MAZE_HEIGHT/3)
SCREEN_WIDTH = BORDERTHICKNESS*2 + WALLTHICKNESS*2 + MAZE_WIDTH
SCREEN_HEIGHT = BORDERTHICKNESS*3 + WALLTHICKNESS*3 + MAZE_HEIGHT
MAZE_CENTERX = MAZE_XMIN + int(MAZE_WIDTH/2)
MAZE_CENTERY = MAZE_YMIN + int(MAZE_HEIGHT/2)

Debug.print("# MAZE_XMIN, YMIN = ", MAZE_XMIN, ', ', MAZE_XMIN)
Debug.print("# MAZE_XMAX, YMAX = ", MAZE_XMAX, ', ', MAZE_XMAX)
Debug.print("# SCREEN_WIDTH, HEIGHT  = ", SCREEN_WIDTH, ', ', SCREEN_HEIGHT)


# color constants
BLACK       = (  0,   0,   0)
WHITE       = (255, 255, 255)
GREEN       = (  0, 255,   0)
RED         = (255,   0,   0)
BLUE        = (  0,   0, 255)
YELLOW      = (255, 255,   0)
CYAN        = (  0, 255, 255)
PURPLE      = (255,   0, 255)
DARK_ORCHID = (153,  50, 204)
DARKYELLOW  = (128, 128,   0)
LIGHTSKYBLUE = (135, 206, 250)
GRAY        = (190, 190, 190)
BRIGHTBLUE  = (  0,  50, 255)
DEEPSKYBLUE = (  0, 191, 255)
LIGHTYELLOW = (255, 255, 224)
PALEGREEN   = (152, 251, 152)


# misc game constants
WALL_COLOR = BLUE
BULLETS_MAX = 6     # max bullets on screen
FPS = 30            # frames per second
FONT = 'freesansbold.ttf'
FONT_PATH = FONT
CAPTION = "PyBerzerk"
MAX_LIVES = 3
MIN_ROBOTS = 4
MAX_ROBOTS = 12
ROBOT_KILL_POINTS = 50
BONUS_LIFE_SCORE = 5000
PLAYER_COLOR = GREEN
PLAYER_RECT = (0, 0, 8, 17)
PLAYER_SPRITES = 24
ROBOT_RECT = (0, 0, 8, 11)
ROBOT_SPRITES = 15
LIVES_RECT = (0, 0, 8, 8)
OTTO_RECT = (0, 0, 8, 8)
OTTO_SPRITES = 5
ROBOTEXPLODE_RECT = (0, 0, 16, 16)
ROBOTEXPLODE_SPRITES = 2

# user define events
(SPAWN_OTTO, ROBOT_ACTIVE, PLAYER_EXIT, PLAYER_ELECTROCUTED, BONUS_POINTS, BONUS_LIFE, BLINK) = range(USEREVENT+1, USEREVENT+8)

# movement/shoot directions
(N, NE, E, SE, S, SW, W, NW) = range(8)


