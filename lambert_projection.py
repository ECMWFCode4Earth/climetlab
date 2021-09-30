from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8, 6), edgecolor='b')

m = Basemap(projection='laea', resolution='c', llcrnrlat=0, urcrnrlat=70, \
    llcrnrlon=-80, urcrnrlon=160, lat_0=0, lon_0=-137.)

m.drawcoastlines()
m.drawparallels(np.arange(-90., 91., 10.), labels=[False,True,True,False])
m.drawmeridians(np.arange(-180., 181., 20.), labels=[True,False,False,True])

m.drawmapboundary(fill_color=(1, 253/255, 208/255))

plt.title("Example Lambert projection from Magics tutorial in matplotlib", size=16, y=1.08)
plt.show()