'''
Date:           03-08-2018
Creator:        Arlan Schouwstra
Version:        1
Description:    Main Function
'''

import Mode

while True:
    try:
        mode = Mode.Mode()
        mode.init_modes()

    except Exception as e:
        print "Exception occured: ", e
