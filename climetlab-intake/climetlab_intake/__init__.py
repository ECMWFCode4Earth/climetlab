import pandas as pd
from climetlab import Source
import intake


class Intake(Source):
    def __init__(self):
        pass

    def load_data(self, data):
        data = intake.open_csv(data)
        return data