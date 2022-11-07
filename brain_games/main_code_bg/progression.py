from random import randint
game_saying = 'What number is missing in the progression?'


def game_math():
    stop = randint(50, 100)
    step = randint(1, 5)
    result = list(range(randint(0, 9), stop, step))[: 5]
    good_answer = str(result[randint(0, len(result) - 1)])
    result = " ".join(map(str, (result)))
    question = result.replace(good_answer, "..", 1)
    return question, good_answer
