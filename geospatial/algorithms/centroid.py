

from typing import List
from math import sqrt, sin, cos, pi

from ..classes import Point

# try:
#     from ..classes import Point
# except (ModuleNotFoundError, ValueError):
#     from .classes import Point



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

# pentagon_coords = regular_pentagon(scale = 100)




square_coords = [
    Point(0., 0.),
    Point(10., 0.),
    Point(10., 10.),
    Point(0., 10.),
    ]


pentagon_coords = regular_pentagon(scale = 10)


hexagon_coords = [
    Point(10., 0.),
    Point(0., 10.),
    Point(10., 20.),
    Point(20., 20.),
    Point(30., 10.),
    Point(20., 0.),
    ]


# Helper function to unpack (X, y).
# get_Xy = lambda p: (p.X, p.y)

print_coords = lambda iterable: print(",".join([f"({p.X:.2f},{p.y:.2f})" for p in iterable]))
print_go_coords = lambda iterable: print("\n".join([f"{{X: {p.X:.2f}, Y: {p.y:.2f}}}," for p in iterable]))
print_go_coords(pentagon_coords)
# print_coords(hexagon_coords)

def get_centroid(coords: List[Point]) -> Point:
    """Calculate the centroid of a convex polygon.
    
    >>> square_coords = [
        Point(0., 0.),
        Point(10., 0.),
        Point(10., 10.),
        Point(0., 10.),
    ]
    >>> res = get_centroid(square_coords)
    >>> res
    (5.0, 5.0)

    >>> hexagon_coords = [
        Point(10., 0.),
        Point(0., 10.),
        Point(10., 20.),
        Point(20., 20.),
        Point(30., 10.),
        Point(20., 0.),
    ]
    >>> res = get_centroid(hexagon_coords)
    >>> res
    (15.0, 10.0)    
    """
    nvertices = len(coords)
    signed_area = 0.
    centroid = Point(0., 0.)

    for c in range(nvertices - 2):
        # X0, y0 = get_Xy(coords[c])
        # X1, y1 = get_Xy(coords[c + 1])
        X0, y0 = coords[c].Xy
        X1, y1 = coords[c + 1].Xy
  
        area = (X0 * y1) - (X1 * y0)
        signed_area += area
        centroid.X += (X0 + X1) * area
        centroid.y += (y0 + y1) * area


    # Process last few points
    X0, y0 = coords[nvertices - 2].Xy
    X1, y1 = coords[nvertices - 1].Xy

    area = (X0 * y1) - (X1 * y0)

    signed_area += area

    centroid.X += (X0 + X1) * area
    centroid.y += (y0 + y1) * area

    signed_area *= 0.5
    centroid.X /= (6. * signed_area)
    centroid.y /= (6. * signed_area)
    return centroid



def test_polygons():
    res = get_centroid(square_coords)
    assert (res.X == 5.0 and res.y == 5.0), "Regular square centroid error."

    res = get_centroid(pentagon_coords)

    res = get_centroid(hexagon_coords) 
    assert (res.X == 15.0 and res.y == 10.0), "Hexagon centroid error."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
