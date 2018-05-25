import pyfirmata
import time
# on the Arduino, load a new file with the example firmata and then pick StandardFirmata.
# https://www.youtube.com/watch?v=s4o8T6F-zGU
board = pyfirmata.Arduino('/dev/ttyACM0')
# The first section determines if the pin will be used in analog or digital mode.
# The second section is the number of the pin you would like to use.
# The third section selects the pin mode between input, output, pwm, and servo.
# The returned pin can be assigned to a variable and then later used to call read() and write() methods.
pin13 = board.get_pin('d:13:o')
while True:
    # turns LED on pin 13 on and off.
    time.sleep(1)
    print("on")
    pin13.write(1)
    time.sleep(1)
    print("off")
    pin13.write(0)