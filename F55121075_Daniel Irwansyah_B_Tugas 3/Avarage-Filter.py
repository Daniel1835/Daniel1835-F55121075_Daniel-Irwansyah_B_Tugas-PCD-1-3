import cv2
import numpy as np

image = cv2.imread('2.jpg')

kernel_size = 5

kernel = np.ones((kernel_size, kernel_size), np.float32) / kernel_size**2

filtered_image = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()