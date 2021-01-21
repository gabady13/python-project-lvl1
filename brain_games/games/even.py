"""Init of game."""

import random


def show_rules():
    """Show rules of game."""
    print('Answer "yes" if the number is even. Otherwise answer "no".')


def correct_answer(value_question):
    """Find yes or no.

    Parameters:
        value_question: value question of game

    Returns:
        result: yes or no
    """
    answer = 'no'

    if value_question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return answer


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game
        correct_answer: correct answer of question
    """
    random_value = random.randint(1, 1000)

    return random_value, correct_answer(random_value)
