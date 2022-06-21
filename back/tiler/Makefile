all: tiler.o

tiler.o: tiler.cpp
	g++ -std=c++17 -Wall -o tiler.o -g tiler.cpp `pkg-config vips-cpp --cflags --libs`