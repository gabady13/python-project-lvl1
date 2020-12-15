"""Play games."""

import prompt

from brain_games import cli, constants, question_and_answer
from brain_games.scripts import brain_game

TYPE_OF_GAMES = constants.TYPE_GAMES
COUNT_ROUND = 3
REPRESENTATION = 'REPRESENTATION'
VAL = 'VALUE'


def show_rules(game):
    """Show rules of game.

    Parameters:
        game: name game
    """
    str_rules = ''

    if game is TYPE_OF_GAMES.even:
        str_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game is TYPE_OF_GAMES.calc:
        str_rules = 'What is the result of the expression?'
    elif game is TYPE_OF_GAMES.calc:
        str_rules = 'Find the greatest divisor of given numbers.'

    print(str_rules)


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
        question = question_and_answer.get_question(game)
        print('Question: {0}'.format(question[REPRESENTATION]))
        answer_of_user = prompt.string('Your answer: ')
        answer_correct = question_and_answer.get_correct_answer(game, question)
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
    brain_game.main()
    name = cli.get_name_user()
    show_rules(game)
    ask_questions(game, name)
