# -*- coding: utf-8 -*-

import orjson
from io import StringIO, BytesIO
import urllib.request as ureq
import pandas as pd

# Airports
# https://github.com/andrea-ballatore/open-geo-data-education/raw/main/datasets/airports/airports_2020.geojson

oa_base = "https://ourairports.com/data/"
oa_assets = [
    "airports",
    "countries",
    "regions",
]
oa_urls = [ureq.urljoin(oa_base, f"{u}.csv") for u in oa_assets]

airport_cols = """
id ident type name latitude_deg longitude_deg elevation_ft continent iso_country iso_region municipality scheduled_service gps_code iata_code local_code
"""
airport_cols = airport_cols.strip().split(" ")

df1 = pd.read_csv(oa_urls[0], usecols = airport_cols)
df1.name = oa_assets[0]
df2 = pd.read_csv(oa_urls[1], usecols = ["id", "code", "name", "continent"])
df2.name = oa_assets[1]
df3 = pd.read_csv(oa_urls[2], usecols = ["id", "code", "local_code", "name", "continent", "iso_country"])
df3.name = oa_assets[2]



# GeoJSON us_states
# https://github.com/andrea-ballatore/open-geo-data-education/blob/main/datasets/us_states/us_states_2018.geojson.gz
fp = r"C:\Users\Work1\Downloads\us_states_2018.geojson"
with open(fp) as f:
	data = orjson.loads(f.read())


len(data.get("features"))
# data.get("features")
data.get("features")[0].get("geometry").get("type") # MultiPolygon
len(data.get("features")[0].get("geometry").get("coordinates"))

for i in range(8):
	print(i, " -> ", len(data.get("features")[0].get("geometry").get("coordinates")[i][0]))




data.get("features")[0].get("properties")
data.get("features")[0].get("geometry")
data.get("features")[0].get("geometry").get("coordinates")

data.get("features")[0].get("geometry").get("coordinates")[6][0]




# tmp = orjson.loads(data)
# tmp.get("type")
# tmp.get("name")
# tmp.get("crs")
tmp.get("features") # n = 3187
tmp.get("features")[0].get("properties")
tmp.get("features")[0].get("geometry")
tmp.get("features")[0].get("geometry").get("coordinates")

""" Sample Data: tmp.get("features")[0]

{'type': 'Feature',
 'properties': {'FID': 1,
  'id': 3.0,
  'ident': 'AGGH',
  'type': 'medium_airport',
  'name': 'Honiara International Airport',
  'latitude_d': -9.4280004501343,
  'longitude_': 160.05499267578,
  'elevation_': 28.0,
  'continent': 'OC',
  'iso_countr': 'SB',
  'iso_region': 'SB-CT',
  'municipali': 'Honiara',
  'scheduled_': 'yes',
  'gps_code': 'AGGH',
  'iata_code': 'HIR',
  'local_code': None,
  'home_link': None,
  'wikipedia_': 'https://en.wikipedia.org/wiki/Honiara_International_Airport',
  'keywords': 'Henderson Field',
  'id_1': 233754.0,
  'airport_re': 3.0,
  'airport_id': 'AGGH',
  'length_ft': 7218.0,
  'width_ft': 148.0,
  'surface': 'ASP',
  'lighted': 1.0,
  'closed': 0.0,
  'le_ident': '06',
  'le_latitud': -9.43174,
  'le_longitu': 160.045,
  'le_elevati': '28',
  'le_heading': 68.0,
  'le_displac': None,
  'he_ident': '24',
  'he_latitud': -9.42426,
  'he_longitu': 160.064,
  'he_elevati': '14',
  'he_heading': '248',
  'he_displac': None,
  'ObjectID': 10420,
  'type_1': 'AFIS',
  'descriptio': 'INFO',
  'frequency_': 118.1},
 'geometry': {'type': 'Point',
  'coordinates': [160.05499268, -9.42800045, 0.0]}}
"""




def natural_earth_data():
	import zipfile
	# https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/
	# https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_1_states_provinces.zip
	zipdata = None
	us_states_zip_url = "https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_1_states_provinces.zip"
	with ureq.urlopen(us_states_zip_url) as resp:
		zipdata = BytesIO(resp.read())

	shp_data = None
	dbf_data = None
	with zipfile.ZipFile(zipdata) as zf:
		# il = zf.namelist()
		# print(il)
		# with zf.open("ne_10m_admin_1_states_provinces.shp") as f:
		# 	shp_data = f.read()
		with zf.open("ne_10m_admin_1_states_provinces.dbf") as f:
			dbf_data = f.read()




## Geopy
from geopy.geocoders import Nominatim

kwargs = {
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
}


uhg_hq_addr = "9900 Bren Road East, Minnetonka, MN, 55343"


geoloc = Nominatim(**kwargs)
result = geoloc.geocode(uhg_hq_addr)
print(result.latitude, result.longitude)