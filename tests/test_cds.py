#!/usr/bin/env python3

# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import pytest

from climetlab import load_source
from climetlab.testing import can_call_cds


@pytest.mark.skipif(
    not can_call_cds(),
    reason="No access to CDS",
)
def test_cds_csv_zip():
    s = load_source(
        "cds",
        "insitu-observations-gruan-reference-network",
        variable="air_temperature",
        year="2017",
        month="01",
        day="01",
        format="csv-lev.zip",
    )
    s.to_pandas()
    # s.to_tfdataset()


if __name__ == "__main__":
    from climetlab.testing import main

    main(globals())
