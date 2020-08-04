# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#


import os
import yaml


def load(collection, name):
    path = os.path.join(os.path.dirname(__file__), collection, name)
    with open(path + ".yaml") as f:
        return yaml.load(f.read(), Loader=yaml.SafeLoader)
