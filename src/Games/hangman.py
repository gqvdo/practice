import random

def jogar():

    imprime_titulo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(True):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros +=  1
            print("Ops, você errou! Faltam {} tentativas.".format(7-erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        if (enforcou or acertou):
            break

    mensagem_final(acertou, enforcou, palavra_secreta)
def imprime_titulo():
    print("\n***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")
def carrega_palavra_secreta(nome_arquivo="words.txt"):
    lista_palavras = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)

    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].upper()
    return palavra_secreta
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
def pede_chute():
    chute = input("\nQual letra?: ")
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def desenha_forca(erros):
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
def mensagem_final(acertou, enforcou, palavra_secreta):
    if(acertou):
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
    elif(enforcou):
            print("Puxa, você foi enforcado!")
            print("A palavra era {}".format(palavra_secreta))
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
if(__name__ == "__main__"):
    jogar()