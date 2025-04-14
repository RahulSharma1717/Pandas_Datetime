# Convert the datetime column into proper datetime format, considering the data in the column is in (dd-mm-yyyy hh:mm) format.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")
df['proper_date'] = df['proper_datetime'].dt.date
print(df)


"""Output:
              datetime  total     proper_datetime proper_date
0     11-07-2019 15:35  23800 2019-07-11 15:35:00  2019-07-11
1     11-07-2019 16:10  15800 2019-07-11 16:10:00  2019-07-11
2     12-07-2019 11:49  58000 2019-07-12 11:49:00  2019-07-12
3     13-07-2019 13:19  14800 2019-07-13 13:19:00  2019-07-13
4     13-07-2019 13:22  15600 2019-07-13 13:22:00  2019-07-13
...                ...    ...                 ...         ...
2415  02-05-2020 11:37  19500 2020-05-02 11:37:00  2020-05-02
2416  02-05-2020 11:39  19800 2020-05-02 11:39:00  2020-05-02
2417  02-05-2020 12:15  14300 2020-05-02 12:15:00  2020-05-02
2418  02-05-2020 13:45  15000 2020-05-02 13:45:00  2020-05-02
2419  02-05-2020 14:45  24100 2020-05-02 14:45:00  2020-05-02

[2420 rows x 4 columns]
"""

