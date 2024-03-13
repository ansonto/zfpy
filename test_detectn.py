'''
> a code to test out the contour function on a image <
set up virtual environment with 'python3 -m venv zfpy_vir'
remember to RUN in dedicated terminal in order to access the cv2 library in the virtual environment 
made chaanges to findCountours --> using RETR_tree instead 
this algorithm is called Otsu's binarization 
'''
import cv2
import numpy as np
import serial

# Code to load an image called 'zf_testimg'
image = cv2.imread('zf_testimg.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise reduction 
_, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, adaptive_threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the noise-reduced image
contours, _ = cv2.findContours(adaptive_threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour in the list of contours
largest_contour = max(contours, key=cv2.contourArea)

# Draw contours and bounding rectangle on the original image
cv2.drawContours(image, largest_contour, -1, (0, 255, 0), 2)
x, y, w, h = cv2.boundingRect(largest_contour)
cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

''' # Discard smaller objects and do not annotate the smaller objects in the image
for contour in contours:
    if cv2.contourArea(contour) < cv2.contourArea(largest_contour):
        cv2.drawContours(image, [contour], -1, (0, 0, 0), cv2.FILLED)
'''

## Detect fluo
## Ideally this only happens when it recognizes a 'valid' zebrafish 

# Convert array to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to detect fluorescence
_, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Calculate the percentage of pixels that are fluorescent
fluorescent_pixels = np.count_nonzero(binary)
total_pixels = image.shape[0] * image.shape[1]
fluorescence_level = (fluorescent_pixels / total_pixels) * 100

# Display the original image with contours
# imshow with the title of the window being the fluorescent level 
cv2.imshow('Fluorescent Level: {:.2f}%'.format(fluorescence_level), image)
cv2.waitKey(0)
cv2.destroyAllWindows()




