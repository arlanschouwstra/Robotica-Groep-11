'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Edited by:      Thijs Zijlstra
Version:        2.0
Description:    Bluetooth
'''

import bluetooth
import serial
from Mode import Mode
import json
from pprint import pprint

class Bluetooth:
    mode = Mode()

    def __init__(self):
        self.sock = self.connect()

    def read_data(self):
        # send it to arduino
        ser = serial.Serial('/dev/ttyUSB0', 9600)

        while self.sock.connected():
            try:
                data = self.sock.recv(8)                # read incoming data
                data_split = data.split()

                print("splitted data: %s", data_split)
                # data = '{"xr": 12}'
                jsonObject = json.loads(data)
                key = list(jsonObject.keys())[0]
                print('key : %s', key)
                value = jsonObject[key]
                print('value : %s', value)
                if key == 'md':
                    self.mode.change_mode(value)  # give result
                else:
                    self.mode.init_modes(key, value)   # give result
                ser.write(value)
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