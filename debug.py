from config import *

class Debug():
    def print(*args, **kwargs):
        if DEBUG_PRINT_MODE == True: 
            print(*args, **kwargs)
            
DEBUG_PRINT_MODE = True
DEBUG_ROBOT_AI = False
DEBUG_HIDE_OTTO = False
DEBUG_MUTE_SOUND = False