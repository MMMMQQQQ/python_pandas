import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean

style.use('fivethirtyeight')

api_key="h6wdhv7vRv8o7FyNaWTj"

def create_labels(cur_hpi,fut_hpi):
    if fut_hpi>cur_hpi:
        return 1
    else:
        return 0

# we can do moving average in pandas
def moving_average(values):
    return mean(values)


housing_data=pd.read_pickle('HPI.pickle')

# to see the percent changes
housing_data=housing_data.pct_change()

# handle the "na" and "-inf"
housing_data.replace([np.inf,-np.inf],np.nan, inplace=True)

housing_data['US_HPI_future']=housing_data['United States'].shift(-1)

housing_data.dropna(inplace=True)
# print(housing_data[['US_HPI_future','United States']].head())

housing_data['label']=list(map(create_labels,housing_data['United States'],housing_data['US_HPI_future']))

print(housing_data.head())

housing_data['ma_apply_example']=pd.rolling_apply(housing_data['M30'],10,moving_average)

# the last five datas
print(housing_data.tail())
