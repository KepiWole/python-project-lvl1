from brain_games.cli import welcome_user
import prompt


def first_word(game):
    name = welcome_user()
    print(game.GAME_TASK)
    for x in range(3):
        question, right_answer = game.game_math()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if right_answer == str(answer):
            print('Correct!')
        else:
            print(
                f'\"{answer}\" is wrong answer ;(.'
                f' Correct answer was "{right_answer}".')
            return print(f"Let's try again, {name}!")
    else:
        return print(f'Congratulations, {name}!')
