from random import randint
game_saying = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_math():
    question = randint(1, 10)
    if ((question > 1)
            and (question % 2 != 0 or question == 2)
            and (question % 3 != 0 or question == 3)):
        good_answer = 'yes'
    else:
        good_answer = 'no'
    return question, good_answer
