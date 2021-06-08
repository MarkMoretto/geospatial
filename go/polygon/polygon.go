package polygon

import (
	pt "GeGoSpatial/polygon/point"
)

// Polygon is a collection of coordinates.
type Polygon []pt.Point

var Area float32
var SignedArea float32
// var Centroid = pt.Point{X: 0.0, Y: 0.0}
var Centroid pt.Point


// Count of vertices within a given polygon.
func (pg *Polygon) VertexCount() (result uint32){
	// result = len(*pg) / (*pg)[0].Size()
	result = uint32(len(*pg))
	return
}


func (p *Polygon) CalculateCentroid() {

	pCentroid := &Centroid
	pArea := &Area
	pSignedArea := &SignedArea

	*pCentroid = pt.Point{X: 0.0, Y: 0.0}
	*pArea = 0
	*pSignedArea = 0

	// Counters
	var i uint32 = 0
	var ii uint32 = 1

	// Vertices == capacity or length of polygon
	// minus 2.  We're going minus 2 since we're including
	// the next element of the polygon and will finlize
	// calculations outside of the loop.
	for i < p.VertexCount() - 2 {
		x0 := (*p)[i].X
		x1 := (*p)[ii].X
		y0 := (*p)[i].Y
		y1 := (*p)[ii].Y
		
		*pArea = (x0 * y1) - (x1 * y0)

		*pSignedArea = *pSignedArea + Area

		(*pCentroid).X = (*pCentroid).X + ((x0 + x1) * *pArea)
		(*pCentroid).Y = (*pCentroid).Y + ((y0 + y1) * *pArea)	

		i++
		ii++
	}

	// Final calculation
	x0 := (*p)[i].X
	x1 := (*p)[ii].X
	y0 := (*p)[i].Y
	y1 := (*p)[ii].Y

	*pArea = (x0 * y1) - (x1 * y0)

	*pSignedArea = *pSignedArea + *pArea

	(*pCentroid).X = (*pCentroid).X + ((x0 + x1) * *pArea)
	(*pCentroid).Y = (*pCentroid).Y + ((y0 + y1) * *pArea)	

	// Half of signed area
	*pSignedArea = *pSignedArea * 0.5
	(*pCentroid).X = (*pCentroid).X / (6.0 * *pSignedArea)
	(*pCentroid).Y = (*pCentroid).Y / (6.0 * *pSignedArea)
}
