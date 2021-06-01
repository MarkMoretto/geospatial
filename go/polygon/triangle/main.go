package triangle

import pt "GeGoSpatial/polygon/point"


type Triangle struct {
	A, B, C pt.Point
}

// Double the area of a triangle as determined by three points.
// Will be positive if counterclockwise and negative if clockwise
func (t *Triangle) Area() (result float32) {
	lhs := (t.B.X - t.A.X) * (t.C.Y - t.A.Y)
	rhs := (t.C.X - t.A.X) * (t.B.Y - t.A.Y)
	result = lhs - rhs
	return
}

