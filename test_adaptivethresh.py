import cv2
import numpy as np

# Load the image
image = cv2.imread('zf_testimg2.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise reduction with Gaussian Blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Adaptive thresholding
adaptive_threshold_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours in the noise-reduced image
contours, _ = cv2.findContours(adaptive_threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Find the largest contour in the list of contours
largest_contour = max(contours, key=cv2.contourArea)

# Draw contours and bounding rectangle on the original image
cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)
x, y, w, h = cv2.boundingRect(largest_contour)
cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Convert array to grayscale for fluorescence detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to detect fluorescence
_, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Calculate the percentage of pixels that are fluorescent
fluorescent_pixels = np.count_nonzero(binary)
total_pixels = image.shape[0] * image.shape[1]
fluorescence_level = (fluorescent_pixels / total_pixels) * 100

# Display the original image with contours
cv2.imshow('Fluorescent Level: {:.2f}%'.format(fluorescence_level), image)
cv2.waitKey(0)
cv2.destroyAllWindows()
