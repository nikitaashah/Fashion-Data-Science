# Reload required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image again
image_path = "/mnt/data/_ALE0007.webp"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Resize for processing efficiency
resized_image = cv2.resize(image, (200, 200))

# Convert image to grayscale for edge detection
gray = cv2.cvtColor(resized_image, cv2.COLOR_RGB2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Hough Line Transform to detect structured patterns (like plaid or stripes)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

# Create a copy to draw detected lines
line_img = resized_image.copy()

# Draw detected lines
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Fourier Transform for pattern frequency analysis
f = np.fft.fft2(gray)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# Display results
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original Image
axes[0].imshow(resized_image)
axes[0].set_title("Original Image")
axes[0].axis("off")

# Edge Detection
axes[1].imshow(edges, cmap='gray')
axes[1].set_title("Edge Detection (Canny)")
axes[1].axis("off")

# Fourier Spectrum
axes[2].imshow(magnitude_spectrum, cmap='gray')
axes[2].set_title("Fourier Transform (Pattern Analysis)")
axes[2].axis("off")

plt.show()

# Pattern Classification based on Hough Transform
if lines is not None and len(lines) > 20:
    detected_pattern = "Plaid (Grid-like pattern detected)"
elif lines is not None and len(lines) < 10:
    detected_pattern = "Striped (Linear patterns detected)"
else:
    detected_pattern = "Complex pattern (Possible tweed or mixed fabric)"

detected_pattern

# Result
# 'Complex pattern (Possible tweed or mixed fabric)'
