# Create a sample of 700 rows from the dataset and arrange them in ascending order on behalf of date.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

sample_df = df.sample(n=700, random_state=42)
print("The sample taken out from dataframe:\n", sample_df)
sorted_sample = sample_df.sort_values(by='proper_datetime', ascending=True)
print("\nThe sample after getting sorted:\n", sorted_sample)


"""Output:
The sample taken out from dataframe:
               datetime  total     proper_datetime
410   30-08-2019 11:16  14800 2019-08-30 11:16:00
199   07-08-2019 13:28  17600 2019-08-07 13:28:00
1674  14-02-2020 13:46  57500 2020-02-14 13:46:00
1124  05-12-2019 13:56  14800 2019-12-05 13:56:00
1355  04-01-2020 12:51  24800 2020-01-04 12:51:00
...                ...    ...                 ...
1004  18-11-2019 13:55  14000 2019-11-18 13:55:00
1320  29-12-2019 14:32  15000 2019-12-29 14:32:00
162   03-08-2019 11:20  16600 2019-08-03 11:20:00
1211  15-12-2019 13:41  15000 2019-12-15 13:41:00
2070  21-03-2020 12:07  14300 2020-03-21 12:07:00

[700 rows x 3 columns]

The sample after getting sorted:
               datetime  total     proper_datetime
8     13-07-2019 15:23  19100 2019-07-13 15:23:00
13    14-07-2019 11:59  19800 2019-07-14 11:59:00
18    14-07-2019 14:51  25600 2019-07-14 14:51:00
23    17-07-2019 13:23  14800 2019-07-17 13:23:00
25    17-07-2019 16:32  18100 2019-07-17 16:32:00
...                ...    ...                 ...
2406  01-05-2020 11:10  21200 2020-05-01 11:10:00
2410  01-05-2020 12:10  18300 2020-05-01 12:10:00
2411  01-05-2020 13:05  28400 2020-05-01 13:05:00
2415  02-05-2020 11:37  19500 2020-05-02 11:37:00
2417  02-05-2020 12:15  14300 2020-05-02 12:15:00

[700 rows x 3 columns]
"""