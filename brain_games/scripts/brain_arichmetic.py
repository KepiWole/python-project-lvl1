#!/usr/bin/env python3
from random import randint
import random


def arithmetic():
    arithmetic = ['-', '+', '*']
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    point = random.choice(arithmetic)
    if point == '-':
        result = num1 - num2
    elif point == '*':
        result = num1 * num2
    elif point == '+':
        result = num1 + num2
    return [result, num1, num2, point]
