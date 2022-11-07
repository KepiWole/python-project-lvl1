#!/usr/bin/env python3
game_saying = 'What is the result of the expression?'
from random import randint
import random


def game_math():
    arithmetic = ['-', '+', '*']
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    point = random.choice(arithmetic)
    question = f"{num1} {point} {num2}"
    if point == '-':
        good_answer = num1 - num2
    elif point == '*':
        good_answer = num1 * num2
    elif point == '+':
        good_answer = num1 + num2
    return question, good_answer

