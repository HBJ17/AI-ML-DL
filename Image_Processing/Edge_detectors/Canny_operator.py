import cv2
import numpy as np

img = cv2.imread("D:\Studies\Projects\Python\AI-ML-DL\Image_Processing\MainBefore.jpg", 0)

edges = cv2.Canny(img, 100, 200)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
