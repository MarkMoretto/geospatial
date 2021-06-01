package polygon

import (
	pt "GeGoSpatial/polygon/point"
)

// Polygon is a collection of coordinates.
type Polygon []pt.Point

var Area float32 = 0.0
var SignedArea float32 = 0.0
var Centroid = pt.Point{X: 0.0, Y: 0.0}

// Count of vertices within a given polygon.
func (pg *Polygon) VertexCount() (result int){
	result = len(*pg) / (*pg)[0].Size()
	return
}


func (p *Polygon) CalculateCentroid() {
	pCentroid := &Centroid
	pArea := &Area
	pSignedArea := &SignedArea

	// Counters
	var i int = 0
	var ii int = 1

	// Vertices == capacity or length of polygon
	// minus 2.  We're going minus 2 since we're including
	// the next element of the polygon and will finlize
	// calculations outside of the loop.
	for i < cap(*p) - 2 {
		x0 := (*p)[i].X
		x1 := (*p)[ii].X
		y0 := (*p)[i].Y
		y1 := (*p)[ii].Y

		*pArea = (x0 * y1) - (x1 * y0)

		*pSignedArea = *pSignedArea + Area

		(*pCentroid).X = (*pCentroid).X + ((x0 + x1) * Area)
		(*pCentroid).Y = (*pCentroid).Y + ((y0 + y1) * Area)

		i++
		ii++
	}

	// Final calculation
	x0 := (*p)[i].X
	x1 := (*p)[ii].X
	y0 := (*p)[i].Y
	y1 := (*p)[ii].Y

	*pArea = (x0 * y1) - (x1 * y0)

	*pSignedArea = *pSignedArea + Area

	(*pCentroid).X = (*pCentroid).X + ((x0 + x1) * Area)
	(*pCentroid).Y = (*pCentroid).Y + ((y0 + y1) * Area)

	// Half of signed area
	*pSignedArea *= 0.5
	(*pCentroid).X = (*pCentroid).X / (6.0 * SignedArea)
	(*pCentroid).Y = (*pCentroid).Y / (6.0 * SignedArea)
}
