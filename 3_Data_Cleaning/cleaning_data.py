import pandas as pd

cars = pd.read_csv('../cars_null.csv')

cars = cars.rename(columns={'Unnamed: 0': 'model'})
print(cars)
# * Renombra la columna "Unnamed: 0" a "model"'

cars.qsec = cars.qsec.fillna(cars.qsec.mean())
# * Rellena los valores null de qsec con su promedio
print(cars)

cars2 = cars.drop(columns=['drat'])  # ! quita, no elimina
print(cars2)

#/// Correlación matricial /// 

df = cars[['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt',
           'qsec', 'vs', 'am', 'gear', 'carb']].corr()

# * Una matriz correlacional muestra en pantalla el
# * grado de correlacion que tiene una variable con otra.
# * Cuanto mayor sea el valor mas correlatividad existe
# * Esto significa que si un atributo cambia, y su correlatividad es alta es mayor el cambio del otro 
print(df)

#/// Modificar el tipo de datos /// 

cars.mpg = cars.mpg.astype(float)
# Cambia mpg de string a float
print(cars.info(null_counts=True)) # mpg -> float64 
