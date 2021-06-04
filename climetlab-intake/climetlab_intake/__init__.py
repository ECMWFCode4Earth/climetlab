import pandas as pd
from climetlab import Source
import intake


class Intake(Source):
    def __init__(self):
        pass

    def load_data(self, data):
        if data.endswith('.csv'):
            data = intake.open_csv(data)
        elif data.endswith('.nc'):
            data = intake.open_netcdf(data)
        elif data.endswith('.zarr'):
            data = intake.open_zarr(data)

        return data


source = Intake()