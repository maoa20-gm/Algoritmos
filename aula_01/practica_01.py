'''
def hello():
    print("Oi mundo!")
    print("Oi de novo!")

hello()

def continha():
    print(798 - 2 * 378)
    
continha()


def somaQuadrados(a,b):
    return print(a*a + b*b)

somaQuadrados(5,7)


pergunta1 =  "Qual é a Capital da Nicaragua? \n a) Atahualpa\n b) Managua \n c) San Jose \n d) Tegucigalpa"


def passoumedia(nota):
    if nota >= 7.0:
        return True
    else:
        return False


passoumedia(9)    
'''

'''
def compararComprimentos():
    x = input("Salude por favor: ")
    y = input("Salude de nuevo: ")
    if len(x) == len(y):
        return True
    else:
        return False

'''


def somaDigitos():
    x = input("Digite un numero de tres digitos: ")
    total = 0
    while len(x) != 3:
       x = input("Digite por favor un numero de tres digitos: ")
    z = int(x)  # un integer 
    while (z>0):
        restante = z%10
        total = total + restante
        z = z // 10
    return print(total)    


def ordemCrescente():
    y = int(input("Digite un numero de tres digitos: "))
    primer_numero = y%10
    segundo_numero = (y//10)%10
    restante = y//10
    tercer_numero = (restante//10)%10
    if (primer_numero > segundo_numero):
        primer_numero = segundo_numero
        segundo_numero = primer_numero
    if (primer_numero > tercer_numero):
        primer_numero = tercer_numero
        tercer_numero = primer_numero    
    if (segundo_numero > tercer_numero):
        segundo_numero = tercer_numero
        tercer_numero = segundo_numero
    return(print(primer_numero,segundo_numero,tercer_numero))

def is_numeric(numero):
    try:
        int(numero)
    except ValueError:
        return False
    return True


def tipoParametro():
    x = input("Digite solo un caracter: ")
    if len(x) > 1:
        x = input("Por favor digite solo un caracter, osea, un caracter de tamano 1: ")
    if is_numeric(x) == False:
        print(0)
    elif is_numeric(x) == True:
        print(1)
    else:
        print(-1)

def quatroNumeros():
    x = input("Digite un numero de tres digitos: ")
    y = input("Digite otro numero de tres digitos: ")
    z = input("Digite otro numero de tres digitos: ")
    m = input("Digite otro numero de tres digitos: ")
    if len(x) != 3:
        break
    if len(y) != 3:
        break
    if len(z) != 3:
        break
    if len(m) != 3:
        break
    if x%3 == 0 and (x ** (1/2) == round(x ** (1/2))):
        if (y%3 == 0) & (y ** (1/2) == round(y ** (1/2))):
            if (z%3 == 0) & (z ** (1/2) == round(z ** (1/2))):
                if (m%3 == 0) & (m ** (1/2) == round(m ** (1/2))):
    
        
        
    
        

    
    


