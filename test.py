from datetime import datetime
from time import sleep
import pandas as pd

idf = pd.DataFrame({'ip': ['A', 'B', 'C', 'A', 'B', 'C'],
                    'mac': ['10' , '20' , '30' , '50' , '20' , '40'],
                   'data': [1,2,3,4,5,6]}
                   , columns=['ip', 'mac','data'])
# idf = idf.groupby(['ip', 'mac']).mean()
# print(idf)
#print(idf.groupby(['ip', 'mac']).mean())
fdf = idf.loc[ idf['ip'] == 'A']
print(fdf)
fdf = fdf.drop(fdf.loc[fdf['mac'] == '10'].index , inplace=True)
print(fdf)
