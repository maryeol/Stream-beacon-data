from datetime import datetime
from time import sleep

import pandas as pd

idf = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])

idf['distance']=idf['data'] + 1
#print(idf)
fdf = idf[['key', 'distance']]
rdf = fdf.groupby('key').mean()
print(rdf)
print(idf[-5:])

#to drop rows which distance < 5

index_names = idf[idf['distance'] < 5].index
idf.drop(index_names, inplace=True)
#print(idf)


#fdf = idf.groupby('key').mean()
#print(fdf)


t1 = datetime.now()
t1 = t1.time().second
print(t1)
sleep(5)
t2=datetime.now()
t2 = t2.time().second
print(t2)
print(t2 - t1)

