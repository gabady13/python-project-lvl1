"""Init of game."""

import random

DESCRIPTION = 'What number is missing in the progression?'
DIMENSION = 10


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game
        correct_answer: correct answer of question
    """
    index_space = random.randint(1, 10)
    num_start = random.randint(1, 100)
    num_iterator = random.randint(1, 100)
    count_element = 1
    progression_value = ''
    represent_value = []

    while count_element <= DIMENSION:

        if count_element == index_space:
            represent_value.append('..')
            progression_value = str(num_start)
        else:
            represent_value.append(str(num_start))

        num_start += num_iterator
        count_element += 1

    return ' '.join(represent_value), progression_value
