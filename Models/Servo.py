'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Edited by:      Thijs Zijlstra
Version:        3.2
Description:    Servos
'''

import ax12 as x
import time


class Servo:
    """_______VARIABLES__________"""
    y = x.Ax12()

    def __init__(self):
        self.time = time
        pass

    # important! make sure the result position is not less than 0
    # method not used but could be of use
    def move_degree(self, servo,
                    start_position,
                    degree,
                    clockwise):
        if clockwise:
            self.move_position(servo,
                               (start_position - (312 if degree == 90 else 312 / (90 / degree))),
                               50)
        else:
            self.move_position(servo,
                               (start_position + (312 if degree == 90 else 312 / (90 / degree))),
                               50)

        print("moving servo: ",
              servo,
              "at",
              degree,
              "degrees")

    def reset_servos(self):
        # set servos to their start positions
        self.move_position(3,  # id
                           512,  # position
                           50)  # speed
        self.move_position(4,
                           512,
                           50)
        self.move_position(6,
                           200,
                           50)
        self.move_position(15,
                           512,
                           50)
        self.move_position(23,
                           512,
                           50)
        self.move_position(41,
                           512,
                           50)
        self.move_position(51,
                           512,
                           50)

        #already in the unit test. We should run the test on every boot.
        # print servos positions (for testing purposes)
        # print(self.y.readPosition(3))
        # print(self.y.readPosition(4))
        # print(self.y.readPosition(6))
        # print(self.y.readPosition(15))
        # print(self.y.readPosition(23))
        # print(self.y.readPosition(51))
        # print(self.y.readPosition(41))

    # old method to determine speed of the sensitivity for the joystick
    @staticmethod
    def get_speed(joystick, data):
        pass

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

    def move_all_servos(self, data):
        # initialize servos
        # start_positions = [[3, 512, True, True, True],  # right under for up/down
        #                    [4, 512, False, False, False],  # top servo
        #                    [6, 200, False, False, False],
        #                    [15, 512, False, True, True],
        #                    [23, 512, False, True, True],
        #                    [41, 512, True, True, False],  # left under for up/down
        #                    [51, 812, True, False, False]]

        if 'lx' in data:
            self.move(data["lx"], 41, 512, True, False)
        if 'ly' in data:
            self.move(data["ly"], 3, 512, True, True)
            self.move(data["ly"], 15, 512, False, True)
            self.move(data["ly"], 23, 512, False, True)
        if 'rx' in data:
            self.move(data["rx"], 6, 200, False, False)
        if 'ry' in data:
            self.move(data["ry"], 51, 512, True, False)

            # self.move(data, servos[0], servos[1], servos[2], servos[3], servos[4])

    def move_position(self, servo_id, position, speed):  # for easy usage in other classes
        self.y.moveSpeed(servo_id, position, speed)

    def read_position(self, servo_id):  # for easy usage in other classes
        return self.y.readPosition(servo_id)
