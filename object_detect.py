import cv2
import numpy as np

kernal = np.ones((3,3), np.uint8)

def empty(x):
    pass

vdo = cv2.VideoCapture(1)

cv2.namedWindow("settings")
cv2.createTrackbar("Size", "settings", 100, 1000, empty)
cv2.createTrackbar("sigma_X" ,"settings", 10, 100, empty)
cv2.createTrackbar("sigma_Y" ,"settings", 10, 100, empty)
cv2.createTrackbar("Threshold 1" ,"settings", 44, 500, empty)
cv2.createTrackbar("Threshold 2" ,"settings", 61, 500, empty)
cv2.createTrackbar("MinArea", "settings", 500, 10000, empty)


while True:
    _, img = vdo.read()

    s = cv2.getTrackbarPos("Size", "settings")
    img = cv2.resize(img, (s,s))

    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x = cv2.getTrackbarPos("sigma_X", "settings")
    y = cv2.getTrackbarPos("sigma_Y", "settings")
    t1 = cv2.getTrackbarPos("Threshold 1", "settings")
    t2 =cv2.getTrackbarPos("Threshold 2", "settings")
    area = cv2.getTrackbarPos("MinArea", "settings")

    imgblur = cv2.GaussianBlur(imggray, (5,5), x, y)

    imgcanny = cv2.Canny(imgblur, t1,t2)

    imgdailate = cv2.dilate(imgcanny, kernal, iterations=1)

    contours, _ = cv2.findContours(imgdailate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > area:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)

            x,y,w,h = cv2.boundingRect(approx)

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 4)
            cv2.putText(img, f"Coordinates :({x,y})", (x+w,y), cv2.FONT_ITALIC, 0.7, (0,255,0), 2)

    

    cv2.imshow("Img with contours",img)
    cv2.imshow("Canny Image", imgcanny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vdo.release()
cv2.destroyAllWindows()

