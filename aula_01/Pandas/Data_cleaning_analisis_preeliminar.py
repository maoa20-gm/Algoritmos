import pandas as pd

url1 = "/home/maoa/Documents/git/python-ml-course/datasets/titanic/titanic3.csv"
titanic = pd.read_csv(url1)


#print(titanic.head(10))

# Dimension del dataframe

print(titanic.shape) # Sin parentesis porque es un atributo no es un metodo como head()

print(titanic.tail(10))

print(titanic.columns.values) # Para saber el nombre de las columnas

# Resumen de los estadisticos basicos de las variables numericas

print(titanic.describe()) # Es como el summary() de R

print(titanic.dtypes) # Para saber el tipo de las variables en el dataframe


## Missing values

# Devuelve un vector de booleanos donde el True significa que existe un NaN
print(pd.isnull(titanic["body"]))

# Devuelve un vecto de booleanos donde el True significa que el data no es NaN
print(pd.notnull(titanic["body"]))

# el metodo values hace que se transforme en un array, ravel() hace que los valores del array
# se coloquen en una sola fila y con sum podemos sumar los datos en la respectiva fila.
print(pd.isnull(titanic["body"]).values.ravel().sum())

## Borrado de valores que faltan

# dropna() borra los NaN, con axis = 0  especificamos solo por filas y axis = 1 especificamos 
# solo por columna. El parametro how = "all" borra las filas donde todas los datos de las 
# columnas de esa fila tienen NaN.
titanic.dropna(axis = 0, how = "all")

print(titanic.shape)

titanic2 = titanic

# Con how = "any" borra las filas donde al menos una de las columnas de dicha fila tiene NaN
titanic2 = titanic2.dropna(axis = 0 , how = "any")

## Computo de los valores faltantes

# Con fillna(0) rellenamos los NaN con 0 
titanic.fillna(0)