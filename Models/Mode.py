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
        pass

    def init_modes(self, value):
        """__________________DRIVING MODE_______________"""
        if value == '0':
            self.servo.reset_servos()            # go to the start position(maybe not needed to call this every time)

            if result != array[len(array) - 3]:
                self.servo.move_all_servos(result)

            elif result == '35451525000':  # if not stopped, stop all servos
                self.servo.stop_all_servos()

        """_________________DANCING MODE_________________"""
        if value == '3':
            string = self.ser.readline()
            lowValue = string[1]
            middleValue = string[2]
            highValue = string[3]

        """________________LINE DANCE MODE_______________"""
        if value == '1':
            pass

        """________________LINE DETECTION________________"""
        if value == '4':
            LineDetection().send_value_canon()

        """_____________TRANSPORT AND REBUILD____________"""
        if value == '5':
            pass                # kinematics and Camera here
