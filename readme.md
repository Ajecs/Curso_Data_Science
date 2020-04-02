<<<<<<< HEAD
=======
<body>
  <article class="markdown-body">

>>>>>>> 5b2982f0eacbafc3f3f3a36591b3412a3f128ef0
  # Pandas 

  - Pandas proviene de 2 terminos: PANel DAta
  - Instalación de <span>pandas</span> -> `pip install pandas` 
    
  ## Estructura de datos en Pandas

  De acuerdo a la dimension hay tres tipos de estructura:
  * 1 dimensión ->  <span> Series Object </span>
  * 2 dimensiones -> <span> DataFrame </span>
  * 3 dimensiones o más -> <span> Panel Data </span>

  ### <ins>Series object</ins>
  * En python es un array unidimensional 
  * Contiene datos similares o de de diverso tipo
  * Pueden utilizarse 3 tipos de estructuras 
    * Arreglos
    * Diccinarios
    * Escalar

  ### <ins>DataFrame</ins>
  Posee columnas de datos

  #### Caracteristicas
  1.  Su tamaño puede cambiar
  2.  Diferentes tipos de columnas
  3.  Ejes etiquetados
  4.  Operaciones aritméticas en columnas y filas

  ```python
    fruits  count
  0   apple     10
  1  banana     20
  2   mango     15
  ```   

  <hr>

  ## Merge, Join y Concatenate

  [merge.py](merge.py)

  `df3 = df1.merge(df2, on='Title', how='inner')`

  Se obtiene los datos en común de ambos tomando como refencia a <span>title</span> DataFrames  
  <br>
  <ins>Inner merge</ins>

  ```python
      Player_x  Points Title  Player_y  Power
  0   player1   8      Game1  player1   punch
  ```
  * Player_x -> atributo de df1
  * Player_y -> atributo de df2

  <ins>Left merge</ins>
  <br>  
  Con el valor how = <span>left</span> Se obtienen todos los valores del DataFrame izq teniendo como referencia el atributo Player del primer DataFrame (df1) y los valores en comun que posee el segundo(df2). 

  En caso de no haber coincidencias se agrega NaN 

  `df5 = df1.merge(df2, on='Player', how='left')`

  ```python 
  0  player1       8   Game1  punch   Game1
  1  player2       9   Game2    NaN     NaN
  2  player3       6   Game3    NaN     NaN
  ```

  <ins>Right merge</ins>  
  <br>
  Con el valor <code>how = <span>right</span></code> Se obtienen todos los valores del DataFrame der   
  teniendo como referencia el atributo Player del segundo DataFrame (df2)   
  y los valores en comun que posee el primero(df1).

  `df5 = df1.merge(df2, on='Player', how='right')`

  <pre>
      Player   Points   Title_x   Power   Title_y
  <hr class="code-line">
  0  player1     8.0     Game1    punch   Game1
  1  player5     NaN     NaN      kick    Game5
  2  player6     NaN     NaN      elbow   Game6
  </pre>  

  <ins>Outer merge</ins>  
  <br>
  Con el valor <code>how = <span>outer</span></code> se obtienen todos los valores de los   
  DateFrames incluyendo aquellos atributos que no poseen.

  <pre>
      Player  Points Title_x  Power Title_y <hr>
  0  player1     8.0   Game1  punch   Game1
  1  player2     9.0   Game2    NaN     NaN
  2  player3     6.0   Game3    NaN     NaN
  3  player5     NaN     NaN   kick   Game5
  4  player6     NaN     NaN  elbow   Game6
  </pre>
  <br>

  ### Join
  <br>
  Mientras que Merge requiere de atributos en comun, Join une dos DataFrames a partir de su índice.

  <br>
  <br>    
  <ins>Inner Join</ins>
  <br>  
  <br>
  <code>df3 = df1.join(df2, how='inner')</code>

  <pre>
      Player  Points  Title  Players  Power Titles <hr>
  L2  player1       8  Game1  player5   kick  Game5
  L3  player2       9  Game2  player6  elbow  Game6
  </pre>

  <ins>Left Join</ins>

  incorpora siempre los indices del primero, y luego aquellos indice que no posee el segundo les incorpora un valor NaN 

  <pre>
      Player  Points  Title  Players  Power Titles <hr>
  L2  player1       8  Game1  player5   kick  Game5
  L3  player2       9  Game2  player6  elbow  Game6
  L4  player3       6  Game3      NaN    NaN    NaN
  </pre>

  <ins>Right Join</ins>

  Lo mismo pero incorporando esta vez los valores del DataFrame der. 

  <pre>
      Player  Points  Title  Players  Power Titles <hr>
  L1      NaN     NaN    NaN  player1  punch  Game1
  L2  player1     8.0  Game1  player5   kick  Game5
  L3  player2     9.0  Game2  player6  elbow  Game6
  </pre>

  <ins>Outter Join</ins>

  Se obtienen todos los indices en total de los dos DataFrames 

  <pre>
      Player  Points  Title  Players  Power Titles <hr>
  L1      NaN     NaN    NaN  player1  punch  Game1
  L2  player1     8.0  Game1  player5   kick  Game5
  L3  player2     9.0  Game2  player6  elbow  Game6
  L4  player3     6.0  Game3      NaN    NaN    NaN
  </pre>
  <br>

  ### Concatenate  
  <br>
  <code>df3 = pd.concat([df1, df2])</code>    
  <br><br>  
  Se concatena un df con otro

  <pre>
      Player  Points  Title  Players  Power Titles <hr> 
  L2  player1     8.0  Game1      NaN    NaN    NaN
  L3  player2     9.0  Game2      NaN    NaN    NaN
  L4  player3     6.0  Game3      NaN    NaN    NaN
  L1      NaN     NaN    NaN  player1  punch  Game1
  L2      NaN     NaN    NaN  player5   kick  Game5
  L3      NaN     NaN    NaN  player6  elbow  Game6
  </pre>

  <br><br>  
  <hr>
  <br>  

  ## Importando y analizando el conjunto de datos

  * `pd.read_csv('file.csv')` -> Lee los datos a traves de un dataframe
  * `variable.head(num)` -> Lee los primeros 5 registros por defecto o acepta una cantidad a visualizar
  * `print(cars.tail(num))` -> Lee los ultimos 5 registros o x cantidad
  * Estos metodos devuelven un valor <span>unnamed=0</span> -> registros que no poseen valor
  * `file.shape` -> Se obtiene una tupla con dos items: el numeros de filas y de columnas.
  * <span>* </span>`file.info(null_counts=True)`  
  info resumiendo cada columna del df, contandos el numero de registros nulos   
  y el tipo de dato registrado 
  
<pre>
class pandas.core.frame.DataFrame'
RangeIndex: 32 entries, 0 to 31
Data columns (total 12 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   Unnamed: 0  32 non-null     object
 1   mpg         32 non-null     float64
 2   cyl         32 non-null     int64
 3   disp        32 non-null     float64
 4   hp          32 non-null     int64
 5   drat        32 non-null     float64
 6   wt          32 non-null     float64
 7   qsec        32 non-null     float64
 8   vs          32 non-null     int64
 9   am          32 non-null     int64
 10  gear        32 non-null     int64
 11  carb        32 non-null     int64
dtypes: float64(5), int64(6), object(1)   
 <span>***Cantidad de datos por tipo *** </span>
memory usage: 2.9+ KB
</pre>  
<br>  

* `cars.mean()` -> Muestra el promedio de cada atributo
* `cars.median()` -> Muestra la mediana de cada atributo
* `cars.std()` -> Desviación estandar de cada atributo
* `cars.max()` -> El valor máximo de cada atributo
* `cars.min()` -> El valor mínimo de cada atributo
* `cars.count()` -> numero de registros no nulos de cada columna
* `cars.describe()` -> resumen descriptivo con todos datos estadísticos previos

<pre>
             mpg        cyl        disp          hp       drat         wt       qsec         vs         am       gear     carb
count  32.000000  32.000000   32.000000   32.000000  32.000000  32.000000  32.000000  32.000000  32.000000  32.000000  32.0000
mean   20.090625   6.187500  230.721875  146.687500   3.596563   3.217250  17.848750   0.437500   0.406250   3.687500   2.8125
std     6.026948   1.785922  123.938694   68.562868   0.534679   0.978457   1.786943   0.504016   0.498991   0.737804   1.6152
min    10.400000   4.000000   71.100000   52.000000   2.760000   1.513000  14.500000   0.000000   0.000000   3.000000   1.0000
25%    15.425000   4.000000  120.825000   96.500000   3.080000   2.581250  16.892500   0.000000   0.000000   3.000000   2.0000
50%    19.200000   6.000000  196.300000  123.000000   3.695000   3.325000  17.710000   0.000000   0.000000   4.000000   2.0000
75%    22.800000   8.000000  326.000000  180.000000   3.920000   3.610000  18.900000   1.000000   1.000000   4.000000   4.0000
max    33.900000   8.000000  472.000000  335.000000   4.930000   5.424000  22.900000   1.000000   1.000000   5.000000   8.0000  
</pre>
<br>    
<hr> 
<br>

## Data Cleaning

Data Cleaning o data cleansing es el proceso de detección,   
correción o eliminación de registros corruptos o incorrectos de una estructura de datos,   
tabla o base de datos. 
* Se reemplaza, modifica o borra datos incompletos o irrelevantes

<ins>Métodos y atributos</ins> 

* `file.rename(columns={'Unnamed: 0':'model'})` -> Renombra el atributo "Unnamed: 0" a "model
* `file.attribute.fillna(file.attribute.mean())` -> Rellena los valores null del atributo con su promedio
*  `file.drop(columns=['attribute_name'])` -> Quita un atributo <span class="alert">(Quita, no elimina)</span>
*  `df = cars[['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt',  'qsec', 'vs', 'am', 'gear', 'carb']].corr()`  
Se obtiene una <span>Correlación matricial</span>    
Una <span class="highlight">matriz correlacional</span> muestra en pantalla el grado de correlacion que tiene una variable con otra.

* En un rango de a 1 y -1. Cuanto mas cercano al 1 mas correlatividad existe.  
* Los valores con correlatividad 1.0 son ellos mismos(por lo general).  
* Si un atributo cambia, y su correlatividad es alta es mayor el grado de cambio del otro.
* Cuanto mas cercano al 0 menor es la correlación.

<pre>
        mpg       cyl      disp        hp      drat        wt      qsec        vs        am      gear      carb
mpg   1.000000 -0.852162 -0.847551 -0.776168  0.681172 -0.867659  0.385292  0.664039  0.599832  0.480285 -0.550925
cyl  -0.852162  1.000000  0.902033  0.832447 -0.699938  0.782496 -0.555819 -0.810812 -0.522607 -0.492687  0.526988
disp -0.847551  0.902033  1.000000  0.790949 -0.710214  0.887980 -0.399914 -0.710416 -0.591227 -0.555569  0.394977
hp   -0.776168  0.832447  0.790949  1.000000 -0.448759  0.658748 -0.664519 -0.723097 -0.243204 -0.125704  0.749812
drat  0.681172 -0.699938 -0.710214 -0.448759  1.000000 -0.712441  0.055749  0.440278  0.712711  0.699610 -0.090790
wt   -0.867659  0.782496  0.887980  0.658748 -0.712441  1.000000 -0.156305 -0.554916 -0.692495 -0.583287  0.427606
qsec  0.385292 -0.555819 -0.399914 -0.664519  0.055749 -0.156305  1.000000  0.719779 -0.274613 -0.262733 -0.641945
vs    0.664039 -0.810812 -0.710416 -0.723097  0.440278 -0.554916  0.719779  1.000000  0.168345  0.206023 -0.569607
am    0.599832 -0.522607 -0.591227 -0.243204  0.712711 -0.692495 -0.274613  0.168345  1.000000  0.794059  0.057534
gear  0.480285 -0.492687 -0.555569 -0.125704  0.699610 -0.583287 -0.262733  0.206023  0.794059  1.000000  0.274073
carb -0.550925  0.526988  0.394977  0.749812 -0.090790  0.427606 -0.641945 -0.569607  0.057534  0.274073  1.000000
</pre>

* <span>Ejemplo</span>: la correlación entre cilindrada(cyl) y desplazamiento(disp) es igual a 0.9 aprox.    
Esto significa que si la cilindrada aumenta una unidad el desplazamiento aumentará 0.9 (es decir sucedera lo mismo)  
Si cilindrada aumenta drat disminuye -0.7 aprox.

<br>

* `file.attribute = file.attribute.astype(float)` -> Modifica el tipo de dato  
Es util para cambiar datos como string a enteros etc.

<br>  
<hr>  
<br>

## Manipulando la estructura de datos

<ins>Métodos y atributos</ins>

<em>Seleccionar registros y columnas:</em>

* `cars.iloc[:, 0]` -> Obtiene todos los registros (:) de la columna 0 (0) 
* `cars.loc[:6, 'attribute1':'attribute2']` -> Obtiene los primeros 7 registros (:6) desde la columna "attribute1" hasta "attribute2"

<em>Asignar valores</em>

* `file['attribute'] = 1` -> Asigna el valor 1 a todos los registros del atributo 
* ```python
  f = lambda x: x*2
  file['attribute'] = file['am'].apply(f)
  ``` 
  Se aplica una función lambda para asignar un valor

<em>Ordenar valores</em>

* `cars.sort_values(by='attribute')` -> df en orden ascendente segun el valor del atributo
* `cars.sort_values(by='attribute', ascending=false)` -> df en orden descendente
 
<em>filtrar datos</em>

* `file['attribute'] > 6` -> Valor booleano de cada registro del atributo
* ```python
  filter1 = file['attribute'] > 6 
  print(file[filter1])
  ```
  Se obtienen los registros mayores a 6 del atributo
* `filter2 = (file['attribute1'] > 6) & (file['attribute2'] > 300)` -> combinación de filtros  
<br>  
<hr>  
<br>

## Introducción a Machine Learning

### ¿Para que se utiliza el Machine Learning?

<ins>Ejemplos</ins>

* La recomendación de productos de Amazon 
* Amazon <span class="highlight">Alexa</span>
* La recomendación de películas de Netflix
* Prediccion de tráfico de Google

### ¿Que es el Machine Learning?

<dfn>Machine Learning</dfn> forma parte del campo de la inteligencia artificial. Le permite a una máquina aprender sin una programación explícita.  
Los datos son la clave del aprendizaje algorítmico 

Para la incorporación de datos se utilizan dos tipo:  
*  datos de entrenamiento 
*  datos de testeo

Con los datos de entrenamiento se utiliza un algoritmo que posee un modelo de los datos.   
El mismo se aplica con el ingreso de nuevos datos donde se realiza luego del proceso la predicción  
 y se la compara con el modelo.   
Si la operación no es lo sufientemente correcta se repite el proceso hasta obtener un modelo final del entrenamiento









