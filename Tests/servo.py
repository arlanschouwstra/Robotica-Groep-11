import Models.ax12 as x
import unittest

"""Unit test for check if the servo position can be set and read"""
class TestServo(unittest.TestCase):

    def test_position(self):
        y = x.Ax12()
        # vertical body
        y.moveSpeed(3, 512, 50)
        # vertical head
        y.moveSpeed(4, 512, 50)
        # horizontal head
        y.moveSpeed(6, 200, 50)
        y.moveSpeed(15, 512, 50)
        # vertical body middle joint
        y.moveSpeed(23, 812, 50)
        # horizontal body
        y.moveSpeed(41, 512, 50)
        # rotate head
        y.moveSpeed(51, 812, 50)

        self.assertEqual(y.readPosition(3), 512)
        self.assertEqual(y.readPosition(4), 512)
        self.assertEqual(y.readPosition(6), 200)
        self.assertEqual(y.readPosition(15), 512)
        self.assertEqual(y.readPosition(23), 812)
        self.assertEqual(y.readPosition(41), 512)
        self.assertEqual(y.readPosition(51), 812)

if __name__ == '_servo_':
    unittest.main()



