#!/usr/bin/env python3
from random import randint
GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_math():
    question = randint(1, 10)
    if question % 2 == 0:
        right_answer = 'yes'
    elif question % 2 != 0:
        right_answer = 'no'
    return question, right_answer
