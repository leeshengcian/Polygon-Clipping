CXX = g++
CXXFLAGS = -O3 -Wall --shared -std=c++17 -fPIC `python3 -m pybind11 --includes` `python3-config --includes --ldflags` -undefined dynamic_lookup
TARGET = clipper.so
TEST_FILE = test

.PHONY: all run_python clean

all: $(TARGET) run_python
$(TARGET): clipper.cpp
	$(CXX) -o $@ $(CXXFLAGS) $<

run_python: clipper.so test_poly.py
	python3 test_poly.py

clean:
	rm -rf *.o *.so __pycache__ .pytest_cache/