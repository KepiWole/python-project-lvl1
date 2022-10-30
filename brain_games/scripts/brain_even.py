#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main


main()


def rand():
    name = welcome_user()[1]
    print('Answer "yes" if the number is even, otherwise answer "no".')
    good_result = 0
    while True:
        result = randint(1, 10)
        print(f'Question: {result}')
        text = input('Your answer: ').lower()
        if result % 2 == 0 and text == 'yes':
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}!')
        elif result % 2 != 0 and text == 'no':
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}!')
        else:
            return print(f"Let's try again, {name}!")


rand()
