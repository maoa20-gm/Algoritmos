# Crie uma função que recebe uma lista de números como argumento e 
# devolve uma lista onde todos os números da lista original foram
# elevados ao quadrado.

from typing import List

def Quadrado(listas:List) -> List:
    square = []
    for n in listas:
        square.append(n**2)
    return square

x = [2,4,5,10]

print(Quadrado(x))

# Crie uma função maiusculas() que recebe uma lista de strings como argumento e devolve
# uma lista onde todos as letras minúsculas do string original foram transformadas em
# maiúsculas. Dica: "abc".upper() == "ABC"

def maisculas(stringis:List) -> List:
    dados = []
    for n in stringis:
        dados.append(n.upper())
    return dados

y = ["a","b","v","dxeubdewbo"," miguel","veronica","oreo","missu","carmen"]

print(maisculas(y))        

# Crie uma função que, dada uma lista de números, devolve uma lista
# contendo apenas aqueles que são múltiplos de 7.

def MultiploSeven(numeros:List) -> List:
    seven = []
    for n in numeros:
        if n%7 == 0:
            seven.append(n)
    return seven


numeros = [7, 1554, 14, 1566, 23]
print(MultiploSeven(numeros))

# Crie uma função que recebe uma lista de números como argumento e 
# devolve a soma desses números.

def SomaLista(numeros:List) -> int:
    conteo = 0
    for n in numeros:
        conteo = conteo + n
    return conteo

print(SomaLista(numeros))

# Crie um programa que, dada uma lista de strings, devolve um string correspondente
# à concatenação de todos eles.

def concatenar(stringis:List[str]) -> str:
    juntos = ""
    for n in stringis:
        juntos = juntos + n
    return juntos

print(concatenar(y))        

# Crie uma função que recebe um string como argumento e elimina todos os
# caracteres desses string que não sejam alfanuméricos, devolvendo o
# string resultante.

def QuitAlfaNumeric(stringis:str) -> str:
    stringer = ""
    for n in stringis:
        if n.isnumeric() == False:
            stringer = stringer + n
    return stringer

z = "dhwmbsi562485fhshbd452dh1fddbud52452dfdejbfd"

print(QuitAlfaNumeric(z))

# Crie uma função que lê uma sequência de no máximo 100 números a partir do teclado,
# armazenando-os em uma lista. Quando o usuário digitar <ENTER> sem nenhum número, 
# seu programa deve calcular a média de todos os números armazenados e devolver
# esse valor.

def promedio() -> float:
    x:str = input("Digite un numero por favor o presione enter para terminar: ")
    armazenamento = []
    while x.isnumeric() == True:
        x = int(x)
        armazenamento.append(x)
        x = input("Digite un numero por favor o presione enter para terminar: ")
    mean = sum(armazenamento)/ len(armazenamento)
    return mean    

print(promedio())

# Crie uma função diferencaListas() que recebe duas listas l1 e l2 como argumentos
# e devolve uma lista contendo todos os elementos de l1 que não são também
# elementos de l2.

def diferencaListas(l1: List, l2:List) -> List:
    armazenamento = []
    errados = []
    for n in l1:
        for i in l2:
            if n == i:
                errados.append(n)
            else:
                armazenamento.append(n)
                break
    return armazenamento

l1 = [3,1,2]
l2 = [5,2,7]

print(diferencaListas(l1,l2))
















