import cv2

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)
blur = cv2.blur(img, (3,3))

cv2.imshow("Mean Filter", blur)
cv2.waitKey(0)
