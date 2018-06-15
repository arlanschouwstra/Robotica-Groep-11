import serial
# for serial connection between Pi and Arduino.
ser = serial.Serial('/dev/ttyACM0', 9600)
#   while 1:
#       ser.write("displayGroupName")
