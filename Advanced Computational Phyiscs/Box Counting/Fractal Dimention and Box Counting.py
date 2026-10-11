import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the range of box sizes you want to consider
max_box_size = min(image.shape)
box_sizes = 2**np.arange(0, int(np.log2(max_box_size)))

# Initialize an array to store the number of black pixels for each box size
black_pixel_counts = []

# Iterate through each box size
for box_size in box_sizes:
    # Create a copy of the original image to work with
    image_copy = image.copy()

    # Divide the image into a grid of boxes with the current size
    for i in range(0, image.shape[0], box_size):
        for j in range(0, image.shape[1], box_size):
            # Calculate the number of black pixels within the box
            box = image[i:i+box_size, j:j+box_size]
            black_pixel_count = np.sum(box == 0)
            # Add the count to the list
            black_pixel_counts.append(black_pixel_count)

# Calculate the fractal dimension using a linear fit to the log-log plot
x = np.log(box_sizes)
y = np.log(black_pixel_counts)
slope, _ = np.polyfit(x, y, 1)

# Plot the log-log graph
plt.figure()
plt.loglog(box_sizes, black_pixel_counts, 'bo-')
plt.title(f'Fractal Dimension (Slope): {slope:.2f}')
plt.xlabel('Box Size (log scale)')
plt.ylabel('Number of Black Pixels (log scale)')
plt.grid(True)
plt.show()
