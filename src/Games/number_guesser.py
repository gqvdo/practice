import random


def play():
    print_title()
    total_attempts = set_difficulty()
    secret_number = random.randrange(1, 101)
    points = 1000

    for game_round in range(1, total_attempts + 1):
        guess_number = guess(game_round, total_attempts)

        if guess_number < 1 or guess_number > 100:
            print("You must type a number between 1 and 100!")
            continue

        win = guess_number == secret_number
        higher = guess_number > secret_number
        lower = guess_number < secret_number

        if win:
            print_final_message_win(win, points)
            break
        else:
            check_higher_lower(higher, lower)
            lost_points = abs(secret_number - guess_number)
            points = points - lost_points
            if game_round == total_attempts:
                print_final_message_lose()


def print_title():
    print("\n*********************************")
    print("Welcome to the Guessing Game!")
    print("*********************************")


def set_difficulty():
    print("Which difficulty do you choose?")
    print("(1) Easy (2) Medium (3) Hard")
    difficulty = int(input("Set the difficulty: "))

    if difficulty == 1:
        total_attempts = 20
    elif difficulty == 2:
        total_attempts = 10
    else:
        total_attempts = 5
    return total_attempts


def guess(game_round, total_attempts):
    print("\nTry {} of {}".format(game_round, total_attempts))
    return int(input("Type a number between 1 and 100: "))


def check_higher_lower(higher, lower):
    if higher:
        print("You lost! Your guess was HIGHER than the secret number.")
    elif lower:
        print("You lost! Your guess was LOWER than the secret number.")


def print_final_message_win(win, points):
    if win:
        print("Congratulations, you WON and made {} points!".format(points))
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


def print_final_message_lose():
    print("     _______________   ")
    print("    /               \ ")
    print("   /                 \ ")
    print("/\/                   \/\ ")
    print("\ |  XXX         XXX  | /")
    print(" \| XXXXX       XXXXX |/ ")
    print("  |  XXX         XXX  |  ")
    print("  |                   |  ")
    print("  \__      XXX      __/  ")
    print("    |\     XXX     /|    ")
    print("    | |           | |    ")
    print("    | I I I I I I I |    ")
    print("    |  I I I I I I  |    ")
    print("    \_             _/    ")
    print("      \_         _/      ")
    print("        \_______/        ")


if __name__ == "__main__":
    play()
