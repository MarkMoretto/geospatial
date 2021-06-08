package shapes

/*
def regular_pentagon(origin: Point = Point(0., 0.), scale: int = 10) -> List[Point]:
    output: List[Point] = []

    round_to: int = 1

    c1 = round(cos((2*pi)/5) * scale, round_to)
    c2 = round(cos(pi/5) * scale, round_to)
    s1 = round(sin((2*pi)/5) * scale, round_to)
    s2 = round(sin(pi/5) * scale, round_to)


    p1 = Point(origin.X + 1. * scale, origin.y + 0. * scale)
    p2 = Point(origin.X + c1, origin.y + s1)
    p3 = Point(origin.X - c2, origin.y + s2)
    p4 = Point(origin.X - c2, origin.y - s2)
    p5 = Point(origin.X + c1, origin.y - s1)
    output.extend([p1, p2, p3, p4, p5])

    return output
*/

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