from imutils import paths
import numpy as np
import imutils
import cv2

cv2.namedWindow("camera", 1)
# 开启ip摄像头
video = 'http://s10:990516@192.168.3.8:8080/video'
photo = 'http://s10:990516@192.168.3.8:8080/shot.jpg' # 此处@后的ipv4 地址需要改为app提供的地址
cap = cv2.VideoCapture(photo)
ret,img = cap.read()
cv2.imwrite("reference.jpg",img)
# img=cv2.imread(photo)
# cv2.imshow('ok',cv2.resize(img,(800,450)))

# cv2.waitKey(0)

cv2.destroyAllWindows()


# while True:
#     # Start Camera, while true, camera will run
#
#     ret, image_np = cap.read()
#
#     # Set height and width of webcam
#     height = 600
#     width = 1000
#
#     # Set camera resolution and create a break function by pressing 'q'
#     cv2.imshow('object detection', cv2.resize(image_np, (width, height)))
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cap.release()
#         cv2.destroyAllWindows()
#         break
# # Clean up
# cap.release()
# cv2.destroyAllWindows()
