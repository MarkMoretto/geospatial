"""
Summary: Constants for various geodata measures
"""

# Earth
EARTH_EQUATORIAL_RADIUS_M: float = 6378137.000000
EARTH_EQUATORIAL_RADIUS_KM: float = 6378.137000

EARTH_POLAR_RADIUS_M: float = 6356752.314245
EARTH_POLAR_RADIUS_KM: float = 6356.752000

EARTH_VOLUMETRIC_MEAN_RADIUS_KM: float = 6371.000000
EARTH_CORE_RADIUS_KM: float = 3485.000000


# Distance
KM_PER_MI: float = 1.609344
MI_PER_KM: float = 0.6213711922

# DMS Distance
DECIMAL_DEGREE_KM: float = 111.32

# Time
MILLISECOND: int = 1
SECOND: int = MILLISECOND * 1000
MINUTE: int = SECOND * 60
HOUR: int = MINUTE * 60
DAY: int = HOUR * 24


# DMS time
DEGREE: int = 60
ARCMINUTE: float = 1 / DEGREE
ARCSECOND: float = 1 / (DEGREE * DEGREE)






# Earth data sources - 
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
# https://en.wikipedia.org/wiki/World_Geodetic_System