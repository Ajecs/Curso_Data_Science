import pandas as pd 

cars = pd.read_csv('../cars_null.csv')

print(cars.iloc[:, 0]) # Imprime la columna 0 -> modelo
print(cars.iloc[0:5, 4]) # Imprime los primeros 5 valores -> hp
print(cars.iloc[:, :]) # Imprime todas las filas y columnas -> hp
print(cars.iloc[6:, 4:]) # Imprime desde la fila 6 y desde la columna 4

print(cars.loc[:, 'mpg']) # Imprime todas las filas del atributo mpg
print(cars.loc[:6, 'mpg']) # Imprime desde la fila 1 a la 6 del atributo mpg
print(cars.loc[:6, 'mpg':'qsec']) # Imprime desde la fila 1 a la 6 del atributo mpg al qsec
