# Load the data and display.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
print(df)


"""Output:
              datetime  total
0     11-07-2019 15:35  23800
1     11-07-2019 16:10  15800
2     12-07-2019 11:49  58000
3     13-07-2019 13:19  14800
4     13-07-2019 13:22  15600
...                ...    ...
2415  02-05-2020 11:37  19500
2416  02-05-2020 11:39  19800
2417  02-05-2020 12:15  14300
2418  02-05-2020 13:45  15000
2419  02-05-2020 14:45  24100

[2420 rows x 2 columns]
"""