# pandas IO means input/output
import pandas as pd
df=pd.read_csv('ZILLOW-N15963_ZRISFRR.csv')

print(df.head())
# set the "Date" to be the index, and the "inplace" to be true
df.set_index('Date',inplace=True)
# now the new index for the new "Date_index.csv", the index is the "Date"
df.to_csv('Date_index.csv')

df=pd.read_csv('Date_index.csv')
print(df.head())

#index_col=0 means that we do not need the index
df=pd.read_csv('Date_index.csv',index_col=0)
print(df.head())

# index is not a column
# here we rename the column
df.columns=['Austin_HPI']
print(df.head())

# next thing we want ot save it as a csv file
df.to_csv('new_index.csv')
# the new file create has no the title header
df.to_csv('new_index_no_head.csv',header=False)

# then we can input the data without head with the title that we want to name
df=pd.read_csv('new_index_no_head.csv',names=['Date','HPI'])
# rename the column,not forget the "inplace-True"
df.rename(columns={'HPI':'77006'},inplace=True)
print(df.head())

