#Mean mode and median functions in DataFrame
import pandas as pd
df = pd.DataFrame([[10,20,30,40],[7,14,21,28],[55,15,8,12],[15,14,1,8],[7,1,1,8],[5,4,9,2]],columns=['Apple', 'Orange', 'Banana', 'peer'],index = ['Basket1','Basket2','Basket3','Basket4','Basket5','Basket6'])
print(df)
print("Calculating the Mean")
#print(df['Basket2'].mean)
print("Calculating the Median")
print(df.median())
print("Calculating the Mode")
print(df.mode())
