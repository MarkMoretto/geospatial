package main

import (
	p "GeGoSpatial/polygon"
	"fmt"
)


func main() {
	/////////
	//! Test shapes
	var squarePolygon = &p.Polygon{
		{X:0, Y: 0},
		{X:10, Y: 0},
		{X:10, Y: 10},
		{X:0, Y: 10},		
	}

	var pentagonPolygon = &p.Polygon{
		{X:100, Y: 0},
		{X:200, Y: 77},
		{X:160, Y: 200},
		{X:40, Y: 200},		
		{X:0, Y: 77},
	}	


	RunPolygonTest(squarePolygon, "Square")
	RunPolygonTest(pentagonPolygon, "Pentagon")

}


//! Print results to console.
func RunPolygonTest(pg *p.Polygon, shapeName string) {
	fmt.Println("Finding centroid for a ", shapeName)

	fmt.Printf("The polygon length is: %d\n", len(*pg))
	fmt.Printf("The polygon capacity is: %d\n", cap(*pg))
	fmt.Printf("The vertex count is: %d\n", pg.VertexCount())

	pg.CalculateCentroid()
	
	fmt.Printf("Post-run centroid is: (%.6f, %.6f)\n", p.Centroid.X, p.Centroid.Y)
	fmt.Printf("Area is: %f\n", p.SignedArea)
}