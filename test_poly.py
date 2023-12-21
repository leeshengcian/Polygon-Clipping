import math
# import pytest
import numpy as np
import matplotlib.pyplot as plt
import clipper
import time

def read_polygons_from_txt(filename='polygons.txt'):
    polygons = []
    current_polygon = []

    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Check if the line is not empty
                x, y = map(float, line.split(','))
                current_polygon.append([x, y])
            else:
                # Add the current_polygon to the list and reset for the next polygon
                if current_polygon:
                    polygons.append(np.array(current_polygon))
                    current_polygon = []

    # Add the last polygon if any
    if current_polygon:
        polygons.append(np.array(current_polygon))

    # Ensure that exactly two polygons are read
    if len(polygons) != 2:
        raise ValueError("Expected exactly two polygons in the file.")

    return polygons

# Read two polygons from the 'polygons.txt' file
polygons = read_polygons_from_txt()

# Assign the polygons to poly_points and clipper_points
poly_points, clipper_points = polygons

plt.figure(figsize=(8, 8))
# Plotting the original polygon edges
original_x = poly_points[:, 0]
original_y = poly_points[:, 1]
plt.fill(original_x, original_y, color='blue', alpha=0.5, label='Original Polygon')

# Test simple data
# poly_points = np.array([[200,200],[175,200],[150,150],[150,200],[125,200],[175,250],[200,220],[250,250],[300,200],[250,225],[250,175],[200,150]])
# clipper_points = np.array([[100,300],[300,300],[200,100]])

# Set a Timer to record computation time
start_time = time.time()

# Perfrom Polygon Clipping
clipped = clipper.clipPolygons(poly_points, clipper_points)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")

# for i in range(clipped.shape[0]):
#     print("(", clipped[i][0], ",", clipped[i][1], ")")

# Plotting the clipper polygon edges
clipper_x = clipper_points[:, 0]
clipper_y = clipper_points[:, 1]
plt.fill(clipper_x, clipper_y, color='yellow', alpha=0.5, label='Clipper Polygon')

# Highlight the clipped polygon
clipped_x = clipped[:, 0]
clipped_y = clipped[:, 1]
plt.fill(clipped_x, clipped_y, color='red', alpha=0.5, label='Clipped Polygon')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polygon Clipping Visualization')

# Show legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()