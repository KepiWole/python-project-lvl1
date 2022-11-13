from random import randint
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data():
    question = randint(1, 10)
    if question % 2 == 0:
        right_answer = 'yes'
    elif question % 2 != 0:
        right_answer = 'no'
    return question, right_answer
