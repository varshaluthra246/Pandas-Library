import pandas as pd
import numpy as np
details={'A' : [99,np.nan,92,99],
         'B' : [12,94,92,97],
         'C' : [95, 89, 91, 89],
         'D' : [94,87,np.nan,94],
         'E' : [97, np.nan, 99, 99]}
df=pd.DataFrame(details, index = ['Accounts','eco','eng','IP'])
print(df)
print(df.isnull())
