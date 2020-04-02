import pandas as pd

#  * Crear un Series Object en pandas

data = [1, 2, 3, 4]

series1 = pd.Series(data)
# Cambiado indice ->
series2 = pd.Series(data, index=['a', 'b', 'c', 'd'])

print(series1)
print(type(series1))
print(series2)