CXX = g++
CXXFLAGS = -O3 -Wall --shared -std=c++17 -fPIC `python3 -m pybind11 --includes` `python3-config --includes --ldflags` -undefined dynamic_lookup
TARGET = clipper.so
DATA = polygons.txt
TEST_FILE = test

.PHONY: all generate_data run_python clean

all: $(TARGET) generate_data
$(TARGET): clipper.cpp
	$(CXX) -o $@ $(CXXFLAGS) $<

generate_data: $(DATA) run_python
$(DATA): 
	python3 polygon_generator.py

run_python: clipper.so test_poly.py
	python3 test_poly.py

clean:
	rm -rf *.o *.so *.txt __pycache__ .pytest_cache/