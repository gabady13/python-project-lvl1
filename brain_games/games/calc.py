"""Init of game."""

import random
from operator import add, mul, sub

OPERATORS = ((add, '+'), (sub, '-'), (mul, '*'))


def show_rules():
    """Show rules of game."""
    print('What is the result of the expression?')


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game,
        correct_answer: correct answer of question
    """
    num_one = random.randint(1, 1000)
    num_two = random.randint(1, 1000)
    operation, sym = random.choice(OPERATORS)
    represent = '{0} {1} {2}'.format(num_one, sym, num_two)

    return represent, str(operation(num_one, num_two))
