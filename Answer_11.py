# Find out total sale on each day.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

df['day_of_week'] = df['proper_datetime'].dt.day_name()
weekday_sales = df.groupby('day_of_week').agg(
    total_sales=('total', 'sum')
)
print(weekday_sales.sort_values(by='day_of_week').reset_index())


"""Output:
  day_of_week  total_sales
0      Friday      8177700
1      Monday      6887000
2    Saturday      9098000
3      Sunday     11287500
4    Thursday      8140700
5     Tuesday        56000
6   Wednesday      7590600
"""