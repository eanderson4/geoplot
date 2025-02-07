"""
KDEPlot of two NYC traffic accident contributing factors
========================================================

This example shows a ``kdeplot`` of traffic accident densities for two common contributing factors:
loss of consciousness and failure to yield right-of-way. It shows how the geospatial incidence
pattern differs between the two: lost consciousness crashes are more localized to Manhattan.
"""


import geopandas as gpd
import geoplot as gplt
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

nyc_boroughs = gpd.read_file(gplt.datasets.get_path('nyc_boroughs'))
nyc_collision_factors = gpd.read_file(gplt.datasets.get_path('nyc_collision_factors'))


proj = gcrs.AlbersEqualArea(central_latitude=40.7128, central_longitude=-74.0059)
fig = plt.figure(figsize=(10,5))
ax1 = plt.subplot(121, projection=proj)
ax2 = plt.subplot(122, projection=proj)

gplt.kdeplot(
    nyc_collision_factors[
        nyc_collision_factors['CONTRIBUTING FACTOR VEHICLE 1'] == "Failure to Yield Right-of-Way"
    ],
    cmap='Reds',
    projection=proj,
    shade=True, shade_lowest=False, 
    clip=nyc_boroughs.geometry,
    ax=ax1
)
gplt.polyplot(nyc_boroughs, zorder=1, ax=ax1)
plt.title("Failure to Yield Right-of-Way Crashes, 2016")

gplt.kdeplot(
    nyc_collision_factors[
        nyc_collision_factors['CONTRIBUTING FACTOR VEHICLE 1'] == "Lost Consciousness"
    ],
    cmap = 'Reds',
    projection=proj,
    shade=True, shade_lowest=False,
    clip=nyc_boroughs.geometry,
    ax=ax2
)
gplt.polyplot(nyc_boroughs, zorder=1, ax=ax2)
plt.title("Loss of Consciousness Crashes, 2016")

plt.savefig("nyc-collision-factors.png", bbox_inches='tight', pad_inches=0.1)
