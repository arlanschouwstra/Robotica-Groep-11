# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import time


class Camera:

    def __init__(self):
        pass

    def nothing(*arg):
        pass

    def detect(self):
        # construct the argument parse and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-v", "--video",
                        help="path to the (optional) video file")
        ap.add_argument("-b", "--buffer", type=int, default=32,
                        help="max buffer size")
        args = vars(ap.parse_args())
        # define the lower and upper boundaries of the "green" ball in the HSV color space (HUE SATURATION VALUE)

        # Initial HSV GUI slider values to load on program start.
        icol = (0, 0, 0, 255, 255, 255)  # start Value low/high

        cv2.namedWindow('colorTest')
        # Lower range colour sliders.
        cv2.createTrackbar('low_hue', 'colorTest', icol[0], 255, self.nothing)
        cv2.createTrackbar('low_sat', 'colorTest', icol[1], 255, self.nothing)
        cv2.createTrackbar('low_val', 'colorTest', icol[2], 255, self.nothing)
        # Higher range colour sliders.
        cv2.createTrackbar('high_hue', 'colorTest', icol[3], 255, self.nothing)
        cv2.createTrackbar('high_sat', 'colorTest', icol[4], 255, self.nothing)
        cv2.createTrackbar('high_val', 'colorTest', icol[5], 255, self.nothing)
        # redLowerHSV = (170, 200, 50)
        # redUpperHSV = (255, 255, 255)

        # initialize the list of tracked points, the frame counter, and the coordinate deltas
        pts = deque(maxlen=args["buffer"])
        counter = 0
        (dX, dY) = (0, 0)
        direction = ""

        # grab the reference to the webcam
        camera = cv2.VideoCapture(0)

        # keep looping
        while True:
            # grab the current frame
            (_, frame) = camera.read()

            # resize the frame, blur it, and convert it to the HSV color space
            frame = imutils.resize(frame, width=600)
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Get HSV values from the GUI sliders.
            low_hue = cv2.getTrackbarPos('low_hue', 'colorTest')
            low_sat = cv2.getTrackbarPos('low_sat', 'colorTest')
            low_val = cv2.getTrackbarPos('low_val', 'colorTest')
            high_hue = cv2.getTrackbarPos('high_hue', 'colorTest')
            high_sat = cv2.getTrackbarPos('high_sat', 'colorTest')
            high_val = cv2.getTrackbarPos('high_val', 'colorTest')

            # construct a mask for the color "green", then perform a series of dilations and erosions to remove any small blobs left in the mask
            color_low = np.array([low_hue, low_sat, low_val])
            color_high = np.array([high_hue, high_sat, high_val])
            mask = cv2.inRange(hsv, color_low, color_high)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            # find contours in the mask and initialize the current (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None
            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
                contour_sizes = [(cv2.contourArea(contour), contour) for contour in cnts]
                c = max(contour_sizes, key=lambda x: x[0])[1]
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # only proceed if the radius meets a minimum size
                if radius > 10:
                    # draw the circle and centroid on the frame, then update the list of tracked points
                    cv2.circle(frame, (int(x), int(y)), int(radius),
                               (0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    pts.appendleft(center)
            # loop over the set of tracked points
            for i in np.arange(1, len(pts)):
                # if either of the tracked points are None, ignore them
                if pts[i - 1] is None or pts[i] is None:
                    continue

                # check to see if enough points have been accumulated in the buffer
                if counter >= 10 and i == 1 and pts[-10] is not None:
                    # compute the difference between the x and y coordinates and re-initialize the direction text variables
                    dX = pts[-10][0] - pts[i][0]
                    dY = pts[-10][1] - pts[i][1]
                    (dirX, dirY) = ("", "")

                    # ensure there is significant movement in the x-direction
                    if np.abs(dX) > 20:
                        dirX = "East" if np.sign(dX) == 1 else "West"

                    # ensure there is significant movement in the y-direction
                    if np.abs(dY) > 20:
                        dirY = "North" if np.sign(dY) == 1 else "South"

                    # handle when both directions are non-empty
                    if dirX != "" and dirY != "":
                        direction = "{}-{}".format(dirY, dirX)

                    # otherwise, only one direction is non-empty
                    else:
                        direction = dirX if dirX != "" else dirY

            # show the movement deltas and the direction of movement on the frame
            cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.65, (0, 0, 255), 3)
            cv2.putText(frame, "dx: {}, dy: {}".format(dX, dY),
                        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.35, (0, 0, 255), 1)

            # show the frame to our screen and increment the frame counter
            cv2.imshow("Frame", frame)
            cv2.imshow("Mask", mask)
            key = cv2.waitKey(1) & 0xFF
            counter += 1

            # if the 'q' key is pressed, stop the loop
            if key == ord("q"):
                break

        # cleanup the camera and close any open windows
        camera.release()
        cv2.destroyAllWindows()


# calling method:
camera = Camera()
camera.detect()
