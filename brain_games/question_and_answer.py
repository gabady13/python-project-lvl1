"""Play games."""

import random

from brain_games import constants

TYPE_OF_GAMES = constants.TYPE_GAMES
REPRESENTATION = 'REPRESENTATION'
VAL = 'VALUE'


def gcd(one_number, two_number):
    """Find NOD of numbers.

    Parameters:
        one_number: numeric of NOD
        two_number: numeric of NOD

    Returns:
        result: NOD
    """
    while one_number != 0 and two_number != 0:
        if one_number > two_number:
            one_number %= two_number
        else:
            two_number %= one_number

    return one_number + two_number


def get_question(game):
    """Get question of game.

    Parameters:
        game: name game

    Returns:
        question: question of game
    """
    question = None

    if game is TYPE_OF_GAMES.even:
        question = question_even()
    elif game is TYPE_OF_GAMES.calc:
        question = question_calc()
    elif game is TYPE_OF_GAMES.gcd:
        question = question_gcd()

    return question


def question_even():
    """Get question of game.

    Returns:
        question: question of game
    """
    random_value = random.randint(1, 1000)
    return {REPRESENTATION: random_value, VAL: [random_value]}


def question_calc():
    """Get question of game.

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
        if question[REPRESENTATION] % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
    elif game is TYPE_OF_GAMES.calc:
        answer = str(eval(question[REPRESENTATION]))
    elif game is TYPE_OF_GAMES.gcd:
        num_one = question[VAL][0]
        num_two = question[VAL][1]
        answer = str(gcd(num_one, num_two))

    return answer
