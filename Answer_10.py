# Find out the total sales on each date.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

df['date'] = df['proper_datetime'].dt.date
total_sales_per_date = df.groupby('date')['total'].sum().reset_index()
total_sales_per_date.columns = ['Date', 'Total_Sales']
print(total_sales_per_date)


"""Output:
           Date  Total_Sales
0    2019-07-11        39600
1    2019-07-12        58000
2    2019-07-13       117400
3    2019-07-14       212000
4    2019-07-15        30900
..          ...          ...
244  2020-04-27       264600
245  2020-04-29       118100
246  2020-04-30       134100
247  2020-05-01       215700
248  2020-05-02        92700

[249 rows x 2 columns]
"""