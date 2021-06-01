
# Standard in Python 3
import gzip

# Third party
import orjson

with gzip.open("us_states_2018.geojson.gz") as gzf:
    data = orjson.loads(gzf.read())


for i in range(8):
	print(i, " -> ", len(data.get("features")[0].get("geometry").get("coordinates")[i][0]))
