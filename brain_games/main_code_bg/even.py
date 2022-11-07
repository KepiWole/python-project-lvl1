#!/usr/bin/env python3
from random import randint
game_saying = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_math():
    question = randint(1, 10)
    if question % 2 == 0:
        good_answer = 'yes'
    elif question % 2 != 0:
        good_answer = 'no'
    return question, good_answer
