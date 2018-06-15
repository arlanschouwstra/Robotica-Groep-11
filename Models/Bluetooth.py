'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
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

        data = ""
        while 1:
            try:

                data += self.sock.recv(1024)                # read incoming data
                data_end = data.find('\r\n')                # split by new line
                array = []
                if data_end != -1:
                    array = data.split()                    # splits the incoming data in an array
                    data = data[data_end + 1:]

                    if len(array[len(array) - 2]) == 11:    # check if the last number of the array is the length of
                                                            # the needed int
                        result = array[len(array) - 2]
                        ser.write(result)                   # write data to arduino
                        print result                        # testing
                        self.mode.init_modes(result, array) # give result

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
