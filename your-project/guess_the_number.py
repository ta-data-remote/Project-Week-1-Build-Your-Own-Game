def magic_number(level):
    import random

    magic_number = 0

    if level == 1:
        magic_number = random.randint(1, 10)
    elif level == 2:
        magic_number = random.randint(1, 100)
    elif level == 3:
        magic_number = random.randint(-1000, 1000)

    return magic_number


def turns(level):
    turns = 0
    message = ''

    if level == 1:
        turns = 5
        message = 'You will have 5 turns\n'
    elif level == 2:
        turns = 7
        message = 'You will have 7 turns\n'
    elif level == 3:
        turns = 11
        message = 'You will have 11 turns\n'

    return turns, message


def pick_a_number_message(level):
    message = ''

    if level == 1:
        message = 'Pick a number between 1 and 10: '
    elif level == 2:
        message = 'Pick a number between 1 and 100: '
    elif level == 3:
        message = 'Pick a number between -1000 and 1000: '

    return message


how_to_play_the_game = '''The FunBrain Magician will pick a secret number and put it in his hat.
Your task is to guess what number it is. 
If your guess is higher or lower, you'll get a hint.\n'''

print(how_to_play_the_game)

level = input('''Pick a level

1: numbers from 1 to 10
2: numbers from 1 to 100
3: numbers from -1000 to 1000

You have to choose between 1, 2 or 3:
Your choice is: ''')

while True:
    try:

        level = int(level)

        if level < 1 or level > 3:
            print("You have to enter 1 or 2 or 3 other options aren't allowed:")
            level = input('Your choice is: ')
        else:
            break

    except ValueError:
        print("You have to enter 1 or 2 or 3 other options aren't allowed:")
        level = input('Your choice is: ')

magic_number = magic_number(level)
turns, turns_message = turns(level)
message = pick_a_number_message(level)

print(f'\n{turns_message}')

guess = None
current_turn = 0

print(magic_number)

while current_turn < turns and not guess == magic_number:
    try:
        guess = int(input(f'{message}'))

        if guess < magic_number:
            print('You need to guess higher.\n')
        elif guess > magic_number:
            print('You need to guess lower.\n')
        else:
            break

        current_turn += 1

    except ValueError:
        print('Invalid input, try again\n')

if current_turn == turns:
    print("Sorry you didn't guess the magic number")
    print(f"The magic number was {magic_number}")
else:
    print('\nGreat you guess it!')
    print(f'Magic number was {magic_number}')
