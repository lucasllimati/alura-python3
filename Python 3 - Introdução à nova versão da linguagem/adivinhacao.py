print("*" * 20)
print("Bem vindo no jogo da Adivinhação")
print("*" * 20)

numeroSecreto = 10
tentativas = 3
rodada = 1

while (rodada <= tentativas):
    # Chute sem conversão, ele considera STRING como padrão
    # chuteStg = int(input("Digite o seu número: "))
    print(f'Tentativa {rodada} de {tentativas}')
    chute = int(input("Digite o seu número: "))
    print("Você digitou" , chute)

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    # if (numeroSecreto == chute):
    #     print("Você acertou!")
    # else:
    #     if(numeroSecreto > chute):
    #         print("Você errou! O seu chute foi maior que o número secreto")
    #     else:
    #         print("Você errou! O seu chute foi menor que o número secreto")

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto")
    rodada += 1

print("Fim do jogo")    