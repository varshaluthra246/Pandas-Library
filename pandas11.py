import pandas as pd
import numpy as np
df=pd.DataFrame({'First_name' : ['Jivin',np.nan,'ruhi','raunaq','Mike'],
                 'Last_name' : ['Arora',np.nan,'hyat','singh','John'],
                 'Age' : [42.0,np.nan,36.0,24.0,73.0],
                 'Sex' : ['M',np.nan,'f','m','f'],
                 'ValBefore':[4.0,np.nan,np.nan,2.0,3.0],
                 'ValAfter':[25.0,np.nan,np.nan,62.0,70.0]})
#print(df)
print(df.dropna(axis=1))
print(df.isnull())
df[df.isnull()]
df1=df.dropna()
print(df1)
print(df.dropna(how = 'all'))

