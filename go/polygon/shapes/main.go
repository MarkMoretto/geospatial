package shapes

import (
	pg "GeGoSpatial/polygon"
	pt "GeGoSpatial/polygon/point"
	"math"
)


type Polygon pg.Polygon
type Origin pt.Point
type Coord pt.Point


const (
	TwoPi float64 = math.Pi * 2
)

// Regular Pentagon interface.
type RegularPentagon interface{
	P1(o *Origin)
	P2(o *Origin)
	P3(o *Origin)
	P4(o *Origin)
	P5(o *Origin)
}

var Scale float32 = 1

var (
	c1 float32 = float32(math.Cos(TwoPi / 5)) * Scale;
	c2 float32 = float32(math.Cos(math.Pi / 5)) * Scale;
	s1 float32 = float32(math.Sin(TwoPi / 5)) * Scale;
	s2 float32 = float32(math.Sin(math.Pi / 5)) * Scale;
)


func (c *Coord)P1(o *Origin) {
	c.X = o.X + 1 * Scale
	c.Y = o.Y + 0 * Scale
}


func (c *Coord)P2(o *Origin) {
	c.X = o.X + c1
	c.Y = o.Y + s1
}


func (c *Coord)P3(o *Origin) {
	c.X = o.X - c2
	c.Y = o.Y + s2
}

func (c *Coord)P4(o *Origin) {
	c.X = o.X - c2
	c.Y = o.Y - s2
}

func (c *Coord)P5(o *Origin) {
	c.X = o.X + c1
	c.Y = o.Y - s1
}


// func CreatePentagon(r RegularPentagon) pg.Polygon {
// 	p := pg.Polygon{}
// }