
from ..datatypes import List
from ..utility import km_to_mi
from ..constants import EARTH_EQUATORIAL_RADIUS_KM

import numpy as np


EARTH_EQUATORIAL_RADIUS_MI: float = km_to_mi(EARTH_EQUATORIAL_RADIUS_KM)


def shortest_dist_haystack(target: np.array, coords: List[np.array]) -> float:
    """Shortest distance using one-to-many approach."""
    target_X_rads = radians(target[0])
    target_y_rads = radians(target[1])

    d_lat = np.radians(rand_coords[:,0]) - target_X_rads
    d_lon = np.radians(rand_coords[:,1]) - target_y_rads

    a = np.square(np.sin(d_lat * 0.5)) + np.cos(target_X_rads) * np.cos(np.radians(rand_coords[:,0])) * np.square(np.sin(d_lon * 0.5))

    great_circle_distance = 2 * np.arcsin(np.minimum(np.square(a), np.repeat(1, len(a))))

    gross_distance = EARTH_EQUATORIAL_RADIUS_MI * great_circle_distance

    return np.min(gross_distance)