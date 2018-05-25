import ax12 as x


class Dance:

    def set_start_position(self):
        # set library
        y = x.Ax12()

        # set servos to their start positions
        y.moveSpeed(15, 823, 50)
        y.moveSpeed(3, 200, 50)
        y.moveSpeed(23, 823, 50)
        y.moveSpeed(41, 500, 50)
        y.moveSpeed(51, 823, 50)
        y.moveSpeed(6, 512, 50)

    def start(self):
        self.set_start_position()
        self.play_music()

        

    def play_music(self):
        pass
