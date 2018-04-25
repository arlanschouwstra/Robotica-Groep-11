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

