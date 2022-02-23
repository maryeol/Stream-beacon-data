import pandas as pd

idf = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])

print(idf)

print(idf.groupby('key').sum())

