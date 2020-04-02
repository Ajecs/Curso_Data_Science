import pandas as pd 

#/// .csv import dataset /// 

# * Leer y almacenar datos en un dataframe

cars = pd.read_csv('../cars.csv')

# print(cars)
print(type(cars))

print(cars.head())  # 5 registros
print(cars.head(10)) # 10 registros
print(cars.tail()) # ultimos 5 registros
print(cars.tail(10)) # ultimos 10 registros

print(cars.shape) # (32, 12) -> cant fila + cant nro

print(cars.info(null_counts=True)) 
# * Devuelve un resumen del contenido de cada columna 

print("------------promedio---------------")
print(cars.mean()) # muestra el promedio de cada columna
print("---------------mediana-------------")
print(cars.median()) # muestra la mediana de cada columna
print("------------desviación standard---------------")
print(cars.std()) 

print(cars.max()) # valor maximo
print(cars.min()) # valor minimo
print(cars.count()) # numero de registros no nulos de cada columna
print(cars.describe()) # resumen estadistico descriptivo
