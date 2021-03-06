"""Init of game."""

import random

DESCRIPTION = 'Answer "yes" if the number is even. Otherwise answer "no".'


def is_even(number):
    """Find even numbers.

    Parameters:
        number: number of

    Returns:
        result: even
    """
    return number % 2 == 0


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game
        correct_answer: correct answer of question
    """
    question = random.randint(1, 1000)

    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer
