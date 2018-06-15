import cv2
import numpy as np

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        shape = "Unknown"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 4:
            (x,y,w,h) = cv2.boundingRect(approx)
            ar = w / float(h)
            if w > 40 and h > 40:
                shape = "rectangle"
            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle          

        return shape

    
