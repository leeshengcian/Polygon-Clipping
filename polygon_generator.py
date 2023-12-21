import numpy as np

def generate_simple_polygon_array(num_vertices, side_length=10):
    # Generate random angles for the vertices
    angles = np.sort(np.random.rand(num_vertices) * 2 * np.pi)[::-1]

    # Calculate x and y coordinates based on angles
    x = side_length * np.cos(angles)
    y = side_length * np.sin(angles)

    # Shift the coordinates to ensure they are positive
    x_shift = np.min(x)
    y_shift = np.min(y)
    x -= x_shift
    y -= y_shift

    # Combine x and y coordinates to form the vertices
    vertices = np.column_stack((x, y))
    # vertices = np.vstack((vertices, vertices[0]))

    return vertices

def save_polygons_to_txt(polygons, filename='polygons.txt'):
    # Save the polygons to a text file
    with open(filename, 'w') as file:
        for polygon in polygons:
            for vertex in polygon:
                file.write(f"{vertex[0]}, {vertex[1]}\n")
            file.write('\n')  # Add a blank line between polygons

# Generate two simple polygons, each with 10 vertices
polygon1 = generate_simple_polygon_array(6)
polygon2 = generate_simple_polygon_array(100000)

# Save the polygons to a text file
save_polygons_to_txt([polygon1, polygon2], 'polygons.txt')