import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


# Point
human_point = 0
computer_point = 0

while True:
    print('')
    # Game name
    game_name = 'Rock Paper Scissors'.title()
    print(game_name.center(100, ' '))

    # Give choice
    player_choice = input(
        '1. Rock\n2. Paper\n3. Scissors\n\nEnter your choice: ')

    # Type casting
    player = int(player_choice)

    # Checking whether number is 1, 2, 3
    if (player < 1 or player > 3):
        sys.exit(
            f'\nYou need to give 1, 2, or 3 value\n\nYou win {human_point} time\nComputer win {computer_point} time\n\n')

    # Computer choice
    computer_choice = random.choice('123')

    computer = int(computer_choice)

    # Printing choices
    print('\nYour choice: ' + str(RPS(player)).replace('RPS.', '').title())
    print('Computer choice: ' + str(RPS(computer)).replace('RPS.', '').title())

    # Game logic
    if (player != computer):
        if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            print('\nYou win...✌️🫡🥱\n')
            human_point += 1
            print(
                f'You win {human_point} time\nComputer win {computer_point} time')

        else:
            print('\nComputer wins...!😒😪🤔🤦‍♂️🤣\n')
            computer_point += 1
            print(
                f'You win {human_point} time\nComputer win {computer_point} time')

    else:
        print('\nMatch draw...!!!!!😒😪🤔🤦‍♂️🤣\n')
        print(
            f'You win {human_point} time\nComputer win {computer_point} time')
