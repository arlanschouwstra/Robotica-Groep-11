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
        while True:
            if self.ser.inWaiting() > 0:
                inputValue = self.ser.readline()
                print(inputValue)
                if inputValue.startswith('{beat: 8}') or inputValue.startswith('{beat: 7}'):
                    print('Bo0M!!')
                    if self.read_pos(1) >= 805:
                        self.move_serv(1, 612, 200)

                    if self.read_pos(1) <= 614:
                        self.move_serv(1, 812, 200)
                time.sleep(0.5)
    def move_serv(self, servo_id, position, speed):
        return self.move(servo_id, position, speed)


linedance = LineDance()
