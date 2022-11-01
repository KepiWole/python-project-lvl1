from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main


main()


def progression():
    name = welcome_user()[1]
    print('What number is missing in the progression?')
    good_result = 0
    while True:
        stop = randint(20, 50)
        step = randint(1, 5)
        result = list(range(randint(0, 9), stop, step))[0: 5]
        answer = str(result[randint(0, 4)])
        result = " ".join(map(str, (result)))
        printer = result.replace(answer, "..", 1)
        print(f'Question: {printer}')
        text = input('Your answer: ')
        if text == answer:
            good_result += 1
            print('Correct!')
            if good_result == 3:
                return print(f'Congratulations, {name}!')
        elif text != answer:
            return print(f'\'{text}\' is wrong answer ;(. Correct answer was \'{answer}\'.\nLet\'s try again, {name}!')


def main():
    progression()


if __name__ == '__main__':
    main()