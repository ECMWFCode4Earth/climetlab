import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import xarray as xr

temp_data = 't850.grib'

dsgrib = xr.open_dataset(temp_data, engine='cfgrib')

dsarray = dsgrib.to_array()
fig = plt.figure(figsize=(8, 6), edgecolor='b')


m = Basemap(projection='cyl', resolution='c', llcrnrlat=-90, urcrnrlat=90,
llcrnrlon=0, urcrnrlon=360, )
# m = Basemap(projection='cyl', resolution='c', llcrnrlat=-90, urcrnrlat=90,
# llcrnrlon=0, urcrnrlon=180, )
m.drawcoastlines()
m.drawparallels(np.arange(-90., 91., 30.))
m.drawmeridians(np.arange(-180., 181., 60.))
m.drawmapboundary(fill_color=(1, 253/255, 208/255))

lons = dsgrib.variables['longitude'][:]
lats = dsgrib.variables['latitude'][:]

lon, lat = np.meshgrid(lons, lats)
# xi, yi = m(lon, lat)

m.contourf(lon, lat, dsarray[0])

plt.colorbar()
plt.title("Example temperature shading plot from Magics tutorial in matplotlib", size=16)
plt.show()