import random


def play():
    print_title()
    secret_word = load_secret_word()
    correct_letters = show_correct_letters(secret_word)
    errors = 0

    print(correct_letters)

    while True:
        guess_letter = guess()

        if guess_letter in secret_word:
            set_correct_letters(guess_letter, correct_letters, secret_word)
        else:
            errors += 1
            print("Ops, wrong letter! {} attempts left.".format(7 - errors))
            print_hangman(errors)

        hanged = errors == 7
        win = "_" not in correct_letters
        print(correct_letters)
        if hanged or win:
            break

    final_message(win, hanged, secret_word)


def print_title():
    print("\n***************************")
    print("Welcome to Hangman!")
    print("***************************")


def load_secret_word(file_name="words"):
    wordlist = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            wordlist.append(line)

    number = random.randrange(0, len(wordlist))
    secret_word = wordlist[number].upper()
    return secret_word


def show_correct_letters(word):
    return ["_" for letter in word]


def guess():
    guess_letter = input("\nType the letter: ")
    guess_letter = guess_letter.strip().upper()
    return guess_letter


def set_correct_letters(guess_letter, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess_letter == letter:
            correct_letters[index] = letter
        index += 1


def print_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def final_message(win, hanged, secret_word):
    if win:
        print("Congratulations, you won!")
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
    elif hanged:
        print("You lose!")
        print("The word is {}".format(secret_word))
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


if __name__ == "__main__":
    play()
