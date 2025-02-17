from config import *

class Debug():
    def printf(format_string, *args):
        if DEBUG_MODE == False:
            return
        format_string = format_string.replace("%d", "{}").replace("%f", "{}").replace("%s", "{}")
        try:
            formatted_string = format_string.format(*args)
            print(formatted_string)
        except Exception as e:
            print(f"Format Error: {e}")