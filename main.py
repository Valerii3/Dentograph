import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
'''
cv2.namedWindow("frame")

cv2.createTrackbar("HL", "frame", 0, 180, nothing)
cv2.createTrackbar("SL", "frame", 0, 255, nothing)
cv2.createTrackbar("VL", "frame", 0, 255, nothing)

cv2.createTrackbar("H", "frame", 0, 180, nothing)
cv2.createTrackbar("S", "frame", 0, 255, nothing)
cv2.createTrackbar("V", "frame", 0, 255, nothing)
'''


while True:
    success, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    '''
    hl = cv2.getTrackbarPos("HL", "frame")
    sl = cv2.getTrackbarPos("SL", "frame")
    vl = cv2.getTrackbarPos("VL", "frame")

    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")
    '''
    hl = 66   # blue marker
    sl = 64
    vl = 0
    h = 119
    s = 255
    v = 255
    lower = np.array([hl,sl,vl])
    upper = np.array([h,s,v])
    mask = cv2.inRange(hsv, lower, upper)


    res = cv2.bitwise_and(img, img, mask=mask )
   # cv2.imshow("frame", img)
  #  cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break