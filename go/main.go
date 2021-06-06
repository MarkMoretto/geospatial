package main

import (
	p "GeGoSpatial/polygon"
	"fmt"
)


func main() {
	/////////
	//! Test shapes
	var squarePolygon = &p.Polygon{
		{X: 0.00, Y: 0.00},
		{X: 10.00, Y: 0.00},
		{X: 10.00, Y: 10.00},
		{X: 0.00, Y: 10.00},		
	}

	var pentagonPolygon = &p.Polygon{
		{X: 10.00, Y: 0.00},
		{X: 3.09, Y: 9.51},
		{X: -8.09, Y: 5.88},
		{X: -8.09, Y: -5.88},
		{X: 3.09, Y: -9.51},
	}	

	var hexagonPolygon = &p.Polygon{
		{X:10.00, Y: 0.00},
		{X:0.00, Y: 10.00},
		{X:10.00, Y: 20.00},
		{X:20.00, Y: 20.00},
		{X:30.00, Y: 10.00},
		{X:20.00, Y: 0.00},
	}		

	RunPolygonTest(squarePolygon, "Square")
	RunPolygonTest(pentagonPolygon, "Pentagon")
	RunPolygonTest(hexagonPolygon, "Hexagon")

}


//! Print results to console.
func RunPolygonTest(pg *p.Polygon, shapeName string) {
	fmt.Println("\nFinding centroid for a ", shapeName)

	fmt.Printf("The polygon length is: %d\n", len(*pg))
	fmt.Printf("The polygon capacity is: %d\n", cap(*pg))
	fmt.Printf("The vertex count is: %d\n", pg.VertexCount())

	pg.CalculateCentroid()
	
	fmt.Printf("Post-run centroid is: (%.6f, %.6f)\n", p.Centroid.X, p.Centroid.Y)
	fmt.Printf("Area is: %f\n", p.SignedArea)
}