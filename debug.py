from config import *

class Debug():
    def print(*args, **kwargs):
        if DEBUG_MODE == True: 
            print(*args, **kwargs)
            
DEBUG_MODE = True            