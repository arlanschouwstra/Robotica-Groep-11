import time
import Servo
import serial

class Dance:
    def __init__(self):
        self.move = getattr(Servo, 'move_position')
        self.read_pos = getattr(Servo, 'read_position')
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
        # from bottom to stop of the arm.
        self.move(41, 512, 50)

        self.move(3, 512, 50)
        self.move(15, 512, 50)

        self.move(23, 512, 50)

        self.move(6, 200, 50)

        self.move(51, 812, 50)

        self.move(4, 512, 50)

#   ///////////////////////////////////////////////////////////////////////
#   TESTEN.
#   ///////////////////////////////////////////////////////////////////////
    def buildup_speed(self, id_servo, distance, speed):
        start_speed = speed*2
        self.move(id_servo, distance, start_speed)
        time.sleep(0.5)
        self.move(id_servo, distance, speed)

    #   determines the required speed to go from current posistion to destination.
    def calc_speed(self, servo_id, destination):
        return abs(self.read_pos(servo_id)-destination)

    def not_at_position(self, servo_id, destination):
        if self.read_pos(servo_id) != destination:
            return True
        else:
            return False

    def headbang(self):
        #if self.not_at_position(3, 512) and self.not_at_position(15, 512):
        #    self.move(3, 512, self.calc_speed(3, 512))
        #    self.move(15, 512, self.calc_speed(15, 512))
        #if self.not_at_position(23, 612):
        #    self.move(23, 612, self.calc_speed(23, 612))
        #    time.sleep(1)
        if self.read_pos(3) != 512 and self.read_pos(15) != 512:
            self.move(3, 512, (abs(self.read_pos(3)-512)))
            self.move(15, 512, (abs(self.read_pos(15)-512)))
        if self.read_pos(23) != 612:
            self.move(23, 612, (abs(self.read_pos(23)-612)))
            time.sleep(1)
        else:
            for x in range(6):
                self.move(3, 212, 300)
                self.move(15, 812, 300)
                self.move(23, 512, 100)
                time.sleep(1)
                self.move(3, 512, 300)
                self.move(15, 512, 300)
                self.move(23, 612, 100)
                time.sleep(1)

    def twist(self):
        if self.read_pos(51) != 712:
            self.move(51, 712, 100)  # start up the twist.
            time.sleep(1)
        else:
            for x in range(6):
                self.move(51, 912, 200)    # turn far left
                time.sleep(1)
                self.move(51, 712, 200)    # turn far right
                time.sleep(1)
#   ///////////////////////////////////////////////////////////////////////
#   AANPASSEN.
#   ///////////////////////////////////////////////////////////////////////
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
            #   move left
            self.move(41, 600, speed/2)
            time.sleep(1)
            self.move(41, 500, speed/2)
            time.sleep(1)
            self.move(41, 400, speed/2)
            time.sleep(1)
            self.move(41, 300, speed/2)
            time.sleep(1)
            #   move right
            self.move(41, 400, speed/2)
            time.sleep(1)
            self.move(41, 500, speed/2)
            time.sleep(1)
            self.move(41, 600, speed/2)
            time.sleep(1)
            self.move(41, 700, speed/2)

#   ///////////////////////////////////////////////////////////////////////
#   TESTED.
#   ///////////////////////////////////////////////////////////////////////
    def stretch_forward(self, speed):
        self.move(3, 212, speed)
        self.move(15, 812, speed)
        self.move(23, 812, speed)

    def stretch_backward(self, speed):
        self.move(3, 612, speed)
        self.move(15, 412, speed)
        self.move(23, 412, speed)

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
dance.twist()
#dance.set_start_position()
#dance.stretch_backward()
#dance.stretch_forward()
#dance.headbang()
