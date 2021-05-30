# -*- coding: utf-8 -*-
"""
Summary: Functions for converting data.
"""

# Local imports
from datatypes import Number
from constants import DEGREE, KM_PER_MI



# Distance


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


# Coordinates
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


    if seconds > 0:
        seconds = (seconds / (DEGREE * DEGREE))
        
    if minutes > 0:
        minutes = (minutes / DEGREE)

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
