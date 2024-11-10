import cv2
from PIL import Image
import numpy as np


# Load an image using OpenCV
# Change this to your image path
image_path = '/Users/mohamadfarismohdjaafar/Downloads/cake.jpg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Display the original image
    # cv2.imshow('Original Image', image)

    # # Convert the image to grayscale
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # Apply Gaussian blur
    # blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # # Save the processed image
    # cv2.imwrite('blurred_image.jpg', blurred_image)

    # # Convert the blurred image to a format that Pillow can use and show it
    # pil_image = Image.fromarray(blurred_image)
    # pil_image.show()

    # Wait for a key press and close all OpenCV windows
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 1. Image Resizing
    # Resize the image to half of its original dimensions
    resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
    cv2.imshow('Resized Image', resized_image)

    # 2. Edge Detection
    # Convert the image to grayscale for edge detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 50, 100)
    cv2.imshow('Edge Detection', edges)

    # 3. Image Thresholding
    # Apply binary thresholding
    _, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Thresholded Image', thresholded_image)

    # Wait for a key press and close all OpenCV windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
