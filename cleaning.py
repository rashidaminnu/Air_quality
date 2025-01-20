import pandas as pd
df =pd.read_csv("city_day.csv")
#print(df.info())
#print(df.describe())
#print (df.isnull().sum())

#dropping columns

df.drop(columns=["Benzene","Toluene","Xylene","NO","City","Date","AQI_Bucket","NO2"],inplace=True)
#print(df.head())
df.fillna(df.mean(),inplace=True)
df.to_csv('cleaningdata.csv',index=False)
 