import numpy as np
import cv2
import matplotlib.pyplot as plt


# Display an image
def displayImage():
    # testImage = cv2.imread("../Test\ Images/Pokemon\ AG\ anime\ 1.png")
    testImage = cv2.imread("../Test Images/Pokemon AG anime 1.png")
    # cv2.namedWindow("Window name")    # This line is not required.
    cv2.imshow("Window name", testImage)
    cv2.waitKey(0)    # Press any key to continue.

displayImage()
