import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cvtColor(bgr, hsv, COLOR_BGR2HSV);
    # hsv hue sat value
    lower_red = np.array([0, 200, 120])
    upper_red = np.array([255, 255, 255])

    maskR = cv2.inRange(hsv, lower_red, upper_red)
    resR = cv2.bitwise_and(frame, frame, mask = maskR)

    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(resR, -1, kernel)

    blur = cv2.GaussianBlur(resR, (15, 15), 0)
    median = cv2.medianBlur(resR, 15)
    bilateral = cv2.bilateralFilter(resR, 15, 75, 75)


    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', resR)
    #cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()