'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Edited by:      Thijs Zijlstra
Version:        3.2
Description:    Servos
'''

import math
from pyax12.connection import Connection
import ax12 as x
import time


class Servo:
    """_______VARIABLES__________"""
    y = x.Ax12()

    def __init__(self):
        self.time = time
        self.serial_connection = Connection(port="/dev/ttyAMA0", rpi_gpio=True)
        pass

    # important! make sure the result position is not less than 0
    # method not used but could be of use
    def move_degree(self, servo,
                    start_position,
                    degree,
                    clockwise):
        if clockwise:
            self.serial_connection.goto(servo, (start_position - (312 if degree == 90 else 312 / (90 / degree))), speed=512,
                                   degrees=True)

        else:
            self.serial_connection.goto(servo, start_position + (312 if degree == 90 else 312 / (90 / degree)), speed=512,
                                   degrees=True)

            # self.move_position(servo,
            #                    (start_position + (312 if degree == 90 else 312 / (90 / degree))),
            #                    50)

        print("moving servo: ",
              servo,
              "at",
              degree,
              "degrees")

    def reset_servos(self):
        # set servos to their start positions
        self.serial_connection.goto(3, 180, speed=50,
                                    degrees=True)
        self.serial_connection.goto(4, 180, speed=50,
                                    degrees=True)
        self.serial_connection.goto(6, 180, speed=50,
                                    degrees=True)
        self.serial_connection.goto(15, 180, speed=50,
                                    degrees=True)
        self.serial_connection.goto(23, 180, speed=50,
                                    degrees=True)
        self.serial_connection.goto(41, 180, speed=50,
                                    degrees=True)
        self.serial_connection.goto(51, 180, speed=50,
                                    degrees=True)

    # moving the given servo forward or backward on button press
    # body, clockwise and vertical are booleans used for easy initialisations for the servos positions
    def move(self, data, servo_id, start_position, clockwise, body):
        # initialize each position of the joystick
        if 15 > data > 10:
            if clockwise:
                if body:
                    self.move_position(servo_id, start_position, 50)
                else:
                    self.move_position(servo_id, start_position - 300, 50)

            if not clockwise:
                if body:
                    self.move_position(servo_id, start_position, 50)
                else:
                    self.move_position(servo_id, start_position + 300, 50)

        if 15 < data < 20:
            if clockwise:
                self.move_position(servo_id, start_position + 300, 50)

            if not clockwise:
                self.move_position(servo_id, start_position - 300, 50)

    def stop_all_servos(self):
        self.move_position(3,
                           int(self.y.readPosition(3)),
                           1)
        self.move_position(4,
                           int(self.y.readPosition(4)),
                           1)
        self.move_position(6,
                           int(self.y.readPosition(6)),
                           1)
        self.move_position(15,
                           int(self.y.readPosition(15)),
                           1)
        self.move_position(23,
                           int(self.y.readPosition(23)),
                           1)
        self.move_position(41,
                           int(self.y.readPosition(41)),
                           1)
        self.move_position(51,
                           int(self.y.readPosition(51)),
                           1)
        time.sleep(0.01)

    def move_all_servos(self, key, data):
        # initialize servos
        # start_positions = [[3, 512, True, True, True],  # right under for up/down
        #                    [4, 512, False, False, False],  # top servo
        #                    [6, 200, False, False, False],
        #                    [15, 512, False, True, True],
        #                    [23, 512, False, True, True],
        #                    [41, 512, True, True, False],  # left under for up/down
        #                    [51, 812, True, False, False]]

        if 'lx' == key:
            self.move(data, 41, 512, True, False)
        if 'ly' == key:
            self.move(data, 3, 512, True, True)
            self.move(data, 15, 512, False, True)
            self.move(data, 23, 512, False, True)
        if 'rx' == key:
            self.move(data, 6, 200, False, False)
        if 'ry' == key:
            self.move(data, 51, 512, True, False)

            # self.move(data, servos[0], servos[1], servos[2], servos[3], servos[4])

    def move_position(self, servo_id, position, speed):  # for easy usage in other classes

        self.serial_connection.goto(servo_id,  math.floor(position/2.844444), speed=speed,
                                    degrees=True)
        # self.y.moveSpeed(servo_id, position, speed)

    def read_position(self, servo_id):  # for easy usage in other classes
        return self.serial_connection.present_position(servo_id)
        # return self.y.readPosition(servo_id)

