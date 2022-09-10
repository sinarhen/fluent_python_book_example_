from collections import namedtuple


metro_data = {
    ('Tokyo', 'JP' ),
    ('Sao-Paulo', 'BRA' ),
    ('Washington', 'US' ),

}
lat_long = namedtuple('LatLong', 'lat long')
metro_polis = namedtuple('City', 'name cc coord')

metro_areas = [metro_polis(name, cc, coord, lat_long(lat, long)) for name, cc, coord in metro_data]
print(metro_areas)