# import xarray as xr
# import pygrib
# from mpl_toolkits.basemap import Basemap
# from mpl_toolkits.basemap import shiftgrid
# import numpy as np
# from numpy import linspace
# from numpy import meshgrid
# import matplotlib.pyplot as plt

def field_plotting(file):
	fig = plt.figure(figsize=(8, 6), edgecolor='b')
	grib_file = pygrib.open(file)
	
	# grib_msl = pygrib.open('msl.grib')
	# grib_prec = pygrib.open('precip.grib')

	grib_file_data = grib_file.select()[0]
	data = grib_file_data.values

	lon_vals = np.linspace(float(grib_file_data['longitudeOfFirstGridPointInDegrees']), \
	float(grib_file_data['longitudeOfLastGridPointInDegrees']), int(grib_file_data['Ni']) )

	lat_vals = np.linspace(float(grib_file_data['latitudeOfFirstGridPointInDegrees']), \
	float(grib_file_data['latitudeOfLastGridPointInDegrees']), int(grib_file_data['Nj']) )

	data, lon_vals = shiftgrid(180., data, lon_vals, start=False)
	grid_lon_vals, grid_lat_vals = np.meshgrid(lon_vals, lat_vals)

	m = Basemap(projection='cyl', resolution='c', llcrnrlat=20, urcrnrlat=70,
	llcrnrlon=-110, urcrnrlon=-30, )

	x_val, y_val = m(grid_lon_vals, grid_lat_vals)

	# cs_msl = m.pcolormesh(x_msl, y_msl, data_msl, shading='flat', cmap=plt.cm.rainbow)

	cs_data = m.pcolormesh(x_prec, y_prec, data_prec, shading='auto',
	cmap=plt.cm.nipy_spectral_r)

	m.drawcoastlines()
	m.drawparallels(np.arange(-90.,91.,30.))
	m.drawmeridians(np.arange(-180.,181.,60.))
	m.drawmapboundary(fill_color=(1, 253/255, 208/255))

	# plt.colorbar(cs_msl, orientation='vertical', shrink=0.5)
	plt.colorbar(cs_data, orientation='vertical', shrink=0.5)

	# plt.title("Example Mean Sea Level pressure field from Magics tutorial in matplotlib",size=16)
	plt.title("Example Precipitation field from Magics tutorial in matplotlib",size=16)
	plt.show()
