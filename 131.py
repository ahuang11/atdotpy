"""
131. 🐼 pandas for all your datetime needs

📆 Don't write your own date string parser; simply use pandas to parse it for you!

It's also easy to create a range of dates with pandas.

Code 👇

#python #pandas #datetime
"""

import pandas as pd

start_dt = pd.to_datetime("Sep 20, 2023 9:58 PM")
offset = pd.to_timedelta("1D")  # 1 days
dt_range = pd.date_range(start_dt, start_dt + offset, freq="12H")

print(f"{start_dt=}", f"{offset=}", f"{dt_range=}")
