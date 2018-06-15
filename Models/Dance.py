import ax12 as x
import time
import serial

class Dance:
    # for serial connection between Pi and Arduino.
    ser = serial.Serial('/dev/ttyACM0', 9600)

    #   functions for driving
    def turnLeft(self, speed):
        ser.write("turnLeft"+","+str(speed))

    def turnRight(self, speed):
        ser.write("turnRight"+","+str(speed))

    def moveForward(self, speed):
        ser.write("moveForward"+","+str(speed))

    def moveBackward(self, speed):
        ser.write("moveBackward"+","+str(speed))

    def set_start_position(self):
        # set library
        y = x.Ax12()

        # set servos to their start positions
        y.moveSpeed(15, 823, 50)
        y.moveSpeed(3, 200, 50)
        y.moveSpeed(23, 623, 50)
        y.moveSpeed(41, 512, 50)
        y.moveSpeed(51, 823, 50)
        y.moveSpeed(6, 512, 50)

    def buildUpSpeed(self, y, idServo, distance, speed):    #TESTEN!!!
        startSpeed = speed/2
        y.moveSpeed(idServo,distance,startSpeed)
        time.sleep(0.5)
        y.moveSpeed(idServo, distance, speed)

    def headbang(self, y, speed):
        y.moveSpeed(3, 100, speed)
        y.moveSpeed(15, 923, speed)
        y.moveSpeed(23, 623, speed)
        time.sleep(1)
        y.moveSpeed(3, 200, speed)
        y.moveSpeed(15, 823, speed)
        y.moveSpeed(23, 723, speed)
        time.sleep(1)

    def twist(self, y, speed):
        y.moveSpeed(6, 412, speed)    # turn far left
        time.sleep(1)
        y.moveSpeed(6, 612, speed)    # turn far right
        time.sleep(1)

    def sprinklerStart(self, y, speed):
        y.moveSpeed(3, 200, speed)
        y.moveSpeed(15, 823, speed)
        y.moveSpeed(23, 723, speed)
        self.moveRight(y, speed)

    def sprinkler(self, y, speed):
        self.sprinklerStart(y, speed)
        time.sleep(1)
        #   move left
        y.moveSpeed(41, 600, speed/2)
        time.sleep(1)
        y.moveSpeed(41, 500, speed/2)
        time.sleep(1)
        y.moveSpeed(41, 400, speed/2)
        time.sleep(1)
        y.moveSpeed(41, 300, speed/2)
        time.sleep(1)
        #   move right
        y.moveSpeed(41, 400, speed/2)
        time.sleep(1)
        y.moveSpeed(41, 500, speed/2)
        time.sleep(1)
        y.moveSpeed(41, 600, speed/2)
        time.sleep(1)
        y.moveSpeed(41, 700, speed/2)

    def stretchForward(self, y, speed):
        y.moveSpeed(3, 0, speed)
        y.moveSpeed(15, 1023, speed)
        y.moveSpeed(23, 823, speed)

    def stretchBackward(self, y, speed):
        y.moveSpeed(3, 200, speed)
        y.moveSpeed(15, 823, speed)
        y.moveSpeed(23, 623, speed)

    def moveLeft(self, y, speed):
        y.moveSpeed(41, 400, speed)

    def moveRight(self, y, speed):
        y.moveSpeed(41, 600, speed)

    def moveCenter(self, y, speed):
        y.moveSpeed(41, 500, speed)

    def weaveRight(self, y, speed):
        self.stretchBackward(y, speed)
        self.moveRight(y, speed/2)
        self.stretchForward(y, speed/2)
        self.moveLeft(y, speed/2)
        self.stretchBackward(y, speed/2)
        self.moveCenter(y, speed/2)

    def weaveLeft(self, y, speed):
        self.stretchBackward(y, speed)
        self.moveLeft(y, speed/2)
        self.stretchForward(y, speed/2)
        self.moveRight(y, speed/2)
        self.stretchBackward(y, speed/2)
        self.moveCenter(y, speed/2)

    def start(self):
        self.set_start_position()
        self.play_music()
        # (naam,beweging,snelheid)
        # -------onder servos lichaam-------
        # y.moveSpeed(3, )    # onder servo                 (0: max down, 200: max up)
        # y.moveSpeed(15, )   # onder servo tegen gesteld   (1023: max down, 823 max up)
        # y.moveSpeed(23, )   # midden servo                (623: max down, 823:max up)
        # y.moveSpeed(41, )   # servo vertical              (300: max left, 700: max right)
        # -------servos kop------

        # y.moveSpeed(6)      # 2e servo                    (300: max left, 700: max right)
        # y.moveSpeed(4)      # 3e servo                    (300: max left, 700: max right)
        # time.sleep(1)       # used for sleep
        y = x.Ax12()
        self.weaveLeft(y, 100)
