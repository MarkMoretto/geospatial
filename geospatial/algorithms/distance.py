
from math import sqrt

from ..classes import Point



class Distance:

    __slots__ = ["point_1", "point_2",]
    
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def __str__(self):
        return f"<Distance p1:({self.point_1.X}, {self.point_1.y}), p2:({self.point_2.X}, {self.point_2.y}) />"

    @property
    def euclidean(self):
        lhs = (self.point_1.X - self.point_2.X) ** 2
        rhs = (self.point_1.y - self.point_2.y) ** 2
        return sqrt(lhs + rhs)
     


def test_euclidean():
    point1 = Point(1.23209, -370.67322)
    point2 = Point(1.18702, -375.09202)
    d = Distance(point1, point2)
    assert (round(d.euclidean, 6) == 4.41903), "Euclidean test error."
