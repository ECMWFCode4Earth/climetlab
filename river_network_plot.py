from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import xarray as xr


from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 6), edgecolor='b')
m = Basemap(projection='cyl', resolution='c', llcrnrlat=30, urcrnrlat=70,\
llcrnrlon=-20, urcrnrlon=50, )

m.drawcoastlines()
m.drawparallels(np.arange(-90., 91., 10.))
m.drawmeridians(np.arange(-180., 181., 20.))
m.drawmapboundary(fill_color=(1, 253/255, 208/255))
# m.drawcountries()
m.drawrivers()

plt.title("Example River network across Europe in matplotlib", size=16)
plt.show()