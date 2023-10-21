# Polygon-Clipping
This Proposal shows the work flow and plans for the 2023 Autumn NYCU NSD term project

## Basic Information

GitHub Link : [https://github.com/leeshengcian/Polygon-Clipping/tree/main]

Polygon clipping are important operations in algorithm design, especially for computer graphics, computer vision, and computational geometry.

Polygon clipping is the process of cutting off parts of a polygon that lie outside a given boundary.For example, if you have a triangle that extends beyond the edges of a window, polygon clipping is the operation that trims the triangle to fit inside the window.

## Problem to Solve

For Polygon Clipping problem, there are many algorithms are capable of solving this problem, such as **Sutherland–Hodgman algorithm**, **Greiner–Hormann clipping algorithm**, **Vatti clipping algorithm**, **Weiler–Atherton clipping algorithm**.

**Sutherland–Hodgman algorithm**, which is one of the most widely used algorithms for polygon clipping. However, it has some drawbacks, such as being inefficient and slow for large or complex polygons.This is because it must process every edge of the polygon against every edge of the boundary.Additionally, it can lead to numerical errors and rounding issues from the use of floating-point arithmetic and intersection calculations.

possible usage:

1. Rendering
2. Clipping Masks
3. Visibility tests

![image](https://github.com/leeshengcian/Polygon-Clipping/blob/main/image/poly-clip.png)

## System Architecture

![image](https://github.com/leeshengcian/Visualization-of-Dijkstra-Algorithm/blob/main/image/term_project_work_flow.png)

## API Description

1. Dijkstra function in c++ will find the shortest path from the source node to each of the remaining nodes
    - dist[i] will store the shortest distance from source node to ith node
2. Use Pybind11 to wrap C++ functions for Python
3. Python file is responsible for drawing the graph
    - import networkx and matplotlib for plot work

## Engineering Infrastructure

1. Automatic build system: `CMake`
2. Version control: `git`
3. Testing framework: `pytest`
4. Documentation: `README.md`

## Schedule

* Week 1 (10/30):
    - Study domain Knowledge for Dijkstra's Algorithm
    - Plot the original graph using networkx
* Week 2 (11/6):
    - Implement Dijkstra's on given graph
    - Prepare a presentation skeleton
* Week 3 (11/13):
    - Finish Dijkstra's Algorithm in c++ and write pybind11 wrapper
    - Further prepare for presentation
* Week 4 (11/20):
    - Finish Plot work in Python
* Week 5 (11/27):
    - Testing the correctness of algorithm and plot work
* Week 6 (12/4):
    - Implement CMake file
    - Make slides and prepare for presentation
* Week 7 (12/11):
    - Testing if the system build work
    - Write the Documentation
    - Make slides and prepare for presentation
* Week 8 (12/18):
    - Finish writing Documentation
    - Make slides and prepare for presentation

## References

- [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [NetworkX](https://networkx.org/)
