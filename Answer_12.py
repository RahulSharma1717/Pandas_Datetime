# Find rows where the transaction happened in the afternoon (12 PM - 6 PM)

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

df['hour'] = df['proper_datetime'].dt.hour
afternoon_sales = df[(df['hour'] >= 12) & (df['hour'] <= 18)]
print(afternoon_sales)


"""Output:
              datetime  total     proper_datetime  hour
0     11-07-2019 15:35  23800 2019-07-11 15:35:00    15
1     11-07-2019 16:10  15800 2019-07-11 16:10:00    16
3     13-07-2019 13:19  14800 2019-07-13 13:19:00    13
4     13-07-2019 13:22  15600 2019-07-13 13:22:00    13
5     13-07-2019 14:54  15800 2019-07-13 14:54:00    14
...                ...    ...                 ...   ...
2413  01-05-2020 15:03  14800 2020-05-01 15:03:00    15
2414  01-05-2020 15:19  14500 2020-05-01 15:19:00    15
2417  02-05-2020 12:15  14300 2020-05-02 12:15:00    12
2418  02-05-2020 13:45  15000 2020-05-02 13:45:00    13
2419  02-05-2020 14:45  24100 2020-05-02 14:45:00    14

[1712 rows x 4 columns]
"""