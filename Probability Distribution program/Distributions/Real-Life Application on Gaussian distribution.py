
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the noisy image
image = cv2.imread('noisy_image.png', 0)  # Grayscale image

# Add Gaussian noise to the image
mean = 0
std_dev = 50
noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, noise)

# Apply Gaussian blur to denoise the image
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

# Display the original, noisy, and denoised images
plt.figure(figsize=(10, 8))
plt.subplot(131), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.axis('off')
plt.subplot(132), plt.imshow(noisy_image, cmap='gray')
plt.title('Noisy Image'), plt.axis('off')
plt.subplot(133), plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image'), plt.axis('off')
plt.tight_layout()
plt.show()
