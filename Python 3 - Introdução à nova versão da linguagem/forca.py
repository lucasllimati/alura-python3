def jogar():  
    print("*" * 30)
    print("Bem vindo no jogo de Forca")
    print("*" * 30)

    palavraSecreta = "banana".upper()
    letrasCorretas = ["_" for letra in palabraSecreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letrasCorretas)

    # Enquanto True
    while (not enforcou and not acertou):
        
        chute = input("Qual letra? ").upper().strip()

        if (chute in palavraSecreta):
            index = 0
            for letra in palavraSecreta:
                if (chute == letra):
                    letrasCorretas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letrasCorretas        
        print(letrasCorretas)

    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu!!!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()