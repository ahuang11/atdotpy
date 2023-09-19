"""
128. Want to compare YTD precipitation to climatology?

🐼 #pandas has a built-in cumsum method that will calculate the cumulative sum, grouped by year.

📈 Then, use hvPlot to plot both the climatology and year on the same plot.

#python #wxtwitter #datasci #dataviz
"""

import pandas as pd
import hvplot.pandas

# load data
df = pd.read_csv(
    "https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?"
    "network=WA_ASOS&stations=TIW&year1=2018&month1=1&day1=1&"
    "year2=2023&month2=9&day2=15&var=precip_in&var=climo_precip_in&na=blank&format=csv",
    index_col="day",
    parse_dates=True,
)[["precip_in", "climo_precip_in"]]

# get cumulative sum
df["year"] = df.index.year
cumsum_df = df.groupby("year").cumsum()
cumsum_df["year"] = df["year"]
cumsum_df["dayofyear"] = cumsum_df.index.dayofyear
cumsum_df["date"] = cumsum_df.index.date

# get last value for each year
label_df = cumsum_df.groupby("year").last().reset_index()

# create plots
plot_kwargs = dict(x="dayofyear", by="year", hover_cols=["date"])
precip_plot = cumsum_df.hvplot.step(
    y="climo_precip_in", color="black", line_dash="dashed", **plot_kwargs
)
climo_plot = cumsum_df.hvplot.step(y="precip_in", **plot_kwargs)
label_plot = label_df.hvplot.labels(y="precip_in", text="year", **plot_kwargs).opts(
    text_align="left", text_baseline="bottom"
)

# overlay plots and set labels
(precip_plot * climo_plot * label_plot).opts(
    padding=0.2,
    show_grid=True,
    title="KSEA Cumulative Precipitation",
    ylabel="Precipitation (in)",
    xlabel="Julian Day",
)
