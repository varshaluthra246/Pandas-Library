import pandas as pd
df=pd.DataFrame({'A' : [12,4,5,44,1],
                 'B' : [ 5, 2, 54, 3, 2],
                 'C' : [20,16,7,3,8],
                 'D' : [14, 3, 17,2,6]})
'''print(df['A'].max())
print(df['B'].max())
print(df['C'].max())
print(df['D'].max())'''
print(df.max()['A'])
print(df[['A','C']].max())
print(df)
print(df.idxmax())
#print(df.max(axis=1, skipna = False))
'''
df=pd.DataFrame({'A' : [12,4,5,None,1],
                 'B' : [ 5, 2, 54, 3, None],
                 'C' : [20,16,7,3,8],
                 'D' : [14, 3, None,2,6]})
print(df)
print(df.min(axis = 1, skipna = True))
'''

