import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key="h6wdhv7vRv8o7FyNaWTj"

def state_list():
    fiddy_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states=state_list()
    main_df=pd.DataFrame()

    for abbv in states:
        query="FMAC/HPI_"+str(abbv)
        df=quandl.get(query,authtoken=api_key)
        # df=df.pct_change()


        # the get return the dataframe if there is only one column, the name is "value"
        df.columns=[abbv]

        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        # print(df)

        if main_df.empty:
            main_df=df
        else:
            main_df=main_df.join(df)

    print(main_df.head())

    pickle_out=open('fiddy_states3.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df=quandl.get("FMAC/HPI_USA",authtoken=api_key)
    df["United States"]=(df["United States"]-df["United States"][0])/df["United States"][0]*100.0
    return df

# grab_initial_state_data()

fig=plt.figure()
ax1=plt.subplot2grid((2,1),(0,0))
ax2=plt.subplot2grid((2,1),(1,0),sharex=ax1)

HPI_data=pd.read_pickle('fiddy_states3.pickle')
TX_AK_12corr=pd.rolling_corr(HPI_data['TX'],HPI_data['AK'],12)

HPI_data['TX'].plot(ax=ax1,label='TX HPI')
HPI_data['AK'].plot(ax=ax1,label='AK HPI')
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2,label='TX_AK_12corr')

# twelve data points will be choses to calculate the rolling mean
# HPI_data['TX12MA']=pd.rolling_mean(HPI_data['TX'],12)
# HPI_data['TX12STD']=pd.rolling_mean(HPI_data['TX'],12)
#
# print(HPI_data[['TX','TX12MA','TX12STD']].head())
#
#
# HPI_data[['TX','TX12MA']].plot(ax=ax1)
# HPI_data['TX12STD'].plot(ax=ax2)


# bencmark.plot(ax=ax1,color='k',linewidth=10), legend location number in matplotlib:
# https://matplotlib.org/1.3.1/users/legend_guide.html
plt.legend(loc=5)
plt.show()
