'''
Date:           03-08-2018
Creator:        Thijs Zijlstra
Version:        3.2
Description:    Unit tests servo
'''
from Models import Servo
import unittest

"""Unit test for check if the servo position can be set and read"""
class TestServo(unittest.TestCase):

    def test_position(self):
        move = getattr(Servo, 'move_position')
        read = getattr(Servo, 'read_position')
        move(3, 512, 50)
        # vertical body
        move(3, 512, 50)
        # vertical head
        move(4, 512, 50)
        # horizontal head
        move(6, 200, 50)
        move(15, 512, 50)
        # vertical body middle joint
        move(23, 812, 50)
        # horizontal body
        move(41, 512, 50)
        # rotate head
        move(51, 812, 50)

        self.assertEqual(read(3), 512)
        self.assertEqual(read(4), 512)
        self.assertEqual(read(6), 200)
        self.assertEqual(read(15), 512)
        self.assertEqual(read(23), 812)
        self.assertEqual(read(41), 512)
        self.assertEqual(read(51), 812)

if __name__ == '_servo_':
    unittest.main()



