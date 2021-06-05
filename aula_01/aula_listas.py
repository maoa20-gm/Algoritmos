
def Trivia():
    pergunta1:str = "Qual a capital da Australia?"
    pergunta2:str = "Qual é a raça de Aragorn dos Senhor dos Aneis?"
    pergunta3:str = "Quem foi o presidente dos EEUU no ano 1995?"
    
    resposta1:str = "Camberra"
    resposta2:str = "Dunedain"
    resposta3:str = "Bill Clinton"

    pontos = 0   
    
    perguntas = [pergunta1, pergunta2, pergunta3]
    respostas = [resposta1, resposta2, resposta3]

    for n in range(len(perguntas)):
        for i in range(len(respostas)):
            fazerPergunta(perguntas[n],respostas[i], pontos)

    print("Você terminou com " + str(pontos) + " pontos.")

def fazerPergunta(enunciado:str, resposta:str, pontuacao:int):
    palpite:str = input(enunciado + " ")
    if palpite == resposta:
        print("Correto!")
        return pontuacao + 1
    else:
        print("Você errou nesta questão, como em toda a sua vida.")


Trivia()






