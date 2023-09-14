"""
127. Unsure of when to use threads or processes?

Use threads for IO tasks (reading/writing to disk, downloading data) or subprocesses.

Use processes for packages that aren't able to bypass the GIL, but can be run in parallel.

#python #threads #processes #datasci
"""

import dask
import pandas as pd

NETWORK_STATIONS = {
    "IL_ASOS": ["ORD", "CMI", "MDW"],
    "NY_ASOS": ["JFK", "LGA", "BUF"],
    "CA_ASOS": ["SFO", "LAX", "SAN"],
}
URL_FMT = (
    "https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network={network}&{stations}"
    "&year1=1928&month1=1&day1=1&year2=2023&month2=9&day2=14&var=precip_in&na=blank&format=csv"
)


@dask.delayed
def download_precip_history(network, stations):
    print(f"Downloading {network}...")
    url = URL_FMT.format(
        network=network,
        stations="&".join([f"station={station}" for station in stations]),
    )
    return pd.read_csv(url)


# be sure to be mindful of the service's usage policy to avoid being rate limited or blocked
jobs = [
    download_precip_history(network, stations)
    for network, stations in NETWORK_STATIONS.items()
]
# good to use threads (or async) for network calls
df_list = dask.compute(*jobs, num_workers=3, scheduler="threads")
df = pd.concat(df_list)

# Finishes in 15.8 seconds serially, 6.3 seconds with threads
