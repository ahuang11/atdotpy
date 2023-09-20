"""
130. Speed up loading chunks of data with zarr

In the previous example, we rendered the satellite imagery from a TIF file.

However, if we first convert TIF into zarr, we can
speed up rendering the needed chunks of data, in parallel.

Code 👇
"""

import xarray as xr
import geoviews as gv
import rioxarray as rio
from holoviews.operation.datashader import rasterize

gv.extension("bokeh")

# https://www.star.nesdis.noaa.gov/GOES/fulldisk.php?sat=G17
da = rio.open_rasterio("GOES18-ABI-FD-GEOCOLOR-10848x10848.tif")
# preprocess bands into RGBA format
ds = da.to_dataset("band").rename({1: "R", 2: "G", 3: "B", 4: "A"})
ds["x"] = ds["x"] - 180  # convert from 0:360 to -180:180

# convert to zarr
ds.to_zarr("GOES18-ABI-FD-GEOCOLOR-10848x10848.zarr", mode="w")

# # load zarr
ds_zarr = xr.open_zarr("GOES18-ABI-FD-GEOCOLOR-10848x10848.zarr")

(
    rasterize(gv.RGB(ds).opts(title="tif", shared_axes=False))
    + rasterize(gv.RGB(ds_zarr).opts(title="zarr", shared_axes=False))
)
