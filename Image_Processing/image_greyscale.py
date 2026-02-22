import cv2
import numpy

img = cv2.imread("D:\Studies\Projects\Python\AI-ML-DL\Image_Processing\MainBefore.jpg", 0) 
print(img.shape)   
print(img[0][0]) 

print(img)

cv2.imshow("Image", img)
cv2.waitKey(0)