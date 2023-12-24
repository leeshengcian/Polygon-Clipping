import math
# import pytest
import numpy as np
import matplotlib.pyplot as plt
import clipper
import simclipper
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

# Test simple data
# poly_points = np.array([[200,200],[175,200],[150,150],[150,200],[125,200],[175,250],[200,220],[250,250],[300,200],[250,225],[250,175],[200,150]])
# clipper_points = np.array([[100,300],[300,300],[200,100]])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
# Plotting the original polygon edges
original_x = poly_points[:, 0]
original_y = poly_points[:, 1]
plt.fill(original_x, original_y, color='blue', alpha=0.5, label='Original Polygon')

# Set a Timer to record computation time
start_time = time.time()

# Perfrom Complex Polygon Clipping
clipped = clipper.clipPolygons(poly_points, clipper_points)

end_time = time.time()
elapsed_time = end_time - start_time

# print(poly_points)
# print("Complex Clipped Polygon is " , clipped.shape[0] , " edges Polygon")
# print(f"Elapsed time for complex clipping is: {elapsed_time:.8f} seconds")

# Plotting the clipper polygon edges
clipper_x = clipper_points[:, 0]
clipper_y = clipper_points[:, 1]
plt.fill(clipper_x, clipper_y, color='yellow', alpha=0.5, label='Clipper Polygon')

# Highlight the clipped polygon
clipped_x = clipped[:, 0]
clipped_y = clipped[:, 1]
plt.fill(clipped_x, clipped_y, color='red', alpha=0.5, label='Clipped Polygon')

# Set labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
plt.title('Complex Polygon Clipping Visualization')
plt.annotate(f'Number of Edges: {clipped.shape[0]}', xy=(0.5, -0.2), xycoords='axes fraction', ha='center')
plt.annotate(f'Runtime: {elapsed_time:.8f} seconds', xy=(0.5, -0.15), xycoords='axes fraction', ha='center')

# Show legend
plt.legend()
plt.grid(True)
# plt.show()

# Read two polygons from the 'polygons.txt' file
polygons = read_polygons_from_txt()

# Assign the polygons to poly_points and clipper_points
poly_points, clipper_points = polygons

plt.subplot(1, 2, 2)
# Plotting the original polygon edges
original_x = poly_points[:, 0]
original_y = poly_points[:, 1]
plt.fill(original_x, original_y, color='blue', alpha=0.5, label='Original Polygon')

# Set a Timer to record computation time
start_time = time.time()

# Perfrom Simple Polygon Clipping
sim_clipped = simclipper.simclipPolygons(poly_points, clipper_points)

end_time = time.time()
elapsed_time = end_time - start_time

# print(poly_points)
# print("Simple Clipped Polygon is " , sim_clipped.shape[0] , " edges Polygon")
# print(f"Elapsed time for simple clipping is: {elapsed_time:.8f} seconds")

# Plotting the clipper polygon edges
clipper_x = clipper_points[:, 0]
clipper_y = clipper_points[:, 1]
plt.fill(clipper_x, clipper_y, color='yellow', alpha=0.5, label='Clipper Polygon')

# Highlight the clipped polygon
sim_clipped_x = sim_clipped[:, 0]
sim_clipped_y = sim_clipped[:, 1]
plt.fill(sim_clipped_x, sim_clipped_y, color='red', alpha=0.5, label='Clipped Polygon')

# Set labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
plt.title('Simple Polygon Clipping Visualization')
plt.annotate(f'Number of Edges: {sim_clipped.shape[0]}', xy=(0.5, -0.2), xycoords='axes fraction', ha='center')
plt.annotate(f'Runtime: {elapsed_time:.8f} seconds', xy=(0.5, -0.15), xycoords='axes fraction', ha='center')

plt.suptitle(f'When Clipper Polygons has {clipper_points.shape[0]} edges', fontsize=16)
# Show legend
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()