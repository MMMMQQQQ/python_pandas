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
ax1=plt.subplot2grid((1,1),(0,0))

HPI_data=pd.read_pickle('fiddy_states3.pickle')



# bencmark=HPI_Benchmark()
#
# # HPI_data['TX']=HPI_data['TX']*2
# #
# # print(HPI_data['TX'])
#
TX1yr=HPI_data['TX'].resample('A',how='mean')
print(TX1yr.head())
HPI_data['TX'].plot(ax=ax1,label='Monsthly TX HPI')
TX1yr.plot(ax=ax1, label='Yearly TX HPI')

# bencmark.plot(ax=ax1,color='k',linewidth=10)
plt.legend(loc=4)
plt.show()

# correlations
#
#
# this will generate the correlation table
# HPI_State_Correlation is a dataframe

