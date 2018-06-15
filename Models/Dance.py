import time
import Servo
import serial

class Dance:
    def __init__(self):
        self.move = getattr(Servo, 'move_position')
    #  for serial connection between Pi and Arduino.
    def connect_usb(self):
        ser = serial.Serial('/dev/ttyACM0', 9600)
        return ser

    def send_data(self, ser, data):
        ser.write(str(data))

    def receive_data(self, ser):
        return ser.readline()

    #   functions for driving
    def turn_left(self, ser, speed):
        ser.write("turnLeft"+","+str(speed))

    def turn_right(self, ser, speed):
        ser.write("turnRight"+","+str(speed))

    def move_forward(self, ser, speed):
        ser.write("moveForward"+","+str(speed))

    def move_backward(self, ser, speed):
        ser.write("moveBackward"+","+str(speed))

    def set_start_position(self, y):
        # set servos to their start positions
        self.move(15, 823, 50)
        self.move(3, 200, 50)
        self.move(23, 623, 50)
        self.move(41, 512, 50)
        self.move(51, 823, 50)
        self.move(6, 512, 50)

    def buildup_speed(self, y, idServo, distance, speed):    #TESTEN!!!
        start_speed = speed/2
        self.move(idServo,distance,start_speed)
        time.sleep(0.5)
        self.move(idServo, distance, speed)

    def headbang(self, y, speed):
        self.move(3, 100, speed)
        self.move(15, 923, speed)
        self.move(23, 623, speed)
        time.sleep(1)
        self.move(3, 200, speed)
        self.move(15, 823, speed)
        self.move(23, 723, speed)
        time.sleep(1)

    def twist(self, y, speed):
        self.move(6, 412, speed)    # turn far left
        time.sleep(1)
        self.move(6, 612, speed)    # turn far right
        time.sleep(1)

    def sprinkler_start(self, y, speed):
        self.move(3, 200, speed)
        self.move(15, 823, speed)
        self.move(23, 723, speed)
        self.move_right(y, speed)

    def sprinkler(self, y, speed):
        self.sprinkler_start(y, speed)
        time.sleep(1)
        #   move left
        self.move(41, 600, speed/2)
        time.sleep(1)
        self.move(41, 500, speed/2)
        time.sleep(1)
        self.move(41, 400, speed/2)
        time.sleep(1)
        self.move(41, 300, speed/2)
        time.sleep(1)
        #   move right
        self.move(41, 400, speed/2)
        time.sleep(1)
        self.move(41, 500, speed/2)
        time.sleep(1)
        self.move(41, 600, speed/2)
        time.sleep(1)
        self.move(41, 700, speed/2)

    def stretch_forward(self, y, speed):
        self.move(3, 0, speed)
        self.move(15, 1023, speed)
        self.move(23, 823, speed)

    def stretch_backward(self, y, speed):
        self.move(3, 200, speed)
        self.move(15, 823, speed)
        self.move(23, 623, speed)

    def move_left(self, y, speed):
        self.move(41, 400, speed)

    def move_right(self, y, speed):
        self.move(41, 600, speed)

    def move_center(self, y, speed):
        self.move(41, 500, speed)

    def weave_right(self, y, speed):
        self.stretch_backward(y, speed)
        self.move_right(y, speed/2)
        self.stretch_forward(y, speed/2)
        self.move_left(y, speed/2)
        self.stretch_backward(y, speed/2)
        self.move_center(y, speed/2)

    def weave_left(self, y, speed):
        self.stretch_backward(y, speed)
        self.move_left(y, speed/2)
        self.stretch_forward(y, speed/2)
        self.move_right(y, speed/2)
        self.stretch_backward(y, speed/2)
        self.move_center(y, speed/2)

    def start(self):
        # (naam,beweging,snelheid)
        # -------onder servos lichaam-------
        # self.move(3, )    # onder servo                 (0: max down, 200: max up)
        # self.move(15, )   # onder servo tegen gesteld   (1023: max down, 823 max up)
        # self.move(23, )   # midden servo                (623: max down, 823:max up)
        # self.move(41, )   # servo vertical              (300: max left, 700: max right)
        # -------servos kop------

        # self.move(6)      # 2e servo                    (300: max left, 700: max right)
        # self.move(4)      # 3e servo                    (300: max left, 700: max right)
        # time.sleep(1)       # used for sleep
        # y = x.Ax12()
        self.set_start_position(y)

        ser = self.connect_usb()
        self.send_data(ser, "display_group_name")
