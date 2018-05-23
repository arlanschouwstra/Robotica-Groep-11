import cv2
import numpy as np
import time


class Camera:

    def __init__(self):
        pass

    def nothing(*arg):
        pass

    def detect(self):
        FRAME_WIDTH = 320
        FRAME_HEIGHT = 240

        # Initial HSV GUI slider values to load on program start.
        # icol = (36, 202, 59, 71, 255, 255)    # Green
        # icol = (18, 0, 196, 36, 255, 255)  # Yellow
        # icol = (89, 0, 0, 125, 255, 255)  # Blue
        # icol = (0, 100, 80, 10, 255, 255)   # Red
        # icol = (104, 117, 222, 121, 255, 255)   # test
        icol = (0, 105, 160, 255, 255, 255)  # New start

        cv2.namedWindow('colorTest')
        # Lower range colour sliders.
        cv2.createTrackbar('low_hue', 'colorTest', icol[0], 255, self.nothing)
        cv2.createTrackbar('low_sat', 'colorTest', icol[1], 255, self.nothing)
        cv2.createTrackbar('low_val', 'colorTest', icol[2], 255, self.nothing)
        # Higher range colour sliders.
        cv2.createTrackbar('high_hue', 'colorTest', icol[3], 255, self.nothing)
        cv2.createTrackbar('high_sat', 'colorTest', icol[4], 255, self.nothing)
        cv2.createTrackbar('high_val', 'colorTest', icol[5], 255, self.nothing)

        # Initialize webcam. Webcam 0 or webcam 1 or ...
        vidCapture = cv2.VideoCapture(0)
        vidCapture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        vidCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        while True:
            time_check = time.time()
            # Get HSV values from the GUI sliders.
            low_hue = cv2.getTrackbarPos('low_hue', 'colorTest')
            low_sat = cv2.getTrackbarPos('low_sat', 'colorTest')
            low_val = cv2.getTrackbarPos('low_val', 'colorTest')
            high_hue = cv2.getTrackbarPos('high_hue', 'colorTest')
            high_sat = cv2.getTrackbarPos('high_sat', 'colorTest')
            high_val = cv2.getTrackbarPos('high_val', 'colorTest')

            # Get webcam frame
            _, frame = vidCapture.read()

            # Show the original image.
            cv2.imshow('frame', frame)

            # Convert the frame to HSV colour model.
            frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # HSV values to define a colour range we want to create a mask from.
            color_low = np.array([low_hue, low_sat, low_val])
            color_high = np.array([high_hue, high_sat, high_val])
            mask = cv2.inRange(frame_hsv, color_low, color_high)
            # Show the first mask
            cv2.imshow('mask-plain', mask)

            im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
            biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

            # cv2.drawContours(frame, biggest_contour, -1, (0,255,0), 3)

            x, y, w, h = cv2.boundingRect(biggest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # cv2.drawContours(frame, contours, -1, (0,255,0), 3)

            cv2.drawContours(frame, contours, 3, (0,255,0), 3)

            # cnt = contours[1]
            # cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)

            # Show final output image
            cv2.imshow('colorTest', frame)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
            print('fps - ', 1 / (time.time() - time_check))

        cv2.destroyAllWindows()
        vidCapture.release()


# calling method:
camera = Camera()
camera.detect()
