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
                #print('data %s', data)
                if len(data)> 1:
                    array = data.split("\r\n")                    # splits the incoming data in an array
                    #print('array %s', ''.join(array))
                    last_number = [len(array) - 1]
                    ser.write(last_number)                   # write data to arduino
                    self.mode.init_modes(last_number) # give result
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