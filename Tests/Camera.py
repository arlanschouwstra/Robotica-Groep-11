import argparse
import imutils
import cv2
import numpy as np
import unittest
import matplotlib.pyplot as plt


class TestCamera(unittest.TestCase):

    def test_image_recognition(self):
        img = cv2.imread('C:\Users\Brave\Downloads\lel336.jpg', cv2.IMREAD_COLOR)

        cv2.line(img, (0, 0), (150, 150), (255, 255, 255), 15)
        cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 15)
        cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)

        pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
        # pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 255), 5)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'OpenCV', (0, 130), font, 3, (200, 255, 255), 5, cv2.LINE_AA)

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_2(self):
        img = cv2.imread('C:\Users\Brave\Downloads\lel336.jpg', cv2.IMREAD_COLOR)

        img[55, 55] = [255, 255, 255]
        px = img[55, 55]

        img[100:150, 100:150] = [255, 255, 255]

        watch_face = img[37:111, 107:194]
        img[0:74, 0:87] = watch_face

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_3(self):
        img = cv2.imread('C:\Users\Brave\Downloads\lel336.jpg', cv2.IMREAD_COLOR)

        img[55, 55] = [255, 255, 255]
        px = img[55, 55]

        img[100:150, 100:150] = [255, 255, 255]

        watch_face = img[37:111, 107:194]
        img[0:74, 0:87] = watch_face

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_4(self):
        img1 = cv2.imread('C:\Users\Brave\Downloads\\3D-Matplotlib.png')
        img2 = cv2.imread('C:\Users\Brave\Downloads\mainlogo.png')

        rows, cols, channels = img2.shape
        roi = img1[0:rows, 0:cols]

        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

        mask_inv = cv2.bitwise_not(mask)

        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

        dst = cv2.add(img1_bg, img2_fg)
        img1[0:rows, 0:cols] = dst

        cv2.imshow('res', img1)
        cv2.imshow('mask_inv', mask_inv)
        cv2.imshow('img1_bg', img1_bg)
        cv2.imshow('img2_fg', img2_fg)
        cv2.imshow('dst', dst)

        # add = img1 + img2
        # add = cv2.add(img1, img2)
        # weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

        # cv2.imshow('mask', mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_5(self):
        img = cv2.imread('C:\Users\Brave\Downloads\\blocks1.jpg')
        retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

        grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
        gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        retval2, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imshow('original', img)
        cv2.imshow('threshold', threshold)
        cv2.imshow('threshold2', threshold2)
        cv2.imshow('gaus', gaus)
        cv2.imshow('otsu', otsu)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_6(self):
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # hsv hue sat value
            lower_red = np.array([0, 140, 100])
            upper_red = np.array([255, 255, 255])

            mask = cv2.inRange(hsv, lower_red, upper_red)
            res = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()

    def test_7(self):
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            cvtColor(bgr, hsv, COLOR_BGR2HSV);
            # hsv hue sat value
            lower_red = np.array([0, 200, 120])
            upper_red = np.array([255, 255, 255])

            maskR = cv2.inRange(hsv, lower_red, upper_red)
            resR = cv2.bitwise_and(frame, frame, mask=maskR)

            kernel = np.ones((15, 15), np.float32) / 225
            smoothed = cv2.filter2D(resR, -1, kernel)

            blur = cv2.GaussianBlur(resR, (15, 15), 0)
            median = cv2.medianBlur(resR, 15)
            bilateral = cv2.bilateralFilter(resR, 15, 75, 75)

            cv2.imshow('frame', frame)
            # cv2.imshow('mask', mask)
            cv2.imshow('res', resR)
            # cv2.imshow('smoothed', smoothed)
            cv2.imshow('blur', blur)
            cv2.imshow('median', median)
            cv2.imshow('bilateral', bilateral)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()

    def test_8(self):
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # hsv hue sat value
            lower_red = np.array([0, 140, 100])
            upper_red = np.array([255, 255, 255])

            mask = cv2.inRange(hsv, lower_red, upper_red)
            res = cv2.bitwise_and(frame, frame, mask=mask)

            kernel = np.ones((5, 5), np.uint8)
            erosion = cv2.erode(mask, kernel, iterations=1)
            dilation = cv2.dilate(mask, kernel, iterations=1)

            opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            cv2.imshow('frame', frame)
            cv2.imshow('res', res)
            cv2.imshow('erosion', erosion)
            cv2.imshow('dilation', dilation)
            cv2.imshow('opening', opening)
            cv2.imshow('closing', closing)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()

    def test_9(self):
        cap = cv2.VideoCapture(0)

        while True:
            _, frame = cap.read()

            laplacian = cv2.Laplacian(frame, cv2.CV_64F)
            sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
            edges = cv2.Canny(frame, 100, 100)

            cv2.imshow('original', frame)
            cv2.imshow('laplacian', laplacian)
            cv2.imshow('sobelx', sobelx)
            cv2.imshow('sobely', sobely)
            cv2.imshow('edges', edges)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
        cap.release()

    def test_10(self):
        img_bgr = cv2.imread('C:\Users\Brave\Downloads\\blocks\\blocks.jpg')
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        template = cv2.imread('C:\Users\Brave\Downloads\\blocks\\blueb1.jpg', 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

        cv2.imshow('detected', img_bgr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_11(self):
        img = cv2.imread('C:\Users\Brave\Downloads\\blocks1.jpg')
        mask = np.zeros(img.shape[:2], np.uint8)

        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        rect = (50, 50, 300, 500)

        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = img * mask2[:, :, np.newaxis]
        plt.imshow(img)
        plt.colorbar()
        plt.show()
    def test_12(self):
        img = cv2.imread('C:\Users\Brave\Downloads\\blocks1.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

        corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
        corners = np.int0(corners)

        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(img, (x, y), 3, 255, -1)

        cv2.imshow('Corner', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def test_13(self):
        img1 = cv2.imread('C:\Users\Brave\Downloads\\blocks\\blocks.jpg', 0)
        img2 = cv2.imread('C:\Users\Brave\Downloads\\blocks\\blueb1.jpg', 0)

        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)

        img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
        plt.imshow(img3)
        plt.show()
    def test_14(self):
        cap = cv2.VideoCapture('C:\Users\Brave\Downloads\people-walking.mp4')
        fgbg = cv2.createBackgroundSubtractorMOG2()

        while True:
            ret, frame = cap.read()
            fgmask = fgbg.apply(frame)

            cv2.imshow('original', frame)
            cv2.imshow('fg', fgmask)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
    def test_15(self):
        face_cascade = cv2.CascadeClassifier('C:\Users\Brave\Downloads\haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('C:\Users\Brave\Downloads\haarcascade_eye.xml')

        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
    def test_16(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True,
                        help="C:\Users\Brave\Downloads\shapes_and_colors")
        args = vars(ap.parse_args())

        image = cv2.imread(args["C:\Users\Brave\Downloads\shapes_and_colors"])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)[1]

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        for c in cnts:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(image, "center", (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            cv2.imshow("Image", image)
            cv2.waitKey(0)



if __name__ == '_camera_':
    unittest.main()
