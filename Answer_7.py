# Create a sample of 700 rows from the dataset and find the latest date in the dataset.

import pandas as pd

df = pd.read_csv('bakery_sales.csv')
pd.set_option('display.max_columns', None)
df['proper_datetime'] = pd.to_datetime(df['datetime'], format="%d-%m-%Y %H:%M")

sample_df = df.sample(n=700, random_state=42)
latest_date = sample_df['proper_datetime'].max()
print("Latest date in the sample:", latest_date.date())


"""Output:
Latest date in the sample: 2020-05-02
"""