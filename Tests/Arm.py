'''
Date:           03-08-2018
Creator:        Thijs Zijlstra
Version:        3.2
Description:    Arm inverse kinematics
'''
import numpy as np
from Models import Arm
import unittest

"""Unit test for arm inverse kinematics"""

class TestArm(unittest.TestCase):

    def test(self):

      arm = Arm.Arm3Link()

      # set of desired (x,y) hand positions
      x = np.arange(-.75, .75, .05)
      y = np.arange(.25, .75, .05)

      # threshold for printing out information, to find trouble spots
      thresh = .025

      count = 0
      total_error = 0
      # test it across the range of specified x and y values
      for xi in range(len(x)):
          for yi in range(len(y)):
              # test the inv_kin function on a range of different targets
              xy = [x[xi], y[yi]]
              # run the inv_kin function, get the optimal joint angles
              q = arm.inv_kin(xy=xy)
              # find the (x,y) position of the hand given these angles
              actual_xy = arm.get_xy(q)
              # calculate the root squared error
              error = np.sqrt(np.sum((np.array(xy) - np.array(actual_xy)) ** 2))
              # total the error
              total_error += np.nan_to_num(error)

              # if the error was high, print out more information
              if np.sum(error) > thresh:
                  print('-------------------------')
                  print('Initial joint angles', arm.q)
                  print('Final joint angles: ', q)
                  print('Desired hand position: ', xy)
                  print('Actual hand position: ', actual_xy)
                  print('Error: ', error)
                  print('-------------------------')

              count += 1

      print('\n---------Results---------')
      print('Total number of trials: ', count)
      print('Total error: ', total_error)
      print('-------------------------')


if __name__ == '__TestArm__':
    unittest.main()
