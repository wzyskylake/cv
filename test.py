from imutils import paths
import numpy as np
import imutils
import cv2

image = cv2.imread('./reference.jpg')

# convert the image to grayscale, blur it, and detect edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 35, 125)

# the contour of paper is not closed, so apply close operation(dilate and erode)
kernel = np.ones((3, 3), np.uint8)
close = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

# find the contours in the edged image and keep the largest one;
# we'll assume that this is our piece of paper in the image
cnts = cv2.findContours(close.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
np1 = np.array([1, 1], np.int32, ndmin=2)
np2 = np.array([1, 2], np.int32, ndmin=2)
np3 = np.array([2, 2], np.int32, ndmin=2)
np4 = np.array([2, 1], np.int32, ndmin=2)
npa = np.array([np1, np2, np3, np4], np.int32)

cnts.append(npa)
# max1=max(list,cnts)
max=max(cnts,key=cv2.contourArea)
# c = max(max1,max2)

print(type(cnts))
