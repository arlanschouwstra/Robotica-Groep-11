import RPi.GPIO as GPIO
import serial


class LineDetection:
    left_line_sensor = GPIO.input(31)
    right_line_sensor = GPIO.input(32)
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    def __init__(self):
        GPIO.setwanrnings(False)
        GPIO.setmode(GPIO.BCM)

    def read_sensors(self):
        print("left %s", self.left_line_sensor)
        print("right %s", self.right_line_sensor)

    def send_value_canon(self):
        while True:
            if self.left_line_sensor and self.right_line_sensor:
                print('driving straight...')
                self.ser.write('35451529004')
            if not self.left_line_sensor and self.right_line_sensor:
                print('turning right...')
                self.ser.write('35451925004')
            if self.left_line_sensor and not self.right_line_sensor:
                print('turning left...')
                self.ser.write('35451125004')

    def send_value_dance(self):
        while True:
            if not self.left_line_sensor and self.right_line_sensor:
                print('turning left..')
                self.ser.write('35451125004')
            if self.left_line_sensor and not self.right_line_sensor:
                print('turning right...')
                self.ser.write('35451925004')
