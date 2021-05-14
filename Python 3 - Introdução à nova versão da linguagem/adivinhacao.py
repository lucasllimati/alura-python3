import random

def jogar():    

    print("*" * 30)
    print("Bem vindo no jogo da Adivinhação")
    print("*" * 30)

    # numeroSecreto = 10
    # numeroSecreto = round(random.random() * 100)
    # rodada = 1

    numeroSecreto = random.randrange(1, 101)
    print(f'Número secreto: {numeroSecreto}')
    tentativas = 0
    pontos = 1000

    print("Defina o nível de dificuldade")
    print("(1) - Fácil (2) - Médio (3) - Difícil")
    nivel = int(input("Defina um nível? "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    # Se o número for inválido, vai considerar a dificuldade dificil


    for rodada in range (1, tentativas + 1):
    # while (rodada <= tentativas):

        # Chute sem conversão, ele considera STRING como padrão
        # chuteStg = int(input("Digite o seu número: "))

        # String interpolation
        # print("Tentativa {} de {}".format(rodada, tentativas))

        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input("Valor inválido! Você deve digitar um número entre 1 e 100: "))
        print("Você digitou" , chute)

        # Primeira validação do jogo
        # if (numeroSecreto == chute):
        #     print("Você acertou!")
        # else:
        #     if(numeroSecreto > chute):
        #         print("Você errou! O seu chute foi maior que o número secreto")
        #     else:
        #         print("Você errou! O seu chute foi menor que o número secreto")

        if(chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100: ")
            continue

        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto

        if (acertou):
            print(f'Você acertou e fez {pontos} pontos.')
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos -= pontosPerdidos

        # Incremento While
        # rodada += 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()