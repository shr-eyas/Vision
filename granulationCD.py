import cv2  # type: ignore
import matplotlib.pyplot as plt
import numpy as np 

# Load the image in grayscale
image = cv2.imread('images/satellite.png', cv2.IMREAD_GRAYSCALE)

# Define the alpha values (class centers) for the Water and Land classes
alphaWater = 80  # Center of the Water class
alphaLand = 140  # Center of the Land class

# Define a function to calculate membership based on the π-type function
def calculateMembershipCD(pixelValue, alpha):
    # Safeguard against division by zero if alpha is 0
    if alpha == 0:
        return 0
    
    # Calculate the normalized difference and ensure it is within 0 and 1
    diff = abs(pixelValue - alpha) / alpha
    diff = min(max(diff, 0), 1)  # Clamp diff between 0 and 1 to avoid overflow
    
    # Apply the π-type membership function
    if 0 <= diff <= 0.5:
        return 2 * (1 - diff) ** 2
    elif 0.5 < diff <= 1:
        return 1 - 2 * (diff) ** 2
    else:
        return 0

# Apply CD granulation to each pixel in the image for Water and Land classes
membershipWater = np.zeros_like(image, dtype=np.float32)
membershipLand = np.zeros_like(image, dtype=np.float32)

# Calculate memberships for each pixel in the image
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        pixelValue = image[i, j]
        membershipWater[i, j] = calculateMembershipCD(pixelValue, alphaWater)
        membershipLand[i, j] = calculateMembershipCD(pixelValue, alphaLand)

# Display the membership maps
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.imshow(membershipWater, cmap="Blues")
plt.title("Water Membership")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(membershipLand, cmap="YlGn")
plt.title("Land Membership")
plt.axis("off")

plt.show()
