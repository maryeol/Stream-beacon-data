from datetime import datetime
from time import sleep

import pandas as pd

idf = pd.DataFrame({'ip': ['A', 'B', 'C', 'A', 'B', 'C'],
                    'mac': ['10' , '20' , '30' , '50' , '20' , '40'],
                   'data': [1,2,3,4,5,6]}
                   , columns=['ip', 'mac','data'])

print(idf)
print(idf.groupby(['ip', 'mac']).mean())



