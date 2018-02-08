import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key="h6wdhv7vRv8o7FyNaWTj"

def mortgare_30y():
    df = quandl.get("FMAC/MORTG",trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"] - df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('D').mean()
    df=df.resample('M').mean()
    #
    # change the name of the title
    df.columns=['M30']
    return df


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
    df.columns = ["United States"]
    df["United States"]=(df["United States"]-df["United States"][0])/df["United States"][0]*100.0
    return df


m30=mortgare_30y()
print(m30.head())
HPI_data=pd.read_pickle('fiddy_states3.pickle')
# print(HPI_data.head())

HPI_bench=HPI_Benchmark()
# print(HPI_bench)

state_HPI_M30=HPI_data.join(m30)

# correlation is "M30"
print(state_HPI_M30.corr()['M30'].describe())
# print(state_HPI_M30.corr())
