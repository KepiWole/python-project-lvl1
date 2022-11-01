from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main


main()


def prime():
    name = welcome_user()[1]
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    good_result = 0
    while True:
        result = randint(1, 20)
        print(f'Question: {result}')
        text = input('Your answer: ').lower()
        if result < 10 and text == 'yes':
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}')
        elif result > 10 and text == 'no':
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}')
        else:
            text2 = ''
            if result <= 9:
                text2 += 'yes'
            elif result >= 10:
                text2 += 'no'
            return print(
                f'\'{text}\' is wrong answer ;(. Correct answer was'
                f'\'{text2}\'.\nLet\'s try again, {name}')


def main():
    prime()


if __name__ == '__main__':
    main()
