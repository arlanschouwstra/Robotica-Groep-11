import ax12 as x
import time
import pyfirmata

#board = pyfirmata.Arduino('/dev/ttyACM0')

#iter8 = pyfirmata.util.Iterator(board)
#iter8.start()
#check_sound = board.get_pin('d:5:o')    #   .read this variable for a change when music has started, to start dance sequence.
#start_dance = board.get_pin('d:7:o')    #   pin where leds are connected (first dance bit uses these)
##   code for wheels.
#motor_left = board.get_pin('d:3:p')
#motor_right = board.get_pin('d:4:p')
#STEPS = 10000.0
#if joystick_left == 1:
#    for i in range(int(STEPS)):
#            print i
#            motor_left.write(i / STEPS)  # hardware-PWM accepts values 0.0 ... 1.0
#            time.sleep(0.001)
#
#if joystick_right == 1:
#    for i in range(int(STEPS)):
#            print i
#            motor_left.write(i / STEPS)  # hardware-PWM accepts values 0.0 ... 1.0
#            time.sleep(0.001)

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

    def play_music(self):
        pass
