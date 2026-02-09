import cv2

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)
blur = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("Gaussian Filter", blur)
cv2.waitKey(0)


