import time
import Servo
import serial

class Dance:
    def __init__(self):
        self.move = getattr(Servo, 'move_position')
    #  for serial connection between Pi and Arduino.
    def connect_usb(self):
        ser = serial.Serial('/dev/ttyACM0', 9600)
        return ser

    def send_data(self, ser, data):
        ser.write(str(data))

    def receive_data(self, ser):
        return ser.readline()

    def set_start_position(self):
        # set servos to their start positions
        # from bootom to stop of the arm.
        Servo.Servo().reset_servos()

#   ////////////////////////////////////////////////////////////////////////
#   TESTEN.
#   ////////////////////////////////////////////////////////////////////////
    def buildup_speed(self, idServo, distance, speed):    #TESTEN!!!
        start_speed = speed*2
        self.move(idServo, distance, start_speed)
        time.sleep(0.5)
        self.move(idServo, distance, speed)

    def twist(self):
        # sets servo 51 to start_pos
        if self.not_at_position(51, 512):
            self.run(51, 512, 1)
        time.sleep(1)
        if self.not_at_position(4, 512):
            self.run(4, 512, 1)
            time.sleep(1)
        # do Twist.
        for x in range(2):
            # turn far right
            self.run(51, 612, 0.5)
            time.sleep(0.6)
            # turn far left
            self.run(51, 412, 0.5)
            time.sleep(0.6)

        self.run(51, 512, 1)

    def headbang(self):
        for x in range(6):
            self.run(23, 512, 1)
            self.run(4, 412, 1)
            time.sleep(0.5)
            self.run(23, 612, 1)
            self.run(4, 512, 1)
            time.sleep(0.5)

    def rap(self, times):
        self.run(51, 612, 1)
        self.run(23, 612, 05)
        self.run(4, 512, 0.5)
        time.sleep(1)
        for x in range(times):
            if self.at_destination():
                self.run(23, 512, 0.5)
                self.run(4, 312, 0.5)
                time.sleep(0.7)
            if self.at_destination():
                self.run(23, 612, 0.5)
                self.run(4, 512, 0.5)
                time.sleep(0.7)

#   ////////////////////////////////////////////////////////////////////////////
#   AANPASSEN.
#   ////////////////////////////////////////////////////////////////////////////

    def move_left(self, speed):
        self.move(41, 400, speed)

    def move_right(self, speed):
        self.move(41, 600, speed)

    def move_center(self, speed):
        self.move(41, 500, speed)

    def weave_right(self, speed):
        self.stretch_backward(speed)
        self.move_right(speed/2)
        self.stretch_forward(speed/2)
        self.move_left(speed/2)
        self.stretch_backward(speed/2)
        self.move_center(speed/2)

    def weave_left(self, speed):
        self.stretch_backward(speed)
        self.move_left(speed/2)
        self.stretch_forward(speed/2)
        self.move_right(speed/2)
        self.stretch_backward(speed/2)
        self.move_center(speed/2)

    def sprinkler(self, speed):
        self.move(3, 200, speed)
        self.move(15, 823, speed)
        self.move(23, 723, speed)
        time.sleep(1)
        self.move_right(speed)
        time.sleep(1)
        for x in range(6):
            # move left
            self.move(41, 600, speed/2)
            time.sleep(1)
            self.move(41, 500, speed / 2)
            time.sleep(1)
            self.move(41, 400, speed / 2)
            time.sleep(1)
            self.move(41, 300, speed / 2)
            time.sleep(1)
            #move right
            self.move(41, 400, speed / 2)
            time.sleep(1)
            self.move(41, 500, speed / 2)
            time.sleep(1)
            self.move(41, 600, speed / 2)
            time.sleep(1)
            self.move(41, 700, speed / 2)
            time.sleep(1)

#   //////////////////////////////////////////////////////////////////////////
#   TESTED.
#   //////////////////////////////////////////////////////////////////////////

    # returns required speed to do movement in 1 second.
    # example: move from 200 to 400, would return a difference of 200, ehen this is entered in as the speed,
    # the movement would take 1 second to complete.
    def calc_speed(self, servo_id, destination):
        return abs(self.read_pos(servo_id)-destination)

    # runs the servo, put in lower_speed: 1 to not lower the speed.
    def run(self, servo_id, destination, modifier):
        if modifier == 0.5:
            self.move(servo_id, destination, self.calc_speed(servo_id, destination)*2)
        else:
            self.move(servo_id, destination, self.calc_speed(servo_id, destination)/modifier)

    def at_destination(position, desired_position):
        if position == desired_position:
            return True
        else:
            return False

    def stretch_forward(self, speed):
        self.move(3, 0, speed)
        self.move(15, 1023, speed)
        self.move(23, 823, speed)

    def stretch_backward(self, speed):
        self.move(3, 200, speed)
        self.move(15, 823, speed)
        self.move(23, 623, speed)

    def start(self):
        # (naam,beweging,snelheid)
        # -------onder servos lichaam-------
        # self.move(3, )    # onder servo                 (0: max down, 200: max up)
        # self.move(15, )   # onder servo tegen gesteld   (1023: max down, 823 max up)
        # self.move(23, )   # midden servo                (623: max down, 823:max up)
        # self.move(41, )   # servo vertical              (300: max left, 700: max right)
        # -------servos kop------

        # self.move(6)      # 2e servo                    (300: max left, 700: max right)
        # self.move(4)      # 3e servo                    (300: max left, 700: max right)
        # time.sleep(1)       # used for sleep

        self.set_start_position(y)

        ser = self.connect_usb()
        self.send_data(ser, "display_group_name")
dance = Dance()
dance.set_start_position()
time.sleep(5)
#dance.stretch_backward()
#dance.stretch_forward()
#dance.headbang()
#dance.twist()
dance.rap(10)
