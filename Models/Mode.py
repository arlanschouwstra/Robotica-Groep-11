import ax12 as x
import Servo


class Mode:
    y = x.Ax12()
    servo = Servo.Servo()

    def __init__(self):
        pass

    def init_modes(self, result, array):

        """__________________DRIVING MODE_______________"""
        if result[10:11] == '0':
            self.servo.reset_servos()            # go to the start position(maybe not needed to call this every time)

            if result != array[len(array) - 3]:
                self.servo.move_all_servos(result)

            elif result == '35451525000':  # if not stopped, stop all servos
                self.servo.stop_all_servos()

        """_________________DANCING MODE_________________"""
        if result[10:11] == '3':
            string = self.ser.readline()
            lowValue = string[1]
            middleValue = string[2]
            highValue = string[3]

        """________________LINE DANCE MODE_______________"""
        if result[10:11] == '1':
            pass

        """_____________TRANSPORT AND REBUILD____________"""
        if result[10:11] == '5':
            pass                # kinematics and Camera here
