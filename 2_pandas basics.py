import pandas as pd
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data
from pandas_datareader import DataReader
import pandas_datareader as pdr
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

web_stats={'Day':[1,2,3,4,5,6],
           'Visitors':[43,53,34,45,64,34],
           'Bounce_Rate':[65,72,62,64,54,66]}

df=pd.DataFrame(web_stats)

# print(df)
# # print the first five rows
# print(df.head())
# # print the last five rows
# print(df.tail())
# # print the last two rows
# print(df.tail(2))


# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2015, 8, 22)
#
# import pandas_datareader as pdr
# df=pdr.DataReader("XOM", "yahoo", start, end)
#
# # print(df)
#
# # This prints the first 5 rows of the dataframe
# print(df.head())
#
# df['Adj Close'].plot()
# plt.show()

# set the day as the index, using this function, in fact, we have returned the new dataframe
#
# print(df.set_index('Day'))
# print(df.head())

# df2=df.set_index('Day')
# print(df2.head())

# the second way to reach the same effection
# df.set_index('Day',inplace=True)
# print(df.head())

# # print out some column, for the second way, name is not allowed to have the space
# print(df['Visitors'])
# print(df.Visitors)

# # print out two columns
# print(df[['Bounce_Rate','Visitors']])


# # change the pandas form to the list
# print(df.Visitors.tolist())
# # print out two columns to the list
# print(np.array(df[['Bounce_Rate','Visitors']]))


# convert the np array to the dataframe
df2=pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))
print(df2)
