


class CordPoint:
    """Simple structure to represent a coordinate point."""
    lat: float
    lon: float

class Coord(CordPoint):
    __slots__ = ["latitude", "longitude"]
    def  __init__(self, latitude: float, longitude: float):
        self.lat = latitude
        self.lon = longitude
    
    def __repr__(self):
        return f"<Coord ({self.lat} {self.lon}) />"
