def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        prRed("Invalid input. Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        prLightPurple("You guess it!")
        break
    elif player_number > computer_number:
        prYellow("Too High!")
    else:
        prCyan("Too Low!")
