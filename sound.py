class Sound:
    def __init__(self):
        """
        0: player fired laser
        1: robot fired laser
        2: player is destroyed
        3: robot is destroyed
        
        4: player entered room
        5: player is exiting room
        6: in game

        00: attack it
        01: attack the humanoid
        02: charge it
        03: chicken fight like a robot
        04: destroy it
        05: destroy the intruder
        06: get the chicken
        07: get the intruder
        08: got the humanoid got the intruder
        09: intruder alert intruder alert
        10: kill the intruder
        11: shoot it
        12: the humanoid must not escape
        13: the intruder must not escape
        """
        
        self.mode = 0        
        self.sound = 0
       
    def play(self, mode, sound):
        self.mode = mode
        self.sound = sound