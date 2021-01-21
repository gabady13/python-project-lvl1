"""Play games."""

import prompt

COUNT_ROUND = 3


def ask_questions(module, name):
    """Ask question.

    Parameters:
        module: type of game
        name: name of user

    """
    answer_of_user = None
    answer_correct = None
    round_of_game = 0
    while round_of_game < COUNT_ROUND:
        question, answer_correct = module.get_question_and_answer()
        print('Question: {0}'.format(question))
        answer_of_user = prompt.string('Your answer: ')
        if answer_of_user == answer_correct:
            print('Correct!')
            round_of_game += 1
        else:
            break

    if round_of_game < COUNT_ROUND:
        result_game = """\
'{0}' is wrong answer ;(. Correct answer was '{1}'
Let's try again, {2}!\
""".format(answer_of_user, answer_correct, name)

    else:
        result_game = 'Congratulations, {0}!'.format(name)

    print(result_game)


def get_name_user(module):
    """Do welcome and return user name.

    Parameters:
        module: type of game

    Returns:
        name: name of user.

    """
    print('Welcome to the Brain Games!')
    print()
    module.show_reles()
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def start_game(module):
    """Play games.

    Parameters:
        module: type of game

    """
    name = get_name_user(module)
    ask_questions(module, name)
