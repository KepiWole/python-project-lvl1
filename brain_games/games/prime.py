from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    for i in range(2, int(question / 2 + 1)):
        if question % i == 0:
            return False
    return True


def generate_data():
    question = randint(2, 15)
    if is_prime(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
