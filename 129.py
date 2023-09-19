"""
129. 10848x10848 pixels, high-res satellite image taking forever to render?

You may not need the full resolution rendered on a global extent.

Use `rasterize` from HoloViews Datashader to intelligently regrid and resample on the fly!

Code 👇

#python #GOES18 #NASA #satellite
"""

import geoviews as gv
import rioxarray as rio
from holoviews.operation.datashader import rasterize

gv.extension("bokeh")

# https://www.star.nesdis.noaa.gov/GOES/fulldisk.php?sat=G17
da = rio.open_rasterio("GOES18-ABI-FD-GEOCOLOR-10848x10848.tif")
# preprocess bands into RGBA format
ds = da.to_dataset("band").rename({1: "R", 2: "G", 3: "B", 4: "A"})
ds["x"] = ds["x"] - 180  # convert from 0:360 to -180:180

rasterize(gv.RGB(ds).opts(width=600, height=600))
