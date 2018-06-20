# -*- coding: utf-8 -*-
#@author: Leon
from imutils import paths
import numpy as np
import imutils
import cv2

def findMarker(image):
    #convert the image to hsv/gray, blurs it and makes it detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1)
    edged = cv2.Canny(blur, 35, 125)
    
    #find the contours of the largest image on the screen
    #cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key = cv2.contourArea)
    return cv2.minAreaRect(c)

def distanceToCamera(knownWidth, focallength, perWidth):
    return (knownWidth * focallength) / perWidth
    
    
#image = cv2.imread(IMAGE_PATHS[0])
knownDistance = 24.0

# initialize the known object width, which in this case, the piece of
# paper is 12 inches wide
knownWidth = 11.0

cap = cv2.VideoCapture(0)
 
while True:
    _, frame = cap.read()
    marker = findMarker(frame)
    focallength = (marker[1][0] * knownDistance) / knownWidth
    #load the image, find the marker in the image, then compute the
    # distance to the marker from the camera
    marker = findMarker(frame)
    inches = distanceToCamera(knownWidth, focallength, marker[1][0])
    
    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    cv2.putText(frame, "%.2fft" % (inches / 12),
        (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
        2.0, (0, 255, 0), 3)
    cv2.imshow("frame", frame)
    
    #Closing the video capturing
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
cap.release()
   
