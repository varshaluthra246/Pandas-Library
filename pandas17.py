import pandas as pd
import numpy as np
d={'A' : [99,np.nan,92,99],
         'B' : [94,np.nan,92,97],
         'C' : [95, np.nan, 91, 89],
         'D' : [np.nan,np.nan,np.nan,np.nan]}
df=pd.DataFrame(d, index = ['Accounts','eco','eng','IP'])
print(df)
print(df.dropna(how='all'))
print(df.dropna(how='all',axis=1))
