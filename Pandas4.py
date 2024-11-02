#iteritems()
import pandas as pd
dict = {'Name':["ram","pam","sam"],
        'marks': [70, 95, 80]}
df = pd.DataFrame(dict, index =['Rno. 1','Rno. 2','Rno. 3'])
print(df)
print("\n")
for i, j in df.iterrows():
    print(j)
    print("____________")
