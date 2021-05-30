
"""
Summary: Various functions for geospatial analysis
Date: 2021-05-29
Contributor(s):
    mark moretto
"""

# Standard
from typing import Iterable, List, Union
from math import acos, asin, cos, radians, sin, sqrt


# Local
from constants import EARTH_EQUATORIAL_RADIUS_KM, KM_PER_MI
from classes import Coord

### Third-party
import numpy as np



### Type declarations
Number = Union[float,int]




### Functions

def km_to_mi(r: Number, scale: int = 6) -> float:
    """Return kilometers converted to miles.

    Parameters
    ----------
        r : Number
            Radius of object.
        scale : int, optional
            Mantissa of return value.
            Default: 6.

    Returns
    -------
        float
            Quantity of miles
    
    >>> km_to_mi(EARTH_EQUATORIAL_RADIUS_KM)
    3963.190592
    >>> km_to_mi("Hello")
    Traceback (most recent call last):
        ...
    ValueError: Float or integer value expected.
    """
    if not isinstance(r, (float, int)):
        raise ValueError("Float or integer value expected.")
    return round(r / KM_PER_MI, scale)



def dms_to_dd(degrees: Number, minutes: Number = 0, seconds: Number = 0, ewns: str = "", scale: int = 5) -> float:
    """Convert degrees, minutes, seconds to decimal degrees for latitudes and longitudes. These
    are representations of degrees in sexagesimal unit subdivisions.

    See: https://ottergeospatial.info/2020/02/03/geographic-coordinate-notation-dd-vs-dm-vs-dms/
    See: https://dateandtime.info/citycoordinates.php?id=5254962
    See: https://en.wikipedia.org/wiki/Degree_(angle)#Subdivisions

    Parameters
    ----------
        degrees : Number
            The geographic coordinate system (GCS) number of degrees away from the equator or prime meridian. These
            should really be called arc hours.
        minutes : Number, optional
            Arc minutes to be converted.  Note: 1 arc minute == 1 / 60 degrees.
            Default: 0.
        seconds : Number, optional
            Arc seconds to be converted.  Note: 1 arc second == 1 / 60 / 60 degrees.
            Default: 0.
        ewns : str
            Additional attribute to determine if latitude or longitude should be negative based on relation
            to equator or prime meridian.  Possible values are "n", "s" (longitude), "w", "e" (latitude).
            Default: "".
        scale : int, optional
            Mantissa of return value.
            Default: 5.

    Returns
    -------
        float
            Decimal degree value.
    
    >>> dms_to_dd(44, 31, 40.2)
    44.52783
    >>> dms_to_dd(87, 54, 58.9, "W")
    -87.91636
    """

    degree: int = 60
    ddegree: int = (degree * degree)    

    if seconds > 0:
        seconds = (seconds / ddegree)
    if minutes > 0:
        minutes = (minutes / degree)

    result = round(degrees + minutes + seconds, scale)

    if ewns.lower() in ("w", "s") and degrees > 0:
        result *= -1
    return result





def dd_to_dms(decimal_degrees: float, scale: int = 1) -> tuple:
    """Return decimal degrees as DMS (degree, minute, second) Notation.
    
    >>> dd_to_dms(44.52783)
    (44, 31, 40.2)
    """
    # Separate degrees from the pack.
    degrees: int = int(decimal_degrees)

    # Take abslute value of decimal degrees to extract mantissa (part to the right of the decimal point).
    degrees_remainder: float = abs(decimal_degrees) % degrees

    # Find the minutes numerator by multiplying the mantissa by 60.
    minutes_numerator: float = 60 * degrees_remainder

    # Actual minutes are just the integer value of the numerator value.
    minutes = int(minutes_numerator)

    # Seconds are the remainder of the minutes modulo multiplied by 60.
    # Value is rounded to a default 1 decimal place.
    seconds = round(60 * (minutes_numerator % minutes), scale)

    return degrees, minutes, seconds



def rand_range_multidim(n_rows: int, n_cols: int, minmax: Iterable[Number], seed: int = None) -> np.array:
    """Return multidimensional numpy array of 32-bit floating-point numbers
    within a given domain.
    
    The generated array will have elements that are half-bound, upper exclusive -> [lower, upper).

    
    Parameters
    ----------
        n_rows : int
            Number of rows in the multidimensional array.
        n_cols : int
            Number of columns in the multidimensional array.
        minmax : Iterable[Number]
            A two-item iterable for the domain of the returned array.
        seed : int, optional
            Seed value for repeatable results from random number generator.
            Default: None.

    Returns
    -------
        numpy.array
            A numpy array of 32-bit floating-point values based on input parameters.
    """

    np_rng = np.random.default_rng()

    if seed:
        np_rng = np.random.default_rng(seed)

    bottom, top = sorted(minmax)
    return (top - bottom) * np_rng.random((n_rows, n_cols), dtype = np.float32) + bottom

# rand_range_multidim(3, 2, [2, 10])

class CoordsValidator:
    "Class to help process and validate an array of coordinates."
    def __init__(self, coordinates: List[Coord]):
        if isinstance(coordinates, list):
            self.__set_min_max(coordinates)

    def __set_min_max(self, coordinates: List[Coord]):
        self.min_lat, self.max_lat = self.min_max_lat(coordinates)
        self.min_lon, self.max_lon = self.min_max_lon(coordinates)

    @staticmethod
    def min_max_lat(iterable: List[Coord]):
        """Return minimum and maximum latitude values from a list of coordinates."""
        return min(c.lat for c in iterable), max(c.lat for c in iterable)

    @staticmethod
    def min_max_lon(iterable: List[Coord]):
        """Return minimum and maximum longitude values from a list of coordinates."""
        return min(c.lon for c in iterable), max(c.lon for c in iterable)

    def lat_ok(self, c: Coord):
        """Return True if latitude of coordinate within minimum and maximum values."""
        return c.lat >= self.min_lat and c.lat <= self.max_lat

    def lon_ok(self, c: Coord):
        """Return True if longitude of coordinate within minimum and maximum values."""
        return c.lon >= self.min_lon and c.lon <= self.max_lon

    def coord_in_plane(self, coord: Coord):
        """Return True if coordinate point falls within or on all boundaries of plane."""
        return self.lat_ok(coord) and self.lon_ok(coord)





def generate_coordinates(lower_left: Coord, upper_right: Coord, n_coords: int = 1000, seed: int = None):
    min_lat= min([lower_left.lat, upper_right.lat])
    max_lat= max([lower_left.lat, upper_right.lat])
    min_lon= min([lower_left.lon, upper_right.lon])
    max_lon= max([lower_left.lon, upper_right.lon])

    lat_arr = rand_range_multidim(n_coords, 1, [min_lat, max_lat])
    lon_arr = rand_range_multidim(n_coords, 1, [min_lon, max_lon])
    if seed:
        lat_arr = rand_range_multidim(n_coords, 1, [min_lat, max_lat], seed)
        lon_arr = rand_range_multidim(n_coords, 1, [min_lon, max_lon], seed)        
    return [Coord(i[0], i[1]) for i in np.concatenate((lat_arr, lon_arr), axis = 1)]

# coords = [Coord(i[0], i[1]) for i in res]
def test_coord_validator():
    USA_lower_left = Coord(32.708733, -117.229598)
    USA_upper_right = Coord(47.361153, -68.290845)
    N = 1000
    seed_value = 13
    coords = generate_coordinates(USA_lower_left, USA_upper_right, N, seed_value)
    v = CoordsValidator(coords)
    las_vegas = Coord(36.1185549983094, -115.17267265946954)
    assert (v.coord_in_plane(las_vegas) == True), "Rerun validation test.  Check seed value."


X = Coord(37.160316546736745, -78.75)
y = Coord(39.095962936305476, -121.2890625)
# data = np.array(list(ittr.repeat(y, 100)))


def shortest_dist_haystack(target: Coord, coords: List[Coord]):
    """Shortest distance using one-to-many approach."""
    target_X_rads = radians(target.lat)
    target_y_rads = radians(target.lon)

    d_lat = radians(coords[:,0]) - target_x_rads
    d_lon = radians(coords[:,1]) - target_y_rads 

    a = sqrt(sin(d_lat * 0.5)) + cos(target_X_rads) * cos(radians(coords[:,0])) * sqrt(sin(d_lon * 0.5))

    great_circle_distance = 2 * asin(min(sqrt(a), np.repeat(1, len(a))))

    d = earth_radius_miles * great_circle_distance

    return np.min(d)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
