# Apply texture analysis using Local Binary Patterns (LBP)
from skimage.feature import local_binary_pattern
from skimage.filters import sobel

# Convert image to grayscale again
gray_texture = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)

# Apply Local Binary Pattern (LBP) for texture extraction
radius = 3  # Neighborhood size
n_points = 8 * radius  # Number of sample points
lbp = local_binary_pattern(gray_texture, n_points, radius, method="uniform")

# Apply Sobel filter to enhance texture edges
sobel_texture = sobel(gray_texture)

# Display Texture Analysis results
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# LBP Texture Analysis
axes[0].imshow(lbp, cmap="gray")
axes[0].set_title("Local Binary Pattern (Texture Analysis)")
axes[0].axis("off")

# Sobel Filtered Texture
axes[1].imshow(sobel_texture, cmap="gray")
axes[1].set_title("Sobel Edge Detection (Texture Enhancement)")
axes[1].axis("off")

plt.show()

# Analyze texture roughness based on LBP variance
texture_variance = np.var(lbp)

# Classify fabric based on texture roughness
if texture_variance < 50:
    texture_type = "Smooth fabric (e.g., silk, cotton)"
elif 50 <= texture_variance < 150:
    texture_type = "Medium-textured fabric (e.g., wool, polyester blend)"
else:
    texture_type = "Highly textured fabric (e.g., tweed, boucle, rough wool)"

texture_type


# Result
# 'Medium-textured fabric (e.g., wool, polyester blend)'
