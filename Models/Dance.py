import time
import Servo
import serial


class Dance:
    def __init__(self):
        self.move = getattr(Servo.Servo(), 'move_position')
        self.read_pos = getattr(Servo.Servo(), 'read_position')

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

    #   ////////////////////////////////////////////////////////////////////////////
    #   AANPASSEN.
    #   ////////////////////////////////////////////////////////////////////////////

    def sprinkler(self, times):
        if self.not_at_destination(3, 612) and self.not_at_destination(15, 412):
            self.run(3, 612, 1)
            self.run(15, 412, 1)
            time.sleep(1.1)
        if self.not_at_destination(23, 512):
            self.run(23, 512, 1)
            time.sleep(1.1)
        if self.not_at_destination(41, 812):
            self.run(41, 812, 1)
            time.sleep(1.1)

        for x in range(times):
            self.run(41, 712, 0.5)
            time.sleep(0.7)
            self.run(41, 612, 0.5)
            time.sleep(0.7)
            self.run(41, 512, 0.5)
            time.sleep(0.7)
            self.run(41, 412, 0.5)
            time.sleep(0.7)
            self.run(41, 312, 0.5)
            time.sleep(0.7)
            self.run(41, 212, 0.5)
            time.sleep(0.7)

            self.run(41, 812, 3)
            time.sleep(2.5)

        self.run(51, 512, 1)  # reset position.
        self.run(3, 512, 1)
        self.run(15, 512, 1)
        self.run(23, 512, 1)
        self.run(41, 512, 3)

    #   //////////////////////////////////////////////////////////////////////////
    #   TESTED.
    #   //////////////////////////////////////////////////////////////////////////

    # returns required speed to do movement in 1 second.
    # example: move from 200 to 400, would return a difference of 200, ehen this is entered in as the speed,
    # the movement would take 1 second to complete.
    def calc_speed(self, servo_id, destination):
        return abs(self.read_pos(servo_id) - destination)

    # runs the servo, put in lower_speed: 1 to not lower the speed.
    def run(self, servo_id, destination, modifier):
        if modifier == 0.5:
            self.move(servo_id, destination, self.calc_speed(servo_id, destination) * 2)
        else:
            self.move(servo_id, destination, self.calc_speed(servo_id, destination) / modifier)

    def at_destination(self, servo_id, desired_position):
        if self.read_pos(servo_id) == desired_position:
            return True
        else:
            return False

    def not_at_destination(self, servo_id, desired_position):
        if self.read_pos(servo_id) != desired_position:
            return True
        else:
            return False

    def twist(self, times):
        # sets servo 51 to start_pos
        if self.not_at_destination(51, 512):
            self.run(51, 512, 1)
        time.sleep(1)
        if self.not_at_destination(4, 512):
            self.run(4, 512, 1)
            time.sleep(1)
        if self.not_at_destination(3, 512) and self.not_at_destination(15, 512):
            self.run(3, 512, 1)
            self.run(15, 512, 1)
            time.sleep(1)
        if self.not_at_destination(23, 512):
            self.run(23, 512, 1)
            time.sleep(1)
        # do Twist.
        for x in range(times):
            self.run(51, 612, 0.5)  # turn far right.
            time.sleep(0.7)
            self.run(51, 412, 0.5)  # turn far left.
            time.sleep(0.7)
            self.run(3, 412, 1)  # move forward.
            self.run(15, 612, 1)
            self.run(23, 612, 1)
            self.run(51, 612, 0.5)
            time.sleep(0.7)
            self.run(51, 412, 0.5)
            time.sleep(0.7)
            self.run(3, 612, 1)  # move backward.
            self.run(15, 412, 1)
            self.run(23, 412, 1)
            time.sleep(1.2)

        self.run(51, 512, 1)  # reset position.
        self.run(3, 512, 1)
        self.run(15, 512, 1)
        self.run(23, 512, 1)

    def headbang(self, times):
        self.run(51, 612, 1)
        self.run(23, 612, 1)
        self.run(4, 512, 1)
        time.sleep(1)
        for x in range(times):
            self.run(23, 512, 0.5)
            self.run(4, 312, 0.5)
            time.sleep(0.7)
            self.run(23, 612, 0.5)
            self.run(4, 512, 0.5)
            time.sleep(0.7)

    def start(self):
        # (naam,beweging,snelheid)
        # -------onder servos lichaam-------
        # self.move(41, )   # servo vertical              (212: max left, 512: middle, 812: max right)
        # self.move(3, )    # onder servo                 (812: max down, 512: middle, 212: max up)
        # self.move(15, )   # onder servo tegen gesteld   (212: max down, 512: middle, 812: max up)
        # self.move(23, )   # midden servo                (312: max down, 512: middle, 912: max up)
        # -------servos kop------

        # self.move(6, )      # 1e servo                (0: max left, 200: middle, 400: max right)
        # self.move(51, )      # 2e servo               (212: max left, 512: middle, 812: max right)
        # self.move(4, )      # 3e servo                (212: max left, 512: middle, 812: max right)

        self.set_start_position(y)

        ser = self.connect_usb()
        self.send_data(ser, "display_group_name")


dance = Dance()
dance.set_start_position()
time.sleep(1)
dance.sprinkler(2)
time.sleep(1)
dance.set_start_position()
time.sleep(1)
dance.twist(2)
# time.sleep(1)
# dance.set_start_position()
# time.sleep(1)
# dance.headbang(10)
