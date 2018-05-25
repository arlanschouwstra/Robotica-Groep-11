import pygame
import ax12 as x
import time


class Servo:

    def __init__(self):
        pygame.init()
        pygame.display.set_mode()

    @staticmethod
    def reset_servos():
        y = x.Ax12()

        # set servos to their start positions
        y.moveSpeed(15, 823, 50)
        y.moveSpeed(3, 200, 50)
        y.moveSpeed(23, 823, 50)
        y.moveSpeed(41, 500, 50)
        y.moveSpeed(51, 823, 50)
        y.moveSpeed(6, 512, 50)

        # print servos positions (for testing purposes)
        print(y.readPosition(6))
        print(y.readPosition(51))
        print(y.readPosition(41))
        print(y.readPosition(23))
        print(y.readPosition(15))
        print(y.readPosition(3))

    # moving the given servo forward or backward on button press
    @staticmethod
    def move(event, servo_id, start_position, clockwise, body, vertical):
        y = x.Ax12()
        start_speed = 100

        # initialize each key what they need to do
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # can be changed later for controller keys or joysticks
                if body:
                    if vertical:
                        y.moveSpeed(servo_id, start_position, start_speed)
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_DOWN:  # can be changed later for controller keys or joysticks
                if body:
                    if vertical:
                        if not clockwise:
                            y.moveSpeed(servo_id, start_position + 200, start_speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))
                        else:
                            y.moveSpeed(servo_id, start_position - 200, start_speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_LEFT:  # can be changed later for controller keys or joysticks
                if body:
                    if not vertical:
                        y.moveSpeed(servo_id, start_position + 200, start_speed)
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_RIGHT:  # can be changed later for controller keys or joysticks
                if body:
                    if not vertical:
                        y.moveSpeed(servo_id, start_position - 200, start_speed)
                        print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_a:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if clockwise:
                            y.moveSpeed(servo_id, start_position + 200, start_speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_d:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if clockwise:
                            y.moveSpeed(servo_id, start_position - 200, start_speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_w:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if not clockwise:
                            y.moveSpeed(servo_id, start_position + 200, start_speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

            if event.key == pygame.K_s:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if not clockwise:
                            y.moveSpeed(servo_id, start_position - 200, start_speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

        # can be used to stop keys at current position if they are released
        if event.type == pygame.KEYUP:
            time.sleep(0.02)
            y.moveSpeed(servo_id, y.readPosition(servo_id), start_speed)

    # calling the servos to move
    def run_servos(self):
        self.reset_servos()

        # initialize servos
        start_positions = [[3, 200, True, True, True],
                           [4, 500, False, False, False],
                           [6, 500, False, False, False],
                           [15, 823, False, True, True],
                           [23, 823, True, True, True],
                           [41, 500, True, True, False],
                           [51, 823, True, False, False]]

        while True:
            for event in pygame.event.get():
                for servo in start_positions:
                        self.move(event, servo[0], servo[1], servo[2],  servo[3], servo[4])
