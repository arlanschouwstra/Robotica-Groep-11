import pygame
import ax12 as x


class Servo:

    def __init__(self):
        pygame.init()
        pygame.display.set_mode()

    def move(self, id):                     # moving the given servo forward or backward on button press
        y = x.Ax12()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:    # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 1000)
                    if event.key == pygame.K_DOWN:  # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 2000)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:    # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 0)
                    if event.key == pygame.K_DOWN:  # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 0)


# call method for class:
servo = Servo()

servo.move(17)
