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

    def play_music(self):
        pass
