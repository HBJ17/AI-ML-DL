import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)

plt.hist(img.ravel(), 256, [0,256])
plt.show()
