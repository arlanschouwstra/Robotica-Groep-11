'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Version:        1
Description:    Main Function
'''

import Bluetooth

while True:
    try:
        bluetooth = Bluetooth.Bluetooth()
        bluetooth.read_data()

    except Exception as e:
        print "Exception occured: ", e
