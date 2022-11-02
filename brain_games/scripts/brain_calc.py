from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main
from random import randint
import random


main()


def arithmetic():
    arithmetic = ['-', '+', '*']
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    point = random.choice(arithmetic)
    if point == '-':
        result = num1 - num2
    elif point == '*':
        result = num1 * num2
    elif point == '+':
        result = num1 + num2
    return [result, num1, num2, point]


def rand_calc():
    name = welcome_user()[1]
    print('What is the result of the expression?')
    good_result = 0
    i = 0
    while i <= 3:
        result, num1, num2, point = arithmetic()
        i += 1
        print(f'Question: {num1}{point}{num2}')
        text = input('Your answer: ')
        if str(result) == str(text):
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}!')
        else:
            return print(
                f'\"{text}\" is wrong answer ;(. Correct answer was "{result}"'
                f'\nLet\'s try again, {name}')


def main():
    rand_calc()


if __name__ == '__main__':
    rand_calc()
