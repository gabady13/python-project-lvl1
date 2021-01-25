"""Init of game."""

import random

DESCRIPTION = 'Answer "yes" if the number is prime. Otherwise answer "no".'


def is_prime(number):
    """Find number of numbers.

    Parameters:
        number: number of

    Returns:
        result: Prime
    """
    divider = 2
    while number % divider != 0:
        divider += 1

    return number == divider


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game
        correct_answer: correct answer of question
    """
    random_value = random.randint(1, 1000)

    if is_prime(random_value):
        answer = 'yes'
    else:
        answer = 'no'

    return random_value, answer
