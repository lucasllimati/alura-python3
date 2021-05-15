def jogar():  
    print("*" * 30)
    print("Bem vindo no jogo de Forca")
    print("*" * 30)

    palavraSecreta = "BANANA"
    enforcou = False
    acertou = False

    # Enquanto True
    while (not enforcou and not acertou):
        chute = input("Qual letra? ").upper().strip()

        index = 0
        for letra in palavraSecreta:
            if (chute == letra):
                print(f'Encontrei a letra {chute} na posição {index}.')
            index += 1

        print("Jogando...")
    print(palavra2)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()