package main

import (
	p "GeGoSpatial/polygon"
	"fmt"
)

// Test data
var squarePolygon p.Polygon = p.Polygon{
	{X:0, Y: 0},
	{X:10, Y: 0},
	{X:10, Y: 10},
	{X:0, Y: 10},		
}

func main() {
	// Finding centroid demo for two-dimensional polygon.
	// The initial run uses a square


	// fmt.Printf("Pre-run centroid is: (%.6f, %.6f)\n", p.Centroid.X, p.Centroid.Y)
	fmt.Printf("The polygon length is: %d\n", len(squarePolygon))
	fmt.Printf("The polygon capacity is: %d\n", cap(squarePolygon))
	fmt.Printf("The vertex count is: %d\n", squarePolygon.VertexCount())

	squarePolygon.CalculateCentroid()

	fmt.Printf("Post-run centroid is: (%.6f, %.6f)\n", p.Centroid.X, p.Centroid.Y)
	fmt.Printf("Area is: %f\n", p.SignedArea)
}
