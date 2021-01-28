"""Init of game."""

import random

DESCRIPTION = 'What number is missing in the progression?'
DIMENSION = 10


def generate_progression(start, diff, length):
    """Generate new progression.

    Parameters:
        start: start progression
        diff: difference progression
        length: length progression

    Returns:
        progression: question of game
    """
    progression = []
    while length > 0:
        progression.append(str(start))
        start += diff
        length -= 1
    return progression


def get_question_and_answer():
    """Get even question of game.

    Returns:
        question: question of game
        correct_answer: correct answer of question
    """
    missed_position = random.randint(1, DIMENSION)
    start = random.randint(1, 100)
    difference = random.randint(1, 100)
    represent_value = generate_progression(start, difference, DIMENSION)
    progression_value = represent_value[missed_position]
    represent_value[missed_position] = '..'
    return ' '.join(represent_value), progression_value
