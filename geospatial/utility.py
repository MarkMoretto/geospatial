
"""
Summary: Various functions for geospatial analysis
Date: 2021-05-29
Contributor(s):
    mark moretto
"""

from typing import Union


from constants import EARTH_EQUATORIAL_RADIUS_KM, KM_PER_MI


def km_to_mi(r: Union[float,int], scale: int = 6) -> float:
    """Return kilometers converted to miles.

    Parameters:
        r: Union[float,int] - Radius of object.

    Returns:
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




if __name__ == "__main__":
    import doctest
    doctest.testmod()
