
class Light:
    import RPi.GPIO as GPIO

    def __init__(self, pin):
        # define the pin for the lights
        self.pin = pin

        # setup the pin for output
        GPIO.setup(pin, GPIO.OUT)
        pass

    def sync_with_sound(self):
        pass


def turn_on(self):
    GPIO.output(self.pin, 1)
    pass


def turn_off(self):
    GPIO.output(self.pin, 0)
    pass
