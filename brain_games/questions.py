"""Play games."""

import random

from brain_games import constants

TYPE_OF_GAMES = constants.TYPE_GAMES
REPRESENTATION = 'REPRESENTATION'
VAL = 'VALUE'


def get_question(game):
    """Get question of game.

    Parameters:
        game: name game

    Returns:
        question: question of game
    """
    question = None

    if game is TYPE_OF_GAMES.even or game is TYPE_OF_GAMES.prime:
        question = question_even()
    elif game is TYPE_OF_GAMES.calc:
        question = question_calc()
    elif game is TYPE_OF_GAMES.gcd:
        question = question_gcd()
    elif game is TYPE_OF_GAMES.progression:
        question = question_progression()

    return question


def question_even():
    """Get even question of game.

    Returns:
        question: question of game
    """
    random_value = random.randint(1, 1000)
    return {REPRESENTATION: random_value, VAL: [random_value]}


def question_calc():
    """Get calc question of game.

    Returns:
        question: question of game
    """
    num_one = random.randint(1, 1000)
    num_two = random.randint(1, 1000)
    operation = random.choice(['*', '-', '+'])
    represent = '{0} {1} {2}'.format(num_one, operation, num_two)
    calc_value = [num_one, num_two, operation]
    return {REPRESENTATION: represent, VAL: calc_value}


def question_gcd():
    """Get question of game.

    Returns:
        question: question of game
    """
    num_one = random.randint(1, 1000)
    num_two = num_one * random.randint(1, 100)
    represent = '{0} {1}'.format(num_one, num_two)
    gcd_value = [num_one, num_two]
    return {REPRESENTATION: represent, VAL: gcd_value}


def question_progression():
    """Get  progression question of game.

    Returns:
        question: question of game
    """
    index_space = random.randint(1, 10)
    num_start = random.randint(1, 100)
    num_iterator = random.randint(1, 100)
    count_element = 1
    progression_value = ''
    represent = ''

    while count_element <= 10:

        if count_element == index_space:
            represent = '{0} {1}'.format(represent, '..')
            progression_value = str(num_start)
        else:
            represent = '{0} {1}'.format(represent, num_start)

        num_start += num_iterator
        count_element += 1

    return {REPRESENTATION: represent, VAL: progression_value}
