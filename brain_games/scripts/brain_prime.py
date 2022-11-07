from random import randint
from brain_games.cli import welcome_user


def even():
    prime = 0
    result = randint(1, 10)
    print(f'Question: {result}')
    text = input('Your answer: ').lower()
    if ((result > 1)
            and (result % 2 != 0 or result == 2)
            and (result % 3 != 0 or result == 3)):
        prime += result
        return text, result, prime
    else:
        return text, result, prime


def prime():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    good_result = 0
    while True:
        text, result, prime = even()
        if (result == prime and text == 'yes'
                or result != prime and text == 'no'):
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}')
        else:
            text2 = ''
            if result == prime:
                text2 += 'yes'
            elif result != prime:
                text2 += 'no'
            return print(
                f'\'{text}\' is wrong answer ;(. Correct answer was '
                f'\'{text2}\'.\nLet\'s try again, {name}!')


def main():
    prime()


if __name__ == '__main__':
    main()
