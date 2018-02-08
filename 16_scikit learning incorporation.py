import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
from sklearn import svm, preprocessing, cross_validation

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

# print(housing_data.head())

housing_data['ma_apply_example']=pd.rolling_apply(housing_data['M30'],10,moving_average)
# housing_data['ma_apply_example']=pd.Series.rolling(window=10,center=False).apply(moving_average,housing_data['M30'])
# housing_data['ma_apply_example']=pd.Series.rolling(window=10,center=False).apply(func=<function>,args=<tuple>,kwargs=<dict>)
# the last five datas
# print(housing_data.tail())

X=housing_data.drop(['label','US_HPI_future'],1)
X.replace([np.inf,-np.inf],np.nan,inplace=True)
X.fillna(method='bfill',inplace=True)
X=np.array(X)
X = preprocessing.scale(X)
y=np.array(housing_data['label'])
# test size will be 20%
x_train,x_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

clf=svm.SVC(kernel='linear')
clf.fit(x_train,y_train)

print(clf.score(x_test,y_test))




# print(housing_data.drop(['label','US_HPI_future'],1))