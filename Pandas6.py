#Binary Operations on Panda's DataFrame
import pandas as pd
d1 = {'p1' : {'1':700, '2':975, '3':970, '4':900},
      'p2' : {'1':490, '2':460, '3':570, '4':590}}
d2 = {'p1' : {'1':1100, '2':1275, '3':1270, '4':1400},
      'p2' : {'1':1400, '2':1260, '3':1570, '4':1190}}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
print("Team 1's Performance")
print(df1)
print("Team 2's Performance")
print(df2)

print("Points Earned by both teams")
print(df1+df2)
print(df1-df2)
print(df2-df1)

print("Team1- Team2 : Point's difference")
print(df1.rsub(df2))
print("Team2- Team1 : Point's difference")
print(df2.rsub(df1))

print("Averge Points Scored by each Player")
av=(df1+df2)/2
print(av)





      
