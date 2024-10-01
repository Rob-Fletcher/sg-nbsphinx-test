"""
Example File
============

Example file just to test ipyleaflet widgets.
"""

from ipyleaflet import Map, basemaps

center = [38.128, 2.588]
zoom = 5

Map(basemap=basemaps.OpenStreetMap.Mapnik, center=center, zoom=zoom)


#%%
# And this is the end of the example.