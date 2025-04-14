# Create a sample of 700 rows from the dataset and find the oldest date in the dataset.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

sample_df = df.sample(n=700, random_state=42)
oldest_date = sample_df['proper_datetime'].min()
print("Oldest date in the sample:", oldest_date.date())


"""Output:
Oldest date in the sample: 2019-07-13
"""