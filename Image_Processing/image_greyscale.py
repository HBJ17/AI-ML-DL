import cv2
import numpy

img = cv2.imread("MainBefore.jpg", 1) 
print(img.shape)   
print(img[0][0]) 

print(img)

cv2.imshow("Image", img)
cv2.waitKey(0)