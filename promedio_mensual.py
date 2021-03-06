import os
import pandas as pd
import numpy as np

os.chdir(os.path.join(os.environ['HOME'], 'Downloads', ))
[i for i in os.listdir() if '.csv' in i]

df = pd.read_csv('rincondaPET_2020-01-01TO2021-12-01.csv')

df['date'] = pd.to_datetime(df['date'])

df.index = df['date']

# df = df['mean']

df['mean'].plot()

df.pivot_table(index=, aggfunc=np.sum)
pd.pivot_table(df, index=[df.index.year, df.index.month], aggfunc='sum', fill_value=np.nan)

pd.unique(df['date'])