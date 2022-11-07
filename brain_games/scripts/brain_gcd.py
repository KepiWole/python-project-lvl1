import math
from random import randint
from brain_games.cli import welcome_user


def rand_gcd():
    print("Welcome to the Brain Games!")
    name = welcome_user()[1]
    print('Find the greatest common divisor of given numbers.')
    good_result = 0
    while True:
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        print(f'Question: {num1, num2}')
        text = int(input('Your answer: '))
        if text == math.gcd(num1, num2):
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}!')
        elif text != math.gcd(num1, num2):
            return print(
                f'\'{text}\' is wrong answer ;(. Correct answer was'
                f'\'{math.gcd(num1, num2)}\'\nLet\'s try again, {name}!')


def main():
    rand_gcd()


if __name__ == '__main__':
    main()
