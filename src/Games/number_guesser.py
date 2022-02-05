import random

def jogar():

    imprime_titulo()
    total_de_tentativas = define_dificuldade()
    numero_secreto = random.randrange(1,101)
    pontos = 1000

    for rodada in range(1, total_de_tentativas + 1):
        chute = recebe_chute(rodada, total_de_tentativas)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            mensagem_final_acertou(acertou, pontos)
            break
        else:
            check_maior_menor(maior, menor)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if rodada == total_de_tentativas:
                mensagem_final_errou()
def imprime_titulo():
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
def define_dificuldade():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas
def recebe_chute(rodada, total_de_tentativas):
    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
    return int(input("Digite um número entre 1 e 100: "))
def mensagem_final_acertou(acertou, pontos):
    if(acertou):
        print("Parabéns, você acertou e fez {} pontos!".format(pontos))
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
def check_maior_menor(maior, menor):
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
def mensagem_final_errou():
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