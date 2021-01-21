"""Init of game."""

import random


def show_rules():
    """Show rules of game."""
    print('Answer "yes" if the number is prime. Otherwise answer "no".')


def prime_number(number):
    """Find number of numbers.

    Parameters:
        number: number of

    Returns:
        result: Prime
    """
    if number % 2 == 0:
        return number == 2

    odd_number = 3
    while odd_number * odd_number <= number and number % odd_number != 0:
        odd_number += 2

    return odd_number * odd_number > number


def correct_answer(value_question):
    """Find yes or no.

    Parameters:
        value_question: value question of game

    Returns:
        result: yes or no
    """
    if prime_number(value_question):
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
