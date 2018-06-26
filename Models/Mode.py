'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Version:        1.0
Description:    Change modes
'''

import ax12 as x
import Servo
from LineDetection import LineDetection

class Mode:
    y = x.Ax12()
    servo = Servo.Servo()

    def __init__(self):
        self.md = 0
        pass

    def init_modes(self, key, value):
        """__________________DRIVING MODE_______________"""
        if self.md == '0':
            self.servo.reset_servos()            # go to the start position(maybe not needed to call this every time)
            self.servo.move_all_servos(key, value)

        """_________________DANCING MODE_________________"""
        if self.md == '3':
            string = self.ser.readline()
            lowValue = string[1]
            middleValue = string[2]
            highValue = string[3]

        """________________LINE DANCE MODE_______________"""
        if self.md == '1':
            pass

        """________________LINE DETECTION________________"""
        if self.md == '4':
            LineDetection().send_value_canon()

        """_____________TRANSPORT AND REBUILD____________"""
        if self.md == '5':
            pass                # kinematics and Camera here
    def change_mode(self, value):
        self.md = value
