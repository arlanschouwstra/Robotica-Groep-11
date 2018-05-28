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
        # y.moveSpeed(3, )    # onder servo
        # y.moveSpeed(41, )   # onder servo tegen gesteld
        # y.moveSpeed(23, )   # midden servo
        # -------servos kop------
        # y.moveSpeed(15)     # 1e servo
        # y.moveSpeed(6)      # 2e servo
        # y.moveSpeed(4)      # 3e servo
        # time.sleep(1)       # used for sleep

    def play_music(self):
        pass
