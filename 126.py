"""
126. Want to interpolate an xarray Dataset?

🌟 The `interp` method is user-friendly!

📈 For non-gridded, 1D output, create matching DataArrays to use with interp.

#python #dataprocessing #datasci
"""

import xarray as xr

ds = xr.tutorial.open_dataset("air_temperature").isel(time=0)

# creates 3x3 grid: (40, 200), (40, 250), (40, 300), (50, 200), ...
ds.interp(lat=[40, 50, 60], lon=[200, 250, 300])

# interpolate to 3 points: (40, 200), (50, 250), (60, 300)
lat_da = xr.DataArray([40, 50, 60], name="lat", dims=["index"])
lon_da = xr.DataArray([200, 250, 300], name="lon", dims=["index"])
ds.interp(lat=lat_da, lon=lon_da)
