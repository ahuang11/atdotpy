"""
126. Want to interpolate an xarray Dataset?

Interp method is easy to use!

If you don't want gridded output, i.e. 1D output, create new
DataArrays with a matching dim to pass to interp.
"""

import xarray as xr
import pandas as pd

ds = xr.tutorial.open_dataset("air_temperature").isel(time=0)

# creates 3x3 grid: (40, 200), (40, 250), (40, 300), (50, 200), ...
ds.interp(lat=[40, 50, 60], lon=[200, 250, 300])

# interpolate to 3 points: (40, 200), (50, 250), (60, 300)
lat_da = xr.DataArray([40, 50, 60], name="lat", dims=["index"])
lon_da = xr.DataArray([200, 250, 300], name="lon", dims=["index"])
ds.interp(lat=lat_da, lon=lon_da)
