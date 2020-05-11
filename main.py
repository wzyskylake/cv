from imutils import paths
import numpy as np
import imutils
import cv2

KNOWN_DISTANCE = 500.00
KNOWN_WIDTH = 125.0

video = 'http://s10:990516@192.168.3.8:8080/video'
photo = 'http://s10:990516@192.168.3.8:8080/shot.jpg'

np1 = np.array([1, 1], np.int32, ndmin=2)
np2 = np.array([1, 2], np.int32, ndmin=2)
np3 = np.array([2, 2], np.int32, ndmin=2)
np4 = np.array([2, 1], np.int32, ndmin=2)
npa = np.array([np1, np2, np3, np4], np.int32)


def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 1, 255)

    # the contour of paper is not closed, so apply close operation(dilate and erode)
    kernel = np.ones((3, 3), np.uint8)
    close = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    cnts = cv2.findContours(close.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts.append(npa)
    c = max(cnts, key=cv2.contourArea)

    # compute the bounding box of the of the paper region and return it
    return cv2.minAreaRect(c)


def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth


reference = cv2.imread("./reference.jpg")
marker = find_marker(reference)
width_r = min(marker[1][0], marker[1][1])
focalLength = (width_r * KNOWN_DISTANCE) / KNOWN_WIDTH

# cap = cv2.VideoCapture(video)

while True:
    cap = cv2.VideoCapture(photo)
    ret, img = cap.read()
    marker = find_marker(img)
    width_w = min(marker[1][1], marker[1][0])
    distance = distance_to_camera(KNOWN_WIDTH, focalLength, width_w)

    box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
    box = np.int0(box)
    cv2.drawContours(img, [box], -1, (0, 255, 0), 2)
    cv2.putText(img, str(distance), (50, 300), 1, 20, (0, 255, 0), 10, 8)
    cv2.imshow('distance test', cv2.resize(img, (800, 600)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

# cv2.imshow('ok',cv2.resize(img,(300,400)))


cv2.waitKey(0)

cv2.destroyAllWindows()
