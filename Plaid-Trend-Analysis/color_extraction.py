# Reload required libraries without GLCM for now
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the image
image_path = "/mnt/data/_ALE0007.webp"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Resize for faster processing
resized_image = cv2.resize(image, (200, 200))

# Reshape image to a 2D array of pixels for clustering
pixels = resized_image.reshape(-1, 3)

# KMeans clustering for dominant colors
k = 5  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans.fit(pixels)
dominant_colors = kmeans.cluster_centers_.astype(int)

# Create a color palette
palette = np.zeros((50, 300, 3), dtype=np.uint8)
step = 300 // k
for i, color in enumerate(dominant_colors):
    palette[:, i * step:(i + 1) * step] = color

# Display results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Original Image
axes[0].imshow(resized_image)
axes[0].set_title("Resized Image")
axes[0].axis("off")

# Dominant Colors
axes[1].imshow(palette)
axes[1].set_title("Dominant Colors")
axes[1].axis("off")

plt.show()

# Return dominant colors as HEX codes
dominant_colors_hex = ['#{:02x}{:02x}{:02x}'.format(*color) for color in dominant_colors]
dominant_colors_hex
