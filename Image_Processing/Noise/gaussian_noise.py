import cv2
import numpy as np

img = cv2.imread("Image_Processing\MainBefore.jpg", 0)
noise = np.random.normal(0, 20, img.shape)
noisy = img + noise

noisy = np.clip(noisy, 0, 255).astype(np.uint8)
cv2.imshow("Gaussian Noise", noisy)
cv2.waitKey(0)
