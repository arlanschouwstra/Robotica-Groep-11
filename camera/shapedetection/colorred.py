import cv2
import numpy as np
import imutils
from shapedetector import ShapeDetector

cap = cv2.VideoCapture(0)

def findContours(mask, frame):
    # find contours in the treshholded frame and initialize the shape detector
    ratio = 1.0
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetector()

    for c in cnts:
        #compute the center of the contour, then detect the rectangle of the
        # shape using only the contour
        M = cv2.moments(c)
        if M["m10"] == 0.0 or M["m00"] == 0.0 or M["m01"] == 0.0:
            continue
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)
        if (shape != "rectangle"):
            continue
        
        # multiply the contour (x, y)-coordinates by the resize ratio,
        # then draw the contours and the name of the shape on the frame
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0),2)


while True:
    _, frame = cap.read()
    
    #blurrs the video so more of the expected color is shown
    blur = cv2.GaussianBlur(frame, (7, 7), 3)
    
    #color wheel 1/4th degrees changed to the left
    hsv = cv2.cvtColor(blur,cv2.COLOR_RGB2HSV)
    lower_red = np.array([220 * 0.5, 50 * 2.55,40 * 2.55])
    upper_red = np.array([250 * 0.5, 100 * 2.55,100 * 2.55])
    lower_green = np.array([95 * 0.5, 32 * 2.55, 22 * 2.55])
    upper_green = np.array([125 * 0.5, 100 * 2.55, 100 * 2.55])
    lower_yellow = np.array([185 * 0.5, 55 * 2.55, 60 * 2.55])
    upper_yellow = np.array([220 * 0.5, 100 * 2.55, 100 * 2.55])
    lower_orange = np.array([200 * 0.5, 60 * 2.55, 60 * 2.55])
    upper_orange = np.array([250 * 0.5, 100 * 2.55, 100 * 2.55])
    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_green, upper_green)
    mask3 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask4 = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # combining the masks together to see all blocks
    mergeMask = cv2.bitwise_or(mask1, mask2)
    mergeMask = cv2.bitwise_or(mergeMask, mask3)
    mergeMask = cv2.bitwise_or(mergeMask, mask4)
    
    #checking if the shape is rectangle
    findContours(mask1,blur)
    findContours(mask2,blur)
    findContours(mask3,blur)
    findContours(mask4,blur)
    
    #Showing the esolution
    res = cv2.bitwise_and(blur, blur, mask = mergeMask)
    
    #show video screens
    cv2.imshow('blurredFrame', blur)
    cv2.imshow('res', res)
    #cv2.imshow('mask', mask)
    
    #Closing the video capturing
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
