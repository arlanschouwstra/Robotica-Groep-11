from Models import Bluetooth
import unittest


class TestBluetooth(unittest.TestCase):

    @staticmethod
    def test_connect(self):
        connect = getattr(Bluetooth, 'connect')
        sock = connect(self)
        self.assertEqual(sock, 1)

if __name__ == '_bluetoothController_':
    unittest.main()
