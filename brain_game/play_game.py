"""Play games."""

import random

import prompt

from brain_game.scripts import brain_games
from brain_game import constants
from brain_game import cli

TYPE_OF_GAMES = constants.TYPE_GAMES
COUNT_ROUND = 3


def show_rules(game):
    """Show rules of game.

    Parameters:
        game: name game
    """
    str_rules = ''

    if game is TYPE_OF_GAMES.even:
        str_rules = 'Answer "yes" if the number is even, otherwise answer "no".'

    print(str_rules)


def get_question(game):
    """Get question of game.

    Parameters:
        game: name game

    Returns:
        question: question of game
    """
    question = None

    if game is TYPE_OF_GAMES.even:
        question = random.randint(1, 1000)

    return question


def get_correct_answer(game, question):
    """Get question of game.

    Parameters:
        question: question
        game: name game

    Returns:
        answer: correct answer
    """
    answer = None

    if game is TYPE_OF_GAMES.even:
        if question % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

    return answer


def ask_questions(game, name):
    """Ask question.

    Parameters:
        game: type of game
        name: name of user

    """
    answer_of_user = None
    answer_correct = None
    round_of_game = 0
    while round_of_game < COUNT_ROUND:
        question = get_question(game)
        print('Question: {0}'.format(question))
        answer_of_user = prompt.string('Your answer: ')
        answer_correct = get_correct_answer(game, question)
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


def start_game(game):
    """Play games.

    Parameters:
        game: type of game

    """
    brain_games.main()
    name = cli.get_name_user()
    show_rules(game)
    ask_questions(game, name)
