# Find the sale happened on weekends(sat and sun).

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

df['day_of_week'] = df['proper_datetime'].dt.day_name()
weekend_sales = df[df['day_of_week'].isin(['Saturday', 'Sunday'])]
print(weekend_sales)


"""Output:
              datetime  total     proper_datetime day_of_week
3     13-07-2019 13:19  14800 2019-07-13 13:19:00    Saturday
4     13-07-2019 13:22  15600 2019-07-13 13:22:00    Saturday
5     13-07-2019 14:54  15800 2019-07-13 14:54:00    Saturday
6     13-07-2019 15:08  15800 2019-07-13 15:08:00    Saturday
7     13-07-2019 15:09  14000 2019-07-13 15:09:00    Saturday
...                ...    ...                 ...         ...
2415  02-05-2020 11:37  19500 2020-05-02 11:37:00    Saturday
2416  02-05-2020 11:39  19800 2020-05-02 11:39:00    Saturday
2417  02-05-2020 12:15  14300 2020-05-02 12:15:00    Saturday
2418  02-05-2020 13:45  15000 2020-05-02 13:45:00    Saturday
2419  02-05-2020 14:45  24100 2020-05-02 14:45:00    Saturday

[1007 rows x 4 columns]
"""