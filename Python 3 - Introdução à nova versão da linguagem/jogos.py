import forca
import adivinhacao

def escolherJogo():
    print("*" * 30)
    print("*******Escolha um jogo *******")
    print("*" * 30)

    print("(1) - Forca (2) - Adivinhação")

    jogo = int(input("Escolha um jogo: "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolherJogo()