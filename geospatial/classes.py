

from numpy import array, float32


class Point:
    """Structure to represent a basic Cartesian point."""
    X: float
    y: float
    def __init__(self, X: float, y: float) -> None:
        self.X = X
        self.y = y

    def __str__(self):
        return f"<Point ({self.X}, {self.y}) />"
        
    def __repr__(self):
        return f"({self.X}, {self.y})"

    @property
    def Xy(self):
        return self.X, self.y
        

class CordPoint:
    """Simple structure to represent a coordinate point."""
    lat: float
    lon: float


class Coord(CordPoint):
    __slots__ = ["latitude", "longitude", "scale"]
    def  __init__(self, latitude: float, longitude: float, scale: int = 6):
        self.__lat = latitude
        self.__lon = longitude
        self.scale = scale
    
    def __repr__(self):
        lhs = f"{self.lat:.{self.scale}f}"
        rhs = f"{self.lon:.{self.scale}f}"
        return f"<Coord ({lhs} {rhs}) />"

    @property
    def lat(self):
        return round(self.__lat, self.scale)

    @lat.setter
    def lat(self, value):
        if not isinstance(value, float):
            raise ValueError("Expected float data type.")
        self.__lat = value

    @property
    def lon(self):
        return round(self.__lon, self.scale)

    @lon.setter
    def lon(self, value):
        if not isinstance(value, float):
            raise ValueError("Expected float data type.")
        self.__lon = value

    def values(self):
        return array([self.lat, self.lon], dtype = float32)

