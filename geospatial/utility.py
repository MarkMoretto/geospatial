# -*- coding: utf-8 -*-

# geospatial\utility.py

"""
Summary: Various functions for geospatial analysis
Date: 2021-05-29
Contributor(s):
    mark moretto
"""

# Standard
from math import acos, asin, cos, radians, sin, sqrt


# Local
from datatypes import Iterable, List, Number, Union
from classes import Coord

### Third-party
import numpy as np
# import numpy.random
# from numpy import array, float32, int32, concatenate, object_



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
        """Set four class variables upon instantiation.
        
        Latitude
        --------
            min_lat : 
        """
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
    """Return numpy.array of random Coord instances for testing.  Generated results will fall within
    the provided lower-left and upper-right Coord object latitude and longitude values.
    
    Parameters
    ----------
        lower_left : Coord
            Coord object containing `start` values, or values in
            the lower-left portion of the shape.
        upper_right : Coord
            Coord object containing `end` values, or values in
            the upper-right portion of the shape.
        n_coords : int
            Number of random Coord objects to generate.
            Default: 1000.
        seed : int, optional
            Seed value for repeatable results from random number generator.
            Default: None.

    Returns
    -------
        numpy.array
            A numpy array of Coord objects.
    """
    min_lat= min([lower_left.lat, upper_right.lat])
    max_lat= max([lower_left.lat, upper_right.lat])
    min_lon= min([lower_left.lon, upper_right.lon])
    max_lon= max([lower_left.lon, upper_right.lon])

    lat_arr = rand_range_multidim(n_coords, 1, [min_lat, max_lat])
    lon_arr = rand_range_multidim(n_coords, 1, [min_lon, max_lon])
    if seed:
        lat_arr = rand_range_multidim(n_coords, 1, [min_lat, max_lat], seed)
        lon_arr = rand_range_multidim(n_coords, 1, [min_lon, max_lon], seed)        
    return np.array([Coord(i[0], i[1]) for i in np.concatenate((lat_arr, lon_arr), axis = 1)], dtype = np.object_)

# coords = [Coord(i[0], i[1]) for i in res]


def test_coord_validator():
    """Test: Coordinate resides within a given plane
    
    This test looks at rough boundaries of the USA
    (from San Diego, Calif., to around Fort Kent, Maine)
    and asks whether a known coordinate falls within that set
    of dimensions.
    """
    USA_lower_left = Coord(32.708733, -117.229598)
    USA_upper_right = Coord(47.361153, -68.290845)
    N = 1000
    seed_value = 13
    coords = generate_coordinates(USA_lower_left, USA_upper_right, N, seed_value)
    v = CoordsValidator(coords)
    las_vegas = Coord(36.1185549983094, -115.17267265946954)
    assert (v.coord_in_plane(las_vegas) == True), "Rerun validation test.  Check seed value."


# X = Coord(37.160316546736745, -78.75)
# y = Coord(39.095962936305476, -121.2890625)
# data = np.array(list(ittr.repeat(y, 100)))




def to_value_array(arr_obj):
    return np.array(list(map(lambda w: w.values(), arr_obj)))


def test_haystack():
    target = np.array([37.160316546736745, -78.75])
    goal = np.array([39.095962936305476, -121.2890625])
    USA_lower_left = Coord(32.708733, -117.229598)
    USA_upper_right = Coord(47.361153, -68.290845)

    rand_coords = generate_coordinates(USA_lower_left, USA_upper_right, 1000)
    rand_coords = to_value_array(rand_coords)
    rand_coords = np.append(rand_coords, [goal], axis=0)
    # rand_coords = np.insert(rand_coords, rand_coords.shape[0], goal, axis=1)

    target_X_rads = radians(target[0])
    target_y_rads = radians(target[1])

    d_lat = np.radians(rand_coords[:,0]) - target_X_rads
    d_lon = np.radians(rand_coords[:,1]) - target_y_rads

    a = np.square(np.sin(d_lat * 0.5)) + np.cos(target_X_rads) * np.cos(np.radians(rand_coords[:,0])) * np.square(np.sin(d_lon * 0.5))

    great_circle_distance = 2 * np.arcsin(np.minimum(np.square(a), np.repeat(1, len(a))))

    d = EARTH_EQUATORIAL_RADIUS_MI * great_circle_distance
    result = np.min(d)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
