import bluetooth
import unittest


class TestBluetooth(unittest.TestCase):

    @staticmethod
    def bluetooth_connect(self):
        bd_addr = "98:D3:31:FB:14:C8"  # MAC-address of our bluetooth-module
        port = 1
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        connection = sock.connect((bd_addr, port))
        self.assertEqual(connection, 1)
        sock.close()


if __name__ == '_bluetoothController_':
    unittest.main()
