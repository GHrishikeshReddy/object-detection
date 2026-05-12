import cv2
import numpy as np

def empty(x):
    pass

vdo = cv2.VideoCapture(0)

cv2.namedWindow("settings")
cv2.createTrackbar("Size", "settings", 100, 1000, empty)
cv2.createTrackbar("sigma_X" ,"settings", 10, 10, empty)
cv2.createTrackbar("sigma_Y" ,"settings", 10, 10, empty)
cv2.createTrackbar("Threshold 1" ,"settings", 44, 500, empty)
cv2.createTrackbar("Threshold 2" ,"settings", 61, 500, empty)


while True:
    _, img = vdo.read()

    s = cv2.getTrackbarPos("Size", "settings")
    img = cv2.resize(img, (s,s))

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x = cv2.getTrackbarPos("sigma_X", "settings")
    y = cv2.getTrackbarPos("sigma_Y", "settings")
    t1 = cv2.getTrackbarPos("Threshold 1", "settings")
    t2 =cv2.getTrackbarPos("Threshold 2", "settings")

    imgblur = cv2.GaussianBlur(imggray, (5,5), x, y)

    imgcanny = cv2.Canny(imgblur, t1,t2)

    res = np.hstack((imggray, imgblur, imgcanny))
    cv2.imshow("set canny",res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vdo.release()
cv2.destroyAllWindows()

