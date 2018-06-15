'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Version:        3.2
Description:    Servos with bluetooth controller
'''

import ax12 as x
import time
import Bluetooth
import re
import serial


class Servo:
    """_______VARIABLES__________"""
    y = x.Ax12()
    bluetooth = Bluetooth.Bluetooth()
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    def __init__(self):
        pass

    # important! make sure the result position is not less than 0
    # method not used but could be of use
    def move_degree(self, servo,
                    start_position,
                    degree,
                    clockwise):
        if degree == 90:
            if clockwise:
                self.y.moveSpeed(servo,
                                 (start_position - 312),
                                 50)
            else:
                self.y.moveSpeed(servo,
                                 (start_position + 312),
                                 50)
        else:
            get_degree = 90 / degree
            if clockwise:
                self.y.moveSpeed(servo,
                                 (start_position - (312 / get_degree)),
                                 50)
            else:
                self.y.moveSpeed(servo,
                                 (start_position - (312 / get_degree)),
                                 50)

        print("moving servo: ",
              servo,
              "at",
              degree,
              "degrees")

    def reset_servos(self):

        # set servos to their start positions
        self.y.moveSpeed(3,  # id
                         512,  # position
                         50)  # speed
        self.y.moveSpeed(4,
                         512,
                         50)
        self.y.moveSpeed(6,
                         200,
                         50)
        self.y.moveSpeed(15,
                         512,
                         50)
        self.y.moveSpeed(23,
                         512,
                         50)
        self.y.moveSpeed(41,
                         512,
                         50)
        self.y.moveSpeed(51,
                         812,
                         50)

        # print servos positions (for testing purposes)
        print(self.y.readPosition(3))
        print(self.y.readPosition(4))
        print(self.y.readPosition(6))
        print(self.y.readPosition(15))
        print(self.y.readPosition(23))
        print(self.y.readPosition(51))
        print(self.y.readPosition(41))

    # old method to determine speed of the sensitivity for the joystick
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

    # moving the given servo forward or backward on button press
    # body, clockwise and vertical are booleans used for easy initialisations for the servos positions
    def move(self, data, servo_id, start_position, clockwise, body, vertical):

        # initialize each position of the joystick
        try:
            if 25 > int(data[6:8]) > 20:  # move up body
                if body:
                    if vertical:
                        self.y.moveSpeed(servo_id,
                                         start_position,
                                         50)
                        print("Servo:",
                              servo_id,
                              "moved to position:",
                              self.y.readPosition(servo_id))

            elif 25 < int(data[6:8]) < 30:  # move down body
                if body:
                    if vertical:
                        if not clockwise:
                            self.y.moveSpeed(servo_id,
                                             start_position + 200,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))
                        else:
                            self.y.moveSpeed(servo_id,
                                             start_position - 200,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

            elif 15 > int(data[4:6]) > 10:  # move left body
                if body:
                    if not vertical:
                        self.y.moveSpeed(servo_id,
                                         start_position + 200,
                                         50)
                        print("Servo:",
                              servo_id,
                              "moved to position:",
                              self.y.readPosition(servo_id))

            elif 15 < int(data[4:6]) < 20:  # move right body
                if body:
                    if not vertical:
                        self.y.moveSpeed(servo_id,
                                         start_position - 200,
                                         50)
                        print("Servo:",
                              servo_id,
                              "moved to position:",
                              self.y.readPosition(servo_id))

            elif 35 > int(data[0:2]) > 30:  # move left head
                if not body:
                    if not vertical:
                        if clockwise:
                            self.y.moveSpeed(servo_id,
                                             start_position + 200,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

            elif 35 < int(data[0:2]) < 40:  # move right head
                if not body:
                    if not vertical:
                        if clockwise:
                            self.y.moveSpeed(servo_id,
                                             start_position - 200,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

            elif 45 > int(data[2:4]) > 40:  # move up head
                if not body:
                    if not vertical:
                        if not clockwise:
                            self.y.moveSpeed(servo_id,
                                             start_position + 200,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

            elif 45 < int(data[2:4]) < 50:  # move down head
                if not body:
                    if not vertical:
                        if not clockwise:
                            self.y.moveSpeed(servo_id,
                                             start_position - 200,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

        except ValueError:
            print("Could not turn servo!!")

    # used to call all servos
    def move_all_servos(self, data):
        # initialize servos
        start_positions = [[3, 512, True, True, True],  # right under for up/down
                           [4, 512, False, False, False],  # top servo
                           [6, 200, False, False, False],
                           [15, 512, False, True, True],
                           [23, 512, False, True, True],
                           [41, 512, True, True, False],  # left under for up/down
                           [51, 812, True, False, False]]

        for servos in start_positions:
            self.move(data, servos[0], servos[1], servos[2], servos[3], servos[4])

    # create connection with bluetooth
    def init_modes(self, result, array):

        """__________________DRIVING MODE_______________"""
        if result[10:11] == '0':
            self.reset_servos()            # go to the start position(maybe not needed to call this every time)

            if result != array[len(array) - 3]:
                self.move_all_servos(result)

            elif result == '35451525000':  # if not stopped, stop all servos
                self.y.moveSpeed(3,
                                 int(self.y.readPosition(3)),
                                 1)
                self.y.moveSpeed(4,
                                 int(self.y.readPosition(4)),
                                 1)
                self.y.moveSpeed(6,
                                 int(self.y.readPosition(6)),
                                 1)
                self.y.moveSpeed(15,
                                 int(self.y.readPosition(15)),
                                 1)
                self.y.moveSpeed(23,
                                 int(self.y.readPosition(23)),
                                 1)
                self.y.moveSpeed(41,
                                 int(self.y.readPosition(41)),
                                 1)
                self.y.moveSpeed(51,
                                 int(self.y.readPosition(51)),
                                 1)
                self.time.sleep(0.01)

        """_________________DANCING MODE_________________"""
        if result[10:11] == '3':
            string = self.ser.readline()
            lowValue = string[1]
            middleValue = string[2]
            highValue = string[3]

    # calling the servos to move (only this needs to be called to run this code)
    def run_servos(self):
        self.bluetooth.bluetooth_connect()
