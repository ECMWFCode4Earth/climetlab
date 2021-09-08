from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8, 6), edgecolor='b')
m = Basemap(projection='cyl', resolution='c', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
m.drawparallels(np.arange(-90., 91., 30.))
m.drawmeridians(np.arange(-180., 181., 60.))
m.drawmapboundary(fill_color=(1, 253/255, 208/255))

plt.title("Example Hello World plot from Magics tutorial in matplotlib", size=16)
plt.show()