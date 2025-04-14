# Display the data of the sale that happened between 1st Aug 2019 and 01 Dec 2019.

import pandas as pd
from datetime import datetime

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

df['date'] = df['proper_datetime'].dt.date
start_date = datetime(2019, 8, 1).date()
end_date = datetime(2019, 12, 1).date()
filtered_dates = df[(df['date'] > start_date) & (df['date'] < end_date)]
print(filtered_dates)


"""Output:
              datetime  total     proper_datetime        date
147   02-08-2019 11:03  19900 2019-08-02 11:03:00  2019-08-02
148   02-08-2019 11:04  14100 2019-08-02 11:04:00  2019-08-02
149   02-08-2019 11:06  18000 2019-08-02 11:06:00  2019-08-02
150   02-08-2019 11:19  16400 2019-08-02 11:19:00  2019-08-02
151   02-08-2019 11:31  17300 2019-08-02 11:31:00  2019-08-02
...                ...    ...                 ...         ...
1082  30-11-2019 13:01  38200 2019-11-30 13:01:00  2019-11-30
1083  30-11-2019 13:44  25100 2019-11-30 13:44:00  2019-11-30
1084  30-11-2019 13:49  20300 2019-11-30 13:49:00  2019-11-30
1085  30-11-2019 14:24  15800 2019-11-30 14:24:00  2019-11-30
1086  30-11-2019 17:04  27600 2019-11-30 17:04:00  2019-11-30

[940 rows x 4 columns]
"""