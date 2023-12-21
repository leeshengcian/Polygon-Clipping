// algorithm for polygon clipping
#include<iostream>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <utility>
#include <numeric>

const int MAX_POINTS = 100000;

// Returns x-value of point of intersection of two
// lines
double x_intersect(double x1, double y1, double x2, double y2,
				double x3, double y3, double x4, double y4)
{
	double num = (x1*y2 - y1*x2) * (x3-x4) -
			(x1-x2) * (x3*y4 - y3*x4);
	double den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4);
	return num/den;
}

// Returns y-value of point of intersection of
// two lines
double y_intersect(double x1, double y1, double x2, double y2,
				double x3, double y3, double x4, double y4)
{
	double num = (x1*y2 - y1*x2) * (y3-y4) -
			(y1-y2) * (x3*y4 - y3*x4);
	double den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4);
	return num/den;
}

// This functions clips all the edges w.r.t one clip
// edge of clipping area
void clip(double poly_points[][2], int &poly_size,
		double x1, double y1, double x2, double y2)
{
	double new_points[MAX_POINTS][2];
	int new_poly_size = 0;

	// std::cout << "Original polygon size is: " << poly_size << std::endl;
	// (ix,iy),(kx,ky) are the co-ordinate values of
	// the points
	for (int i = 0; i < poly_size; i++)
	{
		// i and k form a line in polygon
		int k = (i+1) % poly_size;
		double ix = poly_points[i][0], iy = poly_points[i][1];
		double kx = poly_points[k][0], ky = poly_points[k][1];

		// Calculating position of first point
		// w.r.t. clipper line
		double i_pos = (x2-x1) * (iy-y1) - (y2-y1) * (ix-x1);

		// Calculating position of second point
		// w.r.t. clipper line
		double k_pos = (x2-x1) * (ky-y1) - (y2-y1) * (kx-x1);
		// std::cout << "i_pos is: " << i_pos << std::endl;
		// std::cout << "k_pos is: " << k_pos << std::endl;

		// Case 1 : When both points are inside
		if (i_pos < 0 && k_pos < 0)
		{
			//Only second point is added
			new_points[new_poly_size][0] = kx;
			new_points[new_poly_size][1] = ky;
			new_poly_size++;
		}

		// Case 2: When only first point is outside
		else if (i_pos >= 0 && k_pos < 0)
		{
			// Point of intersection with edge
			// and the second point is added
			new_points[new_poly_size][0] = x_intersect(x1,
							y1, x2, y2, ix, iy, kx, ky);
			new_points[new_poly_size][1] = y_intersect(x1,
							y1, x2, y2, ix, iy, kx, ky);
			new_poly_size++;

			new_points[new_poly_size][0] = kx;
			new_points[new_poly_size][1] = ky;
			new_poly_size++;
		}

		// Case 3: When only second point is outside
		else if (i_pos < 0 && k_pos >= 0)
		{
			//Only point of intersection with edge is added
			new_points[new_poly_size][0] = x_intersect(x1,
							y1, x2, y2, ix, iy, kx, ky);
			new_points[new_poly_size][1] = y_intersect(x1,
							y1, x2, y2, ix, iy, kx, ky);
			new_poly_size++;
		}

		// Case 4: When both points are outside
		else
		{
			//No points are added
		}
	}

	// Copying new points into original array
	// and changing the no. of vertices
	poly_size = new_poly_size;
	// std::cout << "New polygon size is: " << poly_size << std::endl;
	for (int i = 0; i < poly_size; i++)
	{
		poly_points[i][0] = new_points[i][0];
		poly_points[i][1] = new_points[i][1];
	}
}

// Implements Sutherland–Hodgman algorithm
int suthHodgClip(double poly_points[][2], int poly_size,
				double clipper_points[][2], int clipper_size)
{
	//i and k are two consecutive indexes
	for (int i=0; i<clipper_size; i++)
	{
		int k = (i+1) % clipper_size;

		// We pass the current array of vertices, it's size
		// and the end points of the selected clipper line
		clip(poly_points, poly_size, clipper_points[i][0],
			clipper_points[i][1], clipper_points[k][0],
			clipper_points[k][1]);
	}

	return poly_size;
}

namespace py = pybind11;

py::array_t<double> clipPolygons(py::array_t<double> poly_points, py::array_t<double> clipper_points) {
    auto poly_points_ptr = poly_points.mutable_unchecked<2>();
    auto clipper_points_ptr = clipper_points.mutable_unchecked<2>();

    int poly_size = poly_points.shape(0);
    int clipper_size = clipper_points.shape(0);
	int clipped_size = 0;

    double poly_array[MAX_POINTS][2], clipper_array[MAX_POINTS][2];

    for (int i = 0; i < poly_size; ++i) {
        poly_array[i][0] = poly_points_ptr(i, 0);
        poly_array[i][1] = poly_points_ptr(i, 1);
    }

    for (int i = 0; i < clipper_size; ++i) {
        clipper_array[i][0] = clipper_points_ptr(i, 0);
        clipper_array[i][1] = clipper_points_ptr(i, 1);
    }

    clipped_size = suthHodgClip(poly_array, poly_size, clipper_array, clipper_size);

	// Create a NumPy array with the same data
    auto np_array = py::array_t<double>({clipped_size, 2});
    auto buffer_info = np_array.request();

	// Copy the data from the C++ array to the NumPy array
    double* ptr = static_cast<double*>(buffer_info.ptr);
    for (size_t i = 0; i < clipped_size; ++i) {
        for (size_t j = 0; j < 2; ++j) {
            ptr[i * 2 + j] = poly_array[i][j];
        }
    }

    for (int i = 0; i < poly_size; ++i) {
        poly_points_ptr(i, 0) = poly_array[i][0];
        poly_points_ptr(i, 1) = poly_array[i][1];
    }

	return np_array;
}

PYBIND11_MODULE(clipper, m){
    m.doc() = "Polygon Clipping using Sutherland–Hodgman algorithm";
	m.def("clipPolygons", &clipPolygons, "Clip polygons using the Sutherland–Hodgman algorithm");
}
