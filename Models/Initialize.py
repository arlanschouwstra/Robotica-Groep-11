class Initialize:

    def __init__(self):
        pass

    # create methods here: -->
    @staticmethod
    def run_servo():
        import Servo

        servo = Servo.Servo()
        servo.reset_servos()
        servo.run_servos()

    @staticmethod
    def run_camera():
        import Camera

        camera = Camera.Camera()
        camera.detect()
