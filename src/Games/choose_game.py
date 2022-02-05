import forca
import adivinhacao

def jogar():
    mensagem_inicial()
    jogo = escolhe_jogo()

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()
def mensagem_inicial():
    print("*****************")
    print("Escolha seu Jogo!")
    print("*****************")
def escolhe_jogo():
    print("(1) Forca (2) Adivinhação")
    return int(input("Qual o jogo?"))
if(__name__ == "__main__"):
    jogar()