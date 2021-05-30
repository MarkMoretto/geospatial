package main

import (
	md "github.com/MarkMoretto/geospatial/multidim"
)

func main() {

	var testCoords = md.Matrix2DI{
		{0, 0},
		{10, 0},
		{10, 10},
		{0, 10},
	}
	testCoords.PrintIndexRows()

}
