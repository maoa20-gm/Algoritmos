import pandas as pd

x = pd.read_csv("https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv")

print(x.head(5))

titanic_url = "https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv"
url1 = "/home/maoa/Documents/git/python-ml-course/datasets/titanic/titanic3.xls"

## Ficheros XLS y XLSX

titanic2 = pd.read_excel(url1, "titanic3")

print(titanic2.head(5))

# Como crear un excel o un csv a partir de los datos que he trabajado 


### Crea un csv

#titanic2.to_csv("/home/maoa/Documents/git/python-ml-course/datasets/titanic/prueba.csv")

### Crea un xls o xlsx

#titanic2.to_excel("/home/maoa/Documents/git/python-ml-course/datasets/titanic/prueba.xlsx")


