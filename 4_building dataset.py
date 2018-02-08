import quandl
import pandas as pd

api_key="h6wdhv7vRv8o7FyNaWTj"
# api_key=open('quandlapikey.txt','r').read()
#
# df=quandl.get('ZILLOW/N5508_ZHVITTY',authtoken=api_key)
#
# print(df.head())

# read the data in the site,list those table in dataframe
fiddy_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# # this is a list
# print(fiddy_states)

# # this is a dataframe
# print(fiddy_states[0])

# this is a COLUMN
print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    print("FMAC/HPI_"+str(abbv))

# now we will create a new dataframe based on the previous outputs
