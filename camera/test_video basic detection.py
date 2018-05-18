# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
        imageC = frame.array

        # show the frame
        img = cv2.cvtColor(imageC,cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img,(25,25),0)
        ret, th = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)
        image, contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 500:
                img = cv2.drawContours(imageC, [cnt], -1, (0,255,255), 3)

	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
