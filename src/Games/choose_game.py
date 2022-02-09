import hangman
import number_guesser


def play():
    print_title()
    game = choose_game()

    if game == 1:
        hangman.play()
    elif game == 2:
        number_guesser.play()


def print_title():
    print("*****************")
    print("Choose your game!")
    print("*****************")


def choose_game():
    print("(1) Hangman (2) Guessing Game")
    return int(input("Which game you want to play?"))


if __name__ == "__main__":
    play()
