#Discriptive Statistics with pandas
import pandas as pd
import numpy as np
iprod={'Rice':{'Andhra P.':7452.4, 'Gujarat': 1930.0,'Kerala':2604.8, 'Punjab':11586.2,'Tripura':814.6,'Uttar P':13754.0},
       'Wheat':{'Andhra P.':np.NaN, 'Gujarat': 2737.0,'Kerala':np.NaN, 'Punjab':16440.5,'Tripura':0.5,'Uttar P':30056.0},
       'Pulses':{'Andhra P.':931.0, 'Gujarat': 818.0,'Kerala':1.7, 'Punjab':33.0,'Tripura':23.2,'Uttar P':2184.4},
       'Fruits':{'Andhra P.':7830.0, 'Gujarat': 11950.0,'Kerala':113.1, 'Punjab':7152.0,'Tripura':44.1,'Uttar P':140169.2}}
print(iprod.max(axis =None , skipna = None, Numeric_only = None))
print(iprod.min(axis =None , skipna = True, Numeric_only = True))

       
       
       
