import numpy as np
import cv2

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)
noisy = img.copy()

prob = 0.02
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r = np.random.rand()
        if r < prob:
            noisy[i][j] = 0
        elif r > 1 - prob:
            noisy[i][j] = 255

cv2.imshow("Salt & Pepper Noise", noisy)
cv2.waitKey(0)
