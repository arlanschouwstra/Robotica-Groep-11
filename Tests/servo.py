import Models.ax12 as x
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        y = x.Ax12()

        y.moveSpeed(x.Ax12(), 9, 300, 500)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        y.moveSpeed(x.Ax12(), 9, 300, 0)
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '_servo_':
    unittest.main()



