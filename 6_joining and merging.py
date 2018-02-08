import pandas as pd


df1=pd.DataFrame({'Year':[2001,2002,2003,2004],
                  'Int_rate':[2,3,2,2],
                  'US_GDP_Thousands':[50,55,65,55]},
                 )

# df2=pd.DataFrame({'HPI':[80,85,88,85],
#                   'Int_rate':[2,3,2,2],
#                   'US_GDP_Thousands':[50,55,65,55]},
#                  index=[2005,2006,2007,2008])


df3=pd.DataFrame({'Year':[2001,2003,2004,2005],
                  'Unemployment':[7,8,9,2],
                  'Low_tier_HPI':[50,52,50,53]},
                 )

# merge is to combine the same column witch has the same title
# print(pd.merge(df1,df2,on=['HPI','Int_rate']))

# join can not have the same title
# df1.set_index('HPI',inplace=True)
# df3.set_index('HPI',inplace=True)
#
# joined=df1.join(df3)
# print(joined)

# merged=pd.merge(df1,df3,on='Year')
# merged.set_index('Year',index=True)
# print(merged)

# if we want to set the df1 as the basics,
merged=pd.merge(df1,df3,on='Year',how='left')
merged.set_index('Year',inplace=True)
print(merged)