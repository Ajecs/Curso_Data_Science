import pandas as pd

cars = pd.read_csv('../cars.csv')

cars['am'] = 1
print(cars) # Asigna el valor 1 a todos los registros del atributo am

#/// Aplicar una funcion ///

f = lambda x: x*2
cars['am'] = cars['am'].apply(f)
print(cars)

#/// ordenar una columna ///

print("--------sort ascendent by cyl--------------") 
print(cars.sort_values(by='cyl')) # de forma ascendente
print("--------sort descendent by cyl--------------") 
print(cars.sort_values(by='cyl', ascending=False))  # de forma descendente

#/// Filtrando datos ///
print("--------more than 6 cylinders--------------")
print(cars['cyl'] > 6) # boolean

# * obtener los registros filtrados
print("--------only 6 cylinders cars--------------")
filter1 = cars['cyl'] > 6 # filtrar
print(cars[filter1])  # imprime los registros con mas de 6 cilindros

# * Combinar filtros
print("--------only 6 cylinders and 300 hp cars--------------")
filter2 = (cars['cyl'] > 6) & (cars['hp'] > 300) 
print(cars[filter2])

