import pandas as pd

cars = pd.read_csv('../cars.csv')
# /// ordenar una columna ///

print("--------sort ascendent by cyl--------------")
print(cars.sort_values(by='cyl'))  # de forma ascendente
print("--------sort descendent by cyl--------------")
print(cars.sort_values(by='cyl', ascending=False))  # de forma descendente
