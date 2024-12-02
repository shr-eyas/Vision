import cv2  # type: ignore
import matplotlib.pyplot as plt
import numpy as np

# Load the image in grayscale
image = cv2.imread('images/satellite.png', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Display the image using matplotlib
    plt.imshow(image, cmap='gray')  # Use 'gray' colormap for grayscale images
    plt.axis('off')  # Hide axes
    plt.show()
