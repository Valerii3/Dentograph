import cv2
import numpy as np
import time
from clients_db import add_file_path

def createPath( img ):
    h, w = img.shape[:2]
    return np.zeros((h, w, 3), np.uint8)

def nothing(x):
    pass

kernel=np.ones((5,5), np.uint8)

def detect(file_name, name_, surname_):
    file = file_name  # путь к файлу с картинкой
    cap = cv2.VideoCapture(file)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#out = cv2.VideoWriter('captured_full.mp4', -1, 30, size)
#out1 = cv2.VideoWriter('opening.mp4', -1, 30, size)
#out2 = cv2.VideoWriter('mask.mp4', -1, 30, size)
#out3 = cv2.VideoWriter('erosion.mp4', -1, 30, size)
#out4 = cv2.VideoWriter('dilesion.mp4', -1, 30, size)
#out5 = cv2.VideoWriter('final.mp4', -1, 30, size)
#out6 = cv2.VideoWriter('zvet.mp4', -1, 30, size)

    output_file = file.replace(".mp4", "_line_trajectory.avi")
    add_file_path(output_file, name_, surname_)
    out7 = cv2.VideoWriter(output_file, -1, 30, size)

    x = 0
    y = 0
    lastx = 0
    lasty = 0
    path_color = (0,0,255)

    flag, img = cap.read()
    path = createPath(img)



    while True:
        ret, img = cap.read()
        test = np.zeros((size[1], size[0], 3), dtype=np.uint8)
        if (ret == 0):
            break

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        '''
            hl = cv2.getTrackbarPos("HL", "frame")
            sl = cv2.getTrackbarPos("SL", "frame")
            vl = cv2.getTrackbarPos("VL", "frame")

            h = cv2.getTrackbarPos("H", "frame")
            s = cv2.getTrackbarPos("S", "frame")
            v = cv2.getTrackbarPos("V", "frame")
            '''
        hl = 148  # blue marker
        sl = 81
        vl = 88
        h = 162
        s = 255
        v = 255

        lower = np.array([hl, sl, vl])
        upper = np.array([h, s, v])
        img=cv2.bilateralFilter(img, 9, 75, 75)
        mask = cv2.inRange(hsv, lower, upper)

        moments = cv2.moments(mask, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']

        edge = cv2.Canny(mask, 100, 200)

        countours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        countours = sorted(countours, key=cv2.contourArea, reverse=True)

        try:
            cv2.drawContours(img, [countours[0]], -1, (255, 0, 0), 5)
        except Exception:
            print()

        erosion = cv2.erode(mask, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)

        if dArea > 1000:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(closing, (x, y), 5, (0, 0, 255), -1)
        if lastx > 0 and lasty > 0:
            cv2.line(path, (lastx, lasty), (x, y), path_color, 2)
        lastx = x
        lasty = y

        #   img = cv2.add(img, path)
        test = cv2.add(test, path)



        #res = cv2.bitwise_and(img, img, mask=closing)

  #  out.write(closing)
  #  out1.write(opening)
  #  out2.write(mask)
  #  out3.write(erosion)
  #  out4.write(dilation)
  #  out5.write(img)
        out7.write(test)
   # out6.write(res)
 #   cv2.imshow("hsv", mask)




        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
