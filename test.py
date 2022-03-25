from datetime import datetime
from time import sleep
import pandas as pd

idf = pd.DataFrame({'ip': ['A', 'B', 'C', 'A', 'B', 'C'],
                    'mac': ['10', '20', '30', '50', '20', '40'],
                    'data': [1, 2, 3, 6, 5, 4]}
                   , index=["i1", "i2", "i3", "i4", "i5", "i6"]
                   , columns=['ip', 'mac', 'data'])


print(idf)
idf2 = idf.groupby(['ip', 'mac']).last()
print(idf2)
#print(idf2.sort_values(by = ['data']))

#print(idf.sort_values(by = ['data']))


# print(idf2)
# while True:
#     a = 'A'
#     b = '10'
#     df = idf2.drop((a, b), axis=0)
#     print(df)









# print(idf.index)
# print(idf.loc["i1"]['data'])
#
# idf2 = idf.groupby(['ip', 'mac']).mean()
# print(idf2.index)
# df2 = pd.DataFrame(index=idf2.index)
# print(df2)
# print(idf2.loc[('A', '10')]['data'])
# a = 'A'
# b = '10'
# print(type(idf2.loc[(a, b)]['data']))
# idff = pd.DataFrame(idf2.copy(), index = ["i1" ,  "i2" , "i3"])
# print(idff)
# print(idf2['data'] )


# DataFrame.iat
# Series.at
