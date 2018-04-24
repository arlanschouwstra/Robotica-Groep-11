
# Illogical classes which should be functions

class Dance:
    def __init__(self):
        pass

    def begin(self):
        pass

    def end(self):
        pass
    
    def configure_legs(self):
        pass

    def detect_sound(self):
        pass

    def pirouette(self):
        pass

    def touch_line(self):
        pass

    def show_emotion(self):
        Emotion.movements()
        Emotion.sounds()
        pass


class Emotion:
    def __init__(self):
        pass

    def movements(self):
        pass

    def sounds(self):
        pass

    def lights(self):
       pass

class Build:
    def __init__(self):
        pass

    def configure_arms(self):
        pass

    def detect_blocks(self):
        pass

    def place_block(self, position):
        pass


class Move:
    def __init__(self):
        pass

    def legs(self, leg, position):
        pass

    def arm(self, arm, position):
        pass