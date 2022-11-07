from brain_games.cli import welcome_user
import prompt


def rounds(question, good_answer):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    if str(good_answer) == str(answer):
        print('Correct!')
        return  True
    else:
        print(
            f'\"{answer}\" is wrong answer ;(. Correct answer was "{good_answer}".')


def first_word(game):
    name = welcome_user()
    print(game.game_saying)
    result = 0
    while result != 3:
        question, good_answer = game.game_math()
        if rounds(question, good_answer) == True:
            result += 1
        else:
           return print(f"Let's try again, {name}!")
    else:
        return print(f'Congratulations, {name}!')
