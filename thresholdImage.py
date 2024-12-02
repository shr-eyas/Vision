import cv2  # type: ignore
import numpy as np
import matplotlib.pyplot as plt

def thresholdSelection(image, m, n):
    minGray = int(image.min())
    maxGray = int(image.max())
    size = maxGray - minGray + 1
    objectL = np.zeros(size, dtype=int)
    objectU = np.zeros(size, dtype=int)
    backgroundL = np.zeros(size, dtype=int)
    backgroundU = np.zeros(size, dtype=int)

    granules = [
        image[i:i + m, j:j + n]
        for i in range(0, image.shape[0], m)
        for j in range(0, image.shape[1], n)
    ]

    for granule in granules:
        maxGranule = int(granule.max())
        minGranule = int(granule.min())

        for j in range(maxGranule, maxGray + 1):
            objectL[j - minGray] += 1
        for j in range(minGranule, maxGray + 1):
            objectU[j - minGray] += 1
        for j in range(minGray, minGranule + 1):
            backgroundL[j - minGray] += 1
        for j in range(minGray, maxGranule + 1):
            backgroundU[j - minGray] += 1

    roughEntropy = np.zeros(size)
    for l in range(minGray, maxGray + 1):
        idx = l - minGray
        objectRoughness = 1 - (objectL[idx] / objectU[idx] if objectU[idx] != 0 else 1)
        backgroundRoughness = 1 - (backgroundL[idx] / backgroundU[idx] if backgroundU[idx] != 0 else 1)

        if objectRoughness > 0 and backgroundRoughness > 0:
            roughEntropy[idx] = -0.5 * (
                objectRoughness * np.log(objectRoughness) +
                backgroundRoughness * np.log(backgroundRoughness)
            )

    optimalThreshold = minGray + np.argmax(roughEntropy)
    return optimalThreshold


# Load the original color image
original_image = cv2.imread('images/plant.png')

# Convert the image to grayscale for thresholding purposes
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Get the optimal threshold using rough entropy
m, n = 5, 5
roughEntropyThreshold = thresholdSelection(gray_image, m, n)

# Apply Otsu's thresholding to the grayscale image
_, otsuThresholded = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply rough entropy thresholding to the grayscale image
roughEntropyThresholded = np.where(gray_image >= roughEntropyThreshold, 255, 0).astype(np.uint8)

# Plot the results
plt.figure(figsize=(12, 6))

# Original color image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))  # Convert to RGB for displaying in matplotlib
plt.title("Original Image")
plt.axis("off")

# Otsu's thresholded image
plt.subplot(1, 3, 2)
plt.imshow(otsuThresholded, cmap="gray")
plt.title("Otsu's Thresholding")
plt.axis("off")

# Rough entropy thresholded image
plt.subplot(1, 3, 3)
plt.imshow(roughEntropyThresholded, cmap="gray")
plt.title("Rough Entropy Thresholding")
plt.axis("off")

plt.tight_layout()
plt.show()
