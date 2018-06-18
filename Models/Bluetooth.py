'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Edited by:      Thijs Zijlstra
Version:        2.0
Description:    Bluetooth
'''

import bluetooth
import serial
import Mode


class Bluetooth:
    mode = Mode.Mode()

    def __init__(self):
        self.sock = self.connect()

    def read_data(self):
        # send it to arduino
        ser = serial.Serial('/dev/ttyUSB0', 9600)

        while 1:
            try:
                data = self.sock.recv(1024)                # read incoming data
                #data_end = data.find('\r\n')                # split by new line
                if len(data)> 1:
                    array = data.split()                    # splits the incoming data in an array
                    if len(array) > 1:    # check if the last number of the array is the length of
                                                            # the needed int
                        ser.write(array)                   # write data to arduino
                        print(array)                       # testing
                        self.mode.init_modes(array, array) # give result

            except KeyboardInterrupt:
                break

        self.disconnect()

    @staticmethod
    def connect():
        bd_addr = "98:D3:31:FB:14:C8"  # MAC-address of our bluetooth-module
        port = 1
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((bd_addr, port))
        return sock

    def disconnect(self):
        self.sock.close()


if __name__ == '__Bluetooth__':
    Bluetooth()