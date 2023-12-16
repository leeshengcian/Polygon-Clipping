import math
# import pytest
import numpy as np
import matplotlib.pyplot as plt
import clipper

poly_size = 3
poly_points = np.array([[100,150], [200,250], [300,200]])

clipper_size = 4
clipper_points = np.array([[100,300], [300,300], [200,100]])

clipped = clipper.clipPolygons(poly_points, clipper_points)
for i in range(clipped.shape[0]):
    print("(", clipped[i][0], ",", clipped[i][1], ")")
plt.figure(figsize=(8, 8))

# Plotting the original polygon edges
original_x = poly_points[:, 0]
original_y = poly_points[:, 1]
plt.fill(original_x, original_y, color='blue', alpha=0.5, label='Original Polygon')

# Plotting the clipper polygon edges
clipper_x = clipper_points[:, 0]
clipper_y = clipper_points[:, 1]
plt.fill(clipper_x, clipper_y, color='yellow', alpha=0.5, label='Clipper Polygon')

# Highlight the clipped polygon
clipped_x = clipped[:, 0]
clipped_y = clipped[:, 1]
plt.fill(clipped_x, clipped_y, color='black', alpha=0.5, label='Clipped Polygon')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polygon Clipping Visualization')

# Show legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()