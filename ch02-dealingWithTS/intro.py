"""Dealing with time series in python."""

import pandas as pd
import numpy as np
from datetime import date, datetime
from datetime import timedelta
import calendar as clnd

# ------------------------------------------------------------
# pd.DatetimeIndex
# ------------------------------------------------------------

# load data
df = pd.read_csv("./data/data.csv", parse_dates=["date"])
print(df)

print(df.info())

# create time series
ts = pd.date_range(start="2023-04-01", end="2023-07-26")
print(ts[:10])

# another way
ts1 = pd.date_range(start="2023-04-01", freq="D", periods=10)
print(ts1)

# parsing to date or datetime objects from either string
# or separate columns
df1 = pd.DataFrame(
    {'year': [2021, 2022, 2023],
     'month': [3, 4, 5],
     'day': [24, 25, 26]}
)
print(df1)
print(df1.info())

ts2 = pd.to_datetime(df1)
print(ts2)

ts3 = pd.to_datetime("20210324", format="%Y%m%d")
print(ts3)

# rolling windows
s = pd.Series(np.arange(1, 11))
print(s.rolling(3).sum())

# time series would be an index with a time object and one or
# more columns with numeric or other types
rng = pd.date_range("2023-04-01", "2023-07-26", freq="D")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts[:10])

# indexing can be done with datetime objects
print(ts["2023-05-25":"2023-06-05"])

# shifting or lag the values
print(ts.shift(1)[:5])

# change the resolution of the time series objects
print(ts.asfreq("M"))

# ------------------------------------------------------------
# datetime
# ------------------------------------------------------------

today = date.today()
print(today)

# to get some other date
other_date = date(2023, 7, 25)
print(other_date)

# to get a timestamp
now = datetime.now()
print(now)

some_date = datetime(2023, 7, 5, 5, 30, 0)
print(some_date.isoformat())

# timedelta
year = timedelta(days=365)
print(year * 10)


def add(*num):
    """Pass the variable length args."""
    sum = 0
    for n in num:
        sum += n
    return sum


print(add(3, 5, 6, 7))

# calendar
for name in clnd.month_name:
    print(name, sep=",", end=" ")

print(*clnd.month_name)
print(*clnd.day_name)

# getting 1st friday of every month in 2023
for m in range(1, 13):
    cal = clnd.monthcalendar(2023, m)
    week1 = cal[0]
    week2 = cal[1]
    if week1[clnd.FRIDAY] != 0:
        res = week1[clnd.FRIDAY]
    else:
        res = week2[clnd.FRIDAY]
    print(f"{clnd.month_name[m]:<10}: {res}")
