import math
from random import randint
GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game_math():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{num1} {num2}'
    right_answer = str(math.gcd(num1, num2))
    return question, right_answer
