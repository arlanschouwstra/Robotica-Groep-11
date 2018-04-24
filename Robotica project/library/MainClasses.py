class Servo:
    import RPi.GPIO as GPIO

    def __init__(self, pin):

        # define the pin for the servo
        self.pin = pin

        # setup the pin for output
        GPIO.setup(pin, GPIO.OUT)
        pass

    # move the servo to a given position
    def move(self, position):
        GPIO.output(self.pin, position)
        pass

    def rotate(self):
        pass

    def forward(self):
        pass

    def backwards(self):
        pass


class Network:
    def __init__(self):
        pass

    def configure(self):
        pass


class BluetoothController:
    def __init__(self):
        pass

    def configure(self):
        pass


class Leg:
    def __init__(self):
        pass

    def move_forward(self):
        pass

    def move_backwards(self):
        pass

    def rotate(self):
        pass

    def get_position(self):
        pass

    def set_position(self):
        pass


class Lights:
    def __init__(self):
        pass

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Camera:
    def __init__(self):
        pass

    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def reset(self):
        pass

    def detect_objects(self):
        pass


class Dance:
    def __init__(self):
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


class Emotion:
    def movements(self):
        pass

    def sounds(self):
        pass


class Arm:
    def __init__(self):
        pass

    def grab(self):
        pass

    def rotate(self):
        pass

    def move_forward(self):
        pass

    def move_backwards(self):
        pass

    def get_position(self):
        pass

    def set_position(self):
        pass


class Build:
    def __init__(self):
        pass

    def configure_arms(self):
        pass

    def detect_blocks(self):
        pass
