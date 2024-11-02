import pandas as pd
details={'A' : [99,94,92,99],
         'B' : [94,94,92,97],
         'C' : [95, 89, 91, 89],
         'D' : [94,87,99,94],
         'E' : [97, 100, 99, 99]}
df=pd.DataFrame(details, index = ['Accounts','eco','eng','IP'])
print(df)
print("No. of exams conducted for each section:")
print(df.count())
print("topper's total marks in each section")
print(df.sum())
