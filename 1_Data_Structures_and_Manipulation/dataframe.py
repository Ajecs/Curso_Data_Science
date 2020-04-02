import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5]

# * Creando un dataFrame usando una lista

df = pd.DataFrame(data) 

print(df)
print(type(df))

# * Creando un dataFrame usando un diccionario

dictionary = {'fruits': ['apple', 'banana', 'mango'], 'count': [10, 20, 15] }

df2 = pd.DataFrame(dictionary)

print(df2)

# * Creando un dataFrame usando series

series = pd.Series([6, 12], index=['a', 'b'])
df3 = pd.DataFrame(series)
print(df3)

# * Creando un dataFrame usando Numpy array

numpy_array = np.array([[50000, 60000], ['Nicolas', 'Pablo']])

df4 = pd.DataFrame({'name': numpy_array[1], 'salary': numpy_array[0]})
print(df4)