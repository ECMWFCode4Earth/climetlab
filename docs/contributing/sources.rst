Data sources
============

A :ref:`Data source <data-sources>` is a Python class that accesses data from a
given location. Climetlab has build-in sources (the most common being the "url"
source) and a plugin can add more sources capabilities.
A Source provides access to data, the code performing the actual reading can either be
located in the Source itself or delegated to a Reader class.
See details in :ref:`Source class <reference/source>'.


Adding a new source as a plugin
-------------------------------

See https://github.com/ecmwf/climetlab-demo-source

The plugin mechanism of climetlab as follows :
 - The plugin is a python package (the pipy package name should preferably starts with "climetlab-"). The python package to import should starts with "climetlab\_".

 - When installed, the plugin register itself thanks to the entry_points in the setup.py.


    .. code-block:: python
      :emphasize-lines: 2-4

        setuptools.setup(
            entry_points={"climetlab.sources": [
                "demo-source = climetlab_demo_source:DemoSource"
                ]
            },
        )

 - Climetlab is aware of the new capability and cml.load_source("demo-source") becomes available.
