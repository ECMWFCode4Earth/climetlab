import climetlab
import climetlab_intake
import intake

csv_data = 'weather.csv'
nc_data = 'ECMWF_ERA-40_subset.nc'
zarr_data = 'example.zarr'

def test_source():

    cml.register_source(climetlab_intake)
    intake_source = cml.load_source("climetlab-intake")

    data_csv = intake_source.load_data(csv_data)
    data_nc = intake_source.load_data(nc_data)
    data_zarr = intake_source.load_data(zarr_data)

if __name__ == '__main__':
    test_source()