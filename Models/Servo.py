import ax12 as x
import RF as Rf


class Servo:
    # important! make sure the result position is not less than 0
    # method not used but could be of use
    @staticmethod
    def move_degree(servo, start_position, degree, clockwise):
        y = x.Ax12()
        if degree == 90:
            if clockwise:
                y.moveSpeed(servo, (start_position - 312), 50)
            else:
                y.moveSpeed(servo, (start_position + 312), 50)
        else:
            get_degree = 90 / degree
            if clockwise:
                y.moveSpeed(servo, (start_position - (312 / get_degree)), 50)
            else:
                y.moveSpeed(servo, (start_position - (312 / get_degree)), 50)
        print("moving servo: ", servo, "at", degree, "degrees")

    @staticmethod
    def reset_servos():
        y = x.Ax12()
        # set servos to their start positions
        y.moveSpeed(3, 512, 50)
        y.moveSpeed(4, 512, 50)
        y.moveSpeed(6, 200, 50)
        y.moveSpeed(15, 512, 50)
        y.moveSpeed(23, 812, 50)
        y.moveSpeed(41, 512, 50)
        y.moveSpeed(51, 1023, 50)
        # print servos positions (for testing purposes)
        print(y.readPosition(3))
        print(y.readPosition(4))
        print(y.readPosition(6))
        print(y.readPosition(15))
        print(y.readPosition(23))
        print(y.readPosition(51))
        print(y.readPosition(41))

    @staticmethod
    def get_speed(joystick):
        # ______to the right________#
        if joystick == 1:
            return 200
        if joystick == 2:
            return 150
        if joystick == 3:
            return 100
        if joystick == 4:
            return 50
        # _______to the left_________#
        if joystick == 6:
            return 50
        if joystick == 7:
            return 100
        if joystick == 8:
            return 150
        if joystick == 9:
            return 200

    # moving the given servo forward or backward on button press
    def move(self, servo_id, start_position, clockwise, body, vertical):
        y = x.Ax12()
        rf = Rf.RF()

        if rf.receiver.available():
            received_value = rf.receiver.getReceivedValue()

            # initialize each position of the joystick
            if received_value:
                rf.regex(received_value)

                if rf.value_yl > 5:  # move up
                    speed = self.get_speed(rf.value_yl)

                    if body:
                        if vertical:
                            y.moveSpeed(servo_id, start_position, speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_yl < 5:  # move down
                    speed = self.get_speed(rf.value_yl)

                    if body:
                        if vertical:
                            if not clockwise:
                                y.moveSpeed(servo_id, start_position + 200, speed)
                                print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))
                            else:
                                y.moveSpeed(servo_id, start_position - 200, speed)
                                print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_xl < 5:  # move left
                    speed = self.get_speed(rf.value_xl)

                    if body:
                        if not vertical:
                            y.moveSpeed(servo_id, start_position + 200, speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_xl > 5:  # move right
                    speed = self.get_speed(rf.value_xl)

                    if body:
                        if not vertical:
                            y.moveSpeed(servo_id, start_position - 200, speed)
                            print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_xr < 5:  # move left head
                    speed = self.get_speed(rf.value_xr)

                    if not body:
                        if not vertical:
                            if clockwise:
                                y.moveSpeed(servo_id, start_position + 200, speed)
                                print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_xr > 5:  # move right head
                    speed = self.get_speed(rf.value_xr)

                    if not body:
                        if not vertical:
                            if clockwise:
                                y.moveSpeed(servo_id, start_position - 200, speed)
                                print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_yr > 5:  # move up head
                    if not body:
                        if not vertical:
                            if not clockwise:
                                y.moveSpeed(servo_id, start_position + 200, speed)
                                print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                if rf.value_yr < 5:  # move down head
                    if not body:
                        if not vertical:
                            if not clockwise:
                                y.moveSpeed(servo_id, start_position - 200, speed)
                                print("Servo:", servo_id, "moved to position:", y.readPosition(servo_id))

                else:
                    y.moveSpeed(servo_id, y.readPosition(servo_id), speed)

    # calling the servos to move
    def run_servos(self):
        self.reset_servos()

        # initialize servos
        start_positions = [[3, 512, True, True, True],  # right under for up/down
                           [4, 512, False, False, False],  # top servo
                           [6, 200, False, False, False],
                           [15, 512, False, True, True],
                           [23, 823, True, True, True],
                           [41, 512, True, True, False],  # left under for up/down
                           [51, 1023, True, False, False]]

        while True:
            for servo in start_positions:
                self.move(servo[0], servo[1], servo[2], servo[3], servo[4])
