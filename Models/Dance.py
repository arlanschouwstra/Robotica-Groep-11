import ax12 as x
import time

class Dance:

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
        y.moveSpeed(41, 600, speed)
        time.sleep(1)
        y.moveSpeed(41, 500, speed)
        time.sleep(1)
        y.moveSpeed(41, 400, speed)
        time.sleep(1)
        y.moveSpeed(41, 300, speed)
        time.sleep(1)
        #   move right
        y.moveSpeed(41, 400, speed)
        time.sleep(1)
        y.moveSpeed(41, 500, speed)
        time.sleep(1)
        y.moveSpeed(41, 600, speed)
        time.sleep(1)
        y.moveSpeed(41, 700, speed)

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

    def weaveRight(self, y):
        self.stretchBackward(y, 100)
        self.moveRight(y, 50)
        self.stretchForward(y, 50)
        self.moveLeft(y, 50)
        self.stretchBackward(y, 50)
        self.moveCenter(y, 50)

    def weaveLeft(self, y):
        self.stretchBackward(y, 100)
        self.moveLeft(y, 50)
        self.stretchForward(y, 50)
        self.moveRight(y, 50)
        self.stretchBackward(y, 50)
        self.moveCenter(y, 50)

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
        self.weaveLeft(y)

    def play_music(self):
        pass
