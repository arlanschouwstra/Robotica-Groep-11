import pygame
import ax12 as x
import time


class Servo:

    def __init__(self):
        pygame.init()
        pygame.display.set_mode()

    def move_forward(self, id):                     # moving the servo forward on button press
        y = x.Ax12()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:    # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 1000)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:    # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 0)

    def move_backward(self, id):                    # moving the servo backward on button press
        y = x.Ax12()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 2000)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:  # can be changed later for controller keys or joysticks
                        y.moveSpeed(id, 0, 0)
