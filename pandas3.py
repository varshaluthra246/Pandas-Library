#iteritems()
import pandas as pd
diSales = { 'yr1' : {'Qtr1' : 34500,'Qtr2' : 56000,'Qtr3' : 47000,'Qtr4' : 49000},
            'yr2' : {'Qtr1' : 44900,'Qtr2' : 46100,'Qtr3' : 57000,'Qtr4' : 59000},
            'yr3' : {'Qtr1' : 54500,'Qtr2' : 51000,'Qtr3' : 57000,'Qtr4' : 58500}}
df1 = pd.DataFrame(diSales)
for (col,colSeries) in df1.iteritems():
    print("Column Index:",col)
    print("Containing:")
    print(colSeries)
    print("\n")
