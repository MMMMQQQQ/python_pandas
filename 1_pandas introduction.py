import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data
from pandas_datareader import DataReader
import pandas_datareader as pdr

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

import pandas_datareader as pdr
df=pdr.DataReader("XOM", "yahoo", start, end)

# print(df)

# This prints the first 5 rows of the dataframe
print(df.head())

df['Adj Close'].plot()
plt.show()
