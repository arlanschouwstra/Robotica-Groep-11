import pygame
import ax12 as x
import time
import RF


class Servo:

    def __init__(self):
        pygame.init()
        pygame.display.set_mode()

    # important! make sure the result position is not less than 0
    # method not used but could be of use
    @staticmethod
    def move_degree(servo, start_position, degree, clockwise):
        y = x.Ax12()
        if degree == 90:
            if clockwise:
                y.moveSpeed(servo, (start_position - 312), 50)
            else:
                y.moveSpeed(servo, (start_position + 312), 50)
        else:
            get_degree = 90 / degree
            if clockwise:
                y.moveSpeed(servo, (start_position - (312 / get_degree)), 50)
            else:
                y.moveSpeed(servo, (start_position - (312 / get_degree)), 50)
        print("moving servo: ", servo, "at", degree, "degrees")

    @staticmethod
    def reset_servos(id, start_position):
        y = x.Ax12()
        # set servos to their start positions
        y.moveSpeed(id, start_position, 50)
        # print servos positions (for testing purposes)
        print(y.readPosition(id))

    @staticmethod
    def get_speed(joystick):
        if joystick < 510:
            return 514 - joystick   # 514 as start position of joystick

        elif joystick > 520:
            return joystick - 514   # 514 as start position of joystick

    # moving the given servo forward or backward on button press
    def move(self, event, servo_id, start_position, clockwise, body, vertical):
        y = x.Ax12()
        rf = RF()

        # initialize each position of the joystick
        if rf.get_YL_position() > 520:      # move up
            if body:
                if vertical:
                    y.moveSpeed(servo_id, start_position, self.get_speed(rf.get_YL_position()))
                    print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_YL_position() < 510:      # move down
            if body:
                if vertical:
                    if not clockwise:
                        y.moveSpeed(servo_id, start_position + 200, self.get_speed(rf.get_YL_position()))
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))
                    else:
                        y.moveSpeed(servo_id, start_position - 200, self.get_speed(rf.get_YL_position()))
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_XL_position() < 510:      # move left
            if body:
                if not vertical:
                    y.moveSpeed(servo_id, start_position + 200, self.get_speed(rf.get_XL_position()))
                    print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_XL_position() > 520:      # move right
            if body:
                if not vertical:
                    y.moveSpeed(servo_id, start_position - 200, self.get_speed(rf.get_XL_position()))
                    print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_XR_position() < 510:      # move left head
            if not body:
                if not vertical:
                    if clockwise:
                        y.moveSpeed(servo_id, start_position + 200, self.get_speed(rf.get_XR_position()))
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_XR_position() > 520:      # move right head
            if not body:
                if not vertical:
                    if clockwise:
                        y.moveSpeed(servo_id, start_position - 200, self.get_speed(rf.get_XR_position()))
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_YR_position() > 520:      # move up head
            if not body:
                if not vertical:
                    if not clockwise:
                        y.moveSpeed(servo_id, start_position + 200, self.get_speed(rf.get_YR_position()))
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        if rf.get_YR_position() < 510:      # move down head
            if not body:
                if not vertical:
                    if not clockwise:
                        y.moveSpeed(servo_id, start_position - 200, self.get_speed(rf.get_YR_position()))
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

    # calling the servos to move
    def run_servos(self):

        # initialize servos
        start_positions = [[3, 200, True, True, True],      # right under for up/down
                           [4, 500, False, False, False],   # top servo
                           [6, 500, False, False, False],
                           [15, 823, False, True, True],
                           [23, 823, True, True, True],
                           [41, 500, True, True, False],    # left under for up/down
                           [51, 823, True, False, False]]

        while True:
            for servo in start_positions:
                self.reset_servos(servo[0], servo[1])
            for event in pygame.event.get():
                for servo in start_positions:
                        self.move(event, servo[0], servo[1], servo[2],  servo[3], servo[4])
