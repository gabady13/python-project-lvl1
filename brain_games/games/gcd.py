"""Init of game."""

import random

DESCRIPTION = 'Find the greatest divisor of given numbers.'


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


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game
        correct_answer: correct answer of question
    """
    num_one = random.randint(1, 1000)
    num_two = num_one * random.randint(1, 100)
    represent = '{0} {1}'.format(num_one, num_two)

    return represent, str(gcd(num_one, num_two))
