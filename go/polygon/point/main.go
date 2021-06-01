package point

type Point struct {
	X, Y float32
}

func (p *Point) Size() (size int) {
	size = 2
	return
}