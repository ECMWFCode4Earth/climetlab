import warnings

class NoMatplotlib:
    def plot(self, *args, **kwargs):
        raise NotImplementedError(
            "Matplotlib was not loaded successfully, plotting not supported."
        )

try:
    import matplotlib
    import matplotlib.pyplot as plt
except Exception as e:
    warnings.warn(str(e))
    plt = NoMatplotlib()

class Action:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @property
    def action(self):
        return self.__class__.__name__


class mmap(Action):
    def page_ratio(self):
        # TODO: Use projection
        south = self.kwargs.get("subpage_lower_left_latitude", -90.0)
        west = self.kwargs.get("subpage_lower_left_longitude", -180)
        north = self.kwargs.get("subpage_upper_right_latitude", 90.0)
        east = self.kwargs.get("subpage_upper_right_longitude", 180.0)
        return (north - south) / (east - west)

def plot(*args, **kwargs):
    return plt.plot(*args, **kwargs)
