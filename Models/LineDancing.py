import serial
from Servo import Servo
import time

class LineDance():
    def __init__(self):
        self.servo = Servo()
        self.move = getattr(self.servo, 'move_position')
        self.read_pos = getattr(self.servo, 'read_position')
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        self.detect()

    def detect(self):
        is_running_612 = False  # type: bool
        is_running_812 = False  # type: bool

        while True:
            if self.ser.inWaiting() > 0:
                input_value = self.ser.readline()
                print(input_value)

                if input_value.startswith('{beat: 8}'):
                    print('Bo0M!!')
                    if self.read_pos(1) >= 810 and not is_running_612:
                        self.move_serv(1, 612, 200)
                        is_running_812 = False
                        is_running_612 = True

                    elif self.read_pos(1) <= 614 and not is_running_812:
                        self.move_serv(1, 812, 200)
                        is_running_812 = True
                        is_running_612 = False

    def move_serv(self, servo_id, position, speed):
        return self.move(servo_id, position, speed)


linedance = LineDance()
