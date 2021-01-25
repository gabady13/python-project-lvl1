"""Play games."""

import prompt

COUNT_ROUND = 3


def welcome_user():
    """Do welcome and return user name.

    Returns:
        name: name of user.

    """
    print('Welcome to the Brain Games!')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def start_game(module):
    """Play games.

    Parameters:
        module: module game of Brain

    """
    name = welcome_user()
    print(module.DESCRIPTION)
    round_of_game = 0
    while round_of_game < COUNT_ROUND:
        question, answer_correct = module.get_question_and_answer()
        print('Question: {0}'.format(question))
        answer_of_user = prompt.string('Your answer: ')
        if answer_of_user == answer_correct:
            print('Correct!')
            round_of_game += 1
        else:
            print("""\
'{0}' is wrong answer ;(. Correct answer was '{1}'
Let's try again, {2}!\
                """.format(answer_of_user, answer_correct, name),
                  )
            break

    else:
        print('Congratulations, {0}!'.format(name))
