import RPi.GPIO as GPIO
import unittest

"""Unit test for check if the light matrix can be turned on and off."""
class TestLight(unittest.TestCase):

    def turn_on(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        GPIO.output(self.pin, 1)
        self.assertEqual()
    def turn_off(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        GPIO.output(self.pin, 0)
        self.assertEqual()

if __name__ == '_light_':
    unittest.main()