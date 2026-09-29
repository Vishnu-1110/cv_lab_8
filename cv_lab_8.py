import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_filtering(img, kernel, p, s):
    m, n = img.shape
    x, y = kernel.shape

    if p != 0:
        padded_img = np.pad(img, p, 'constant')
    else:
        padded_img = img

    m = int((padded_img.shape[0] - x + 2 * p) / s) + 1
    n = int((padded_img.shape[1] - y + 2 * p) / s) + 1

    filtered_img = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            filtered_img[i, j] = np.sum(
                kernel * padded_img[i * s:i * s + x, j * s:j * s + y]
            )

    return filtered_img


# Read image in grayscale
img = cv2.imread("dove.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found")
else:
    k_s = 9

    # Mean filter kernel
    kernel = np.ones((k_s, k_s), dtype=np.float32) / (k_s * k_s)

    # Apply filtering
    filtered_image = image_filtering(img, kernel, 0, 1)

    # Display original and filtered images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original")
    plt.axis("on")

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap="gray")
    plt.title("Filtered")
    plt.axis("on")

    plt.tight_layout()
    plt.show()

    print("Original size:", img.shape)
    print("Filtered size:", filtered_image.shape)
