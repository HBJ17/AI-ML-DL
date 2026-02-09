import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("Image_Processing\MainBefore.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found")
    exit()

# Sobel gradients
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Gradient magnitude
edges = np.sqrt(sobelx**2 + sobely**2)

# Normalize to 0–255
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)
edges = edges.astype(np.uint8)

# Display
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
