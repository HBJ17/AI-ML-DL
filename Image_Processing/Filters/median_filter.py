import cv2

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)
median = cv2.medianBlur(img, 5)

cv2.imshow("Median Filter", median)
cv2.waitKey(0)


