
def jogoTrivia():
    x:str = input("Digite seu primero numero: ")
    y:int =  0
    
    if x.isnumeric():
        y = int(x)
    else:
        while x.isnumeric()== False:
            x = input("Por favor digite un numero: ")
        y = int(x)    

    for n in range(20):
        print()

    for n in range (3):
        z:int = int(input("Adivine el numero del primer jugador: "))
        if z > y:
            print("Su numero es mayor que el del primer jugador")
        elif z < y:
            print("Su numero es menor que el del primer jugador")
        elif y == z:
            print("Correcto, usted adivino el numero")
            break

jogoTrivia()



# Construa uma função fat que recebe um numero inteiro positivo como argumento e 
# devolve o fatorial desse número.

def fatorial():
    x:str = input("Digite um numero: ")
    numero:int = 0
    resultado:int = 1
    if x.isnumeric():
        numero = int(x)
    else:
        while x.isnumeric() == False:
            x = input("Digite por favor solo datos numericos:")
        numero = int(x)


    for n in range(0,numero):
        resultado = resultado * (n+1)

    return print(resultado)    


fatorial()

            



