# -*- coding: utf-8 -*-
from pi_switch import RCSwitchReceiver
import re
import ax12 as x


class RF:
    receiver = RCSwitchReceiver()
    receiver.enableReceive(2)
    value_xl = 5
    value_yl = 5
    value_xr = 5
    value_yr = 5

    def regex(self, value):
        regex = re.search(r"(.)(.)(.)(.)", str(value))
        print(regex.group(1))
        self.value_xl = regex.group(1)
        self.value_yl = regex.group(2)
        self.value_xr = regex.group(3)
        self.value_yr = regex.group(4)

    # for test purposes
    def receive(self):

        while True:

            if self.receiver.available():
                received_value = self.receiver.getReceivedValue()

                if received_value:
                    print(received_value)
                    self.regex_xl(received_value)
                    print(self.value_xl)

                self.receiver.resetAvailable()

    @staticmethod
    def get_speed(joystick):
        # ______to the right________#
        if joystick == 1:
            return 200
        if joystick == 2:
            return 150
        if joystick == 3:
            return 100
        if joystick == 4:
            return 50
        # _______to the left_________#
        if joystick == 6:
            return 50
        if joystick == 7:
            return 100
        if joystick == 8:
            return 150
        if joystick == 9:
            return 200

    def move(self):  # hard coded moves for controller
        y = x.Ax12()

        while True:
            if self.receiver.available():
                received_value = self.receiver.getReceivedValue()

                if received_value:
                    speed = self.get_speed(received_value)
                    regex(received_value)

                    if value_xl < 5:
                        y.moveSpeed(41, startPosition + 300, speed)

                    elif value_xl > 5:
                        y.moveSpeed(41, startPosition - 300, speed)

                    else:
                        y.moveSpeed(41, y.readPosition(41), speed)

                    if value_yl < 5:
                        y.moveSpeed(3, startPosition, speed)
                        y.moveSpeed(15, startPosition, speed)
                        y.moveSpeed(23, startPosition, speed)

                    elif value_yl > 5:
                        y.moveSpeed(3, startPosition - 200, speed)
                        y.moveSpeed(15, startPosition + 200, speed)
                        y.moveSpeed(23, startPosition - 200, speed)

                    else:
                        y.moveSpeed(3, y.readPosition(3), speed)
                        y.moveSpeed(15, y.readPosition(15), speed)
                        y.moveSpeed(23, y.readPosition(23), speed)

                    if value_xr < 5:
                        y.moveSpeed(6, startPosition6 + 200, speed)

                    elif value_xr > 5:
                        y.moveSpeed(6, startPosition6 - 200, speed)

                    else:
                        y.moveSpeed(6, y.readPosition(6), speed)

                    if value_yr < 5:
                        y.moveSpeed(6, startPosition6 + 200, speed)

                    elif value_yr > 5:
                        y.moveSpeed(6, startPosition6 - 200, speed)

                    else:
                        y.moveSpeed(6, y.readPosition(6), speed)

                self.receiver.resetAvailable()


rf = RF()

rf.receive()


