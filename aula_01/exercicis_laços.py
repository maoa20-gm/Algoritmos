# Dado um string e um caratere (um string com apenas um elemento). Determinar se o caratere
# aparece alguma vez no string e em qual posicao 

def Posicao(text:str, caractere:str) -> int:
    posicion = 0
    achou = True
    for n in text:
        if n == caractere:
            achou = True
            break
        posicion = posicion + 1

    if achou == False:
        posicion = -1    

    return posicion


print(Posicao("ndeionidoendonefnorncnoncneepnepe", "i"))

def ContaOcorrencias(text:str, caractere:str) -> int:
    ocorrencias = 0
    achou = True
    for n in text:
        if n == caractere: 
            ocorrencias = ocorrencias + 1

    return ocorrencias

print(ContaOcorrencias("ndeionidoendonefnorncnoncneepnepe", "e"))


def AchaOcorrencias(text:str, caractere:str) -> list:
    if len(caractere) != 1:
        return -1

    posicoes = []
    posicao = 0
    for n in text:
        if n == caractere:
            posicoes.append(posicao)
        posicao = posicao + 1       

    return posicoes


print(AchaOcorrencias("ndeionidoendonefnorncnoncneepnepe", "f"))

def EncontrarPrimo(n:int) -> bool:
    if n < 2:
        return False

    resultado = True
    ultimo = n//2 + 1
    for i in range(2,ultimo):
        if n % i != 0:
            resultado = False
            break
    return resultado

print(EncontrarPrimo(1254))
