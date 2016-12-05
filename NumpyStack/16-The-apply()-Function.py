import numpy as np
import pandas as pd

# Example using data_1d.csv

df = pd.read_csv('data_1d.csv')
df.columns = ['x', 'y']
df['xy'] = df.apply(lambda row: row['x']*row['y'], axis=1)

print(df)