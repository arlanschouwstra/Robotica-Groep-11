import ax12 as x
import time

class Dance:

    def set_start_position(self):
        # set library
        y = x.Ax12()

        # set servos to their start positions
        y.moveSpeed(15, 823, 50)
        y.moveSpeed(3, 200, 50)
        y.moveSpeed(23, 823, 50)
        y.moveSpeed(41, 512, 50)
        y.moveSpeed(51, 823, 50)
        y.moveSpeed(6, 512, 50)

    def twist(y):
        y.moveSpeed(6, 412, 100)    # turn far left
        time.sleep(1)
        y.moveSpeed(6, 612, 200)    # turn far right
        time.sleep(1)
        y.moveSpeed(6, 512, 100)    # turn back to start point
        time.sleep(1)

    def stretchForward(y):
        y.moveSpeed(3, 0, 200)
        y.moveSpeed(15, 1023, 200)
        y.moveSpeed(23, 823, 200)
        time.sleep(1)

    def stretchBackward(y):
        y.moveSpeed(3, 200, 200)
        y.moveSpeed(15, 823, 200)
        y.moveSpeed(23, 623, 200)
        time.sleep(1)

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

        # LETS DO THE TWIST
        for _ in xrange(10):
            self.twist(y)
            time.sleep(3)
            self.stretchForward(y)
            time.sleep(1)
            self.twist(y)
            time.sleep(3)
            self.stretchBackward(y)
            time.sleep(1)

    def play_music(self):
        pass
