import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)

equalized = cv2.equalizeHist(img)

cv2.imshow("Equalized", equalized)
cv2.waitKey(0)


