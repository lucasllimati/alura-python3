import random



def jogar():

    imprimirCabecalho()
    palavraSecreta = carregarPalavraSecreta()

    letrasCorretas = inicializarPalavraSecreta(palavraSecreta)
    print(letrasCorretas)

    enforcou = False
    acertou = False
    erros = 0   

    # Enquanto True
    while (not enforcou and not acertou):
        
        chute = respostaUsuario()

        if (chute in palavraSecreta):
            chuteCorreto(chute, letrasCorretas, palavraSecreta)
        else:
            erros += 1
            desenhaForca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasCorretas        
        print(letrasCorretas)

    if(acertou):
        resultadoVencedor()
    else:
        resultadoPerdedor(palavraSecreta)
    print("Fim do jogo")

def imprimirCabecalho():
    print("*" * 30)
    print("Bem vindo no jogo de Forca")
    print("*" * 30)

def carregarPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def inicializarPalavraSecreta(palavra):
    return ["_" for letra in palavra]

def respostaUsuario():
    chute = input("Qual letra? ").upper().strip()
    return chute

def chuteCorreto(chute, letrasCorretas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasCorretas[index] = letra
        index += 1

def resultadoVencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def resultadoPerdedor(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()