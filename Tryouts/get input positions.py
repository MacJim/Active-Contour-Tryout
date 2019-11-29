import numpy as np
import cv2


inputPositions = []

def mouseCallback(event, x, y, flags, param):
    if (event == cv2.EVENT_LBUTTONDOWN):
        print(x, y)

testImage = cv2.imread("../Test Images/Pokemon AG anime 1.png")
cv2.imshow("Window name", testImage)
cv2.setMouseCallback("Window name", mouseCallback)
cv2.waitKey(0)
