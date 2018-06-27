'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Version:        3.2
Description:    Servos
'''

import ax12 as x
import time


class Servo:
    """_______VARIABLES__________"""
    y = x.Ax12()

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
        self.y.moveSpeed(7,  # id
                         512,  # position
                         50)  # speed
        self.y.moveSpeed(6,
                         512,
                         50)
        self.y.moveSpeed(9,
                         200,
                         50)
        self.y.moveSpeed(15,
                         512,
                         50)
        self.y.moveSpeed(1,
                         512,
                         50)

        # print servos positions (for testing purposes)
        print(self.y.readPosition(7))
        print(self.y.readPosition(9))
        print(self.y.readPosition(6))
        print(self.y.readPosition(1))

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
            if 45 > int(data[2:4]) > 40:  # move up body
                if body:
                    if vertical:
                        self.y.moveSpeed(servo_id,
                                         start_position,
                                         50)
                        print("Servo:",
                              servo_id,
                              "moved to position:",
                              self.y.readPosition(servo_id))

            elif 45 < int(data[2:4]) < 50:  # move down body
                if body:
                    if vertical:
                        if not clockwise:
                            self.y.moveSpeed(servo_id,
                                             start_position + 300,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))
                        else:
                            self.y.moveSpeed(servo_id,
                                             start_position - 300,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

            elif 15 > int(data[4:6]) > 10:  # move left body
                if body:
                    if not vertical:
                        self.y.moveSpeed(servo_id,
                                         start_position + 300,
                                         50)
                        print("Servo:",
                              servo_id,
                              "moved to position:",
                              self.y.readPosition(servo_id))

            elif 15 < int(data[4:6]) < 20:  # move right body
                if body:
                    if not vertical:
                        self.y.moveSpeed(servo_id,
                                         start_position - 300,
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
                                             start_position + 300,
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
                                             start_position - 300,
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
                                             start_position + 300,
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
                                             start_position - 300,
                                             50)
                            print("Servo:",
                                  servo_id,
                                  "moved to position:",
                                  self.y.readPosition(servo_id))

        except ValueError:
            print("Could not turn servo!!")

    def stop_all_servos(self):
        self.y.moveSpeed(7,
                         int(self.y.readPosition(7)),
                         1)
        self.y.moveSpeed(1,
                         int(self.y.readPosition(1)),
                         1)
        time.sleep(0.01)

    # used to call all servos
    def move_all_servos(self, data):
        # initialize servos
        start_positions = [[7, 512, False, True, True],  # right under for up/down
                           [1, 512, False, True, True]]

        for servos in start_positions:
            self.move(data, servos[0], servos[1], servos[2], servos[3], servos[4])

    def move_position(self, servo_id, position, speed):  # for easy usage in other classes
        self.y.moveSpeed(servo_id, position, speed)

    def read_position(self, servo_id):  # for easy usage in other classes
        return self.y.readPosition(servo_id)
