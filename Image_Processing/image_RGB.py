import cv2

img = cv2.imread("MainBefore.jpg", 0)  

print(img[50][100])   
img[50][100] = 255    

cv2.imshow("Image", img)
cv2.waitKey(0)

