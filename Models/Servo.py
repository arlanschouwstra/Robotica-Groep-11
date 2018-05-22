import pygame
import ax12 as x
import time


class Servo:

    def __init__(self):
        pygame.init()
        pygame.display.set_mode()

    def reset_servos(self):
        y = x.Ax12()

        y.moveSpeed(15, 823, 50)
        y.moveSpeed(3, 200, 50)
        y.moveSpeed(23, 823, 50)
        y.moveSpeed(41, 500, 50)
        y.moveSpeed(51, 823, 50)
        y.moveSpeed(6, 512, 50)

        print(y.readPosition(6))
        print(y.readPosition(51))
        print(y.readPosition(41))
        print(y.readPosition(23))
        print(y.readPosition(15))
        print(y.readPosition(3))

    def move(self, id, cw_servo, event, start_position, body,
             vertical):  # moving the given servo forward or backward on button press
        y = x.Ax12()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # can be changed later for controller keys or joysticks
                if body:
                    if vertical:
                        y.moveSpeed(id, start_position, 100)
                        print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_DOWN:  # can be changed later for controller keys or joysticks
                if body:
                    if vertical:
                        if not cw_servo:
                            y.moveSpeed(id, start_position + 200, 100)
                            print("Servo:", id, "moved to position:", y.readPosition(id))
                        else:
                            y.moveSpeed(id, start_position - 200, 100)
                            print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_LEFT:  # can be changed later for controller keys or joysticks
                if body:
                    if not vertical:
                        y.moveSpeed(id, start_position + 200, 100)
                        print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_RIGHT:  # can be changed later for controller keys or joysticks
                if body:
                    if not vertical:
                        y.moveSpeed(id, start_position - 200, 100)
                        print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_a:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if cw_servo:
                            y.moveSpeed(id, start_position + 200, 100)
                            print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_d:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if cw_servo:
                            y.moveSpeed(id, start_position - 200, 100)
                            print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_w:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if not cw_servo:
                            y.moveSpeed(id, start_position + 200, 100)
                            print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.key == pygame.K_s:  # can be changed later for controller keys or joysticks
                if not body:
                    if not vertical:
                        if not cw_servo:
                            y.moveSpeed(id, start_position - 200, 100)
                            print("Servo:", id, "moved to position:", y.readPosition(id))

            if event.type == pygame.KEYUP:
                time.sleep(0.02)
                y.moveSpeed(id, y.readPosition(id), 100)

    def run_servos(self):
        servo = Servo()
        servo.reset_servos()

        while True:

            for event in pygame.event.get():
                servo.move(3, True, event, 200, True, True)
                servo.move(15, False, event, 200, True, True)
                servo.move(23, True, event, 823, True, True)
                servo.move(41, True, event, 500, True, False)
                servo.move(51, True, event, 823, False, False)
                servo.move(6, False, event, 512, False, False)


# call method for class:
servo = Servo()
servo.run_servos()
