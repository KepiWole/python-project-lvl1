from brain_games.cli import welcome_user
import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.RULE)
    attempts = 3
    for _ in range(attempts):
        question, right_answer = game.generate_data()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if right_answer == str(answer):
            print('Correct!')
        else:
            print(
                f'\"{answer}\" is wrong answer ;(.'
                f' Correct answer was "{right_answer}".')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
